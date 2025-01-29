from flask import Flask, render_template, request, jsonify
import requests
import MetaTrader5 as mt5
import pandas as pd
import plotly
import plotly.graph_objs as go
import json
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import threading
import time

# Load environment variables
load_dotenv()

# MT5 Credentials
MT5_LOGIN = os.getenv('MT5_LOGIN')
MT5_PASSWORD = os.getenv('MT5_PASSWORD')
MT5_SERVER = os.getenv('MT5_SERVER')

app = Flask(__name__)

# Global variables to store data
btc_history = []
equity_history = []
MAX_HISTORY_LENGTH = 50  # Reduced from 100 to 50 for better performance
current_btc_price = None
current_equity = None
current_position = None
last_update_time = None

# Lock for thread-safe operations
data_lock = threading.Lock()

def initialize_mt5():
    """Initialize MT5 connection with credentials"""
    if not mt5.initialize(
        login=int(MT5_LOGIN) if MT5_LOGIN else None,
        password=MT5_PASSWORD,
        server=MT5_SERVER
    ):
        print("MT5 initialization failed")
        print(f"Error: {mt5.last_error()}")
        return False
    return True

def fetch_btc_price():
    """Fetch BTC price from Binance"""
    try:
        response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
        price_data = response.json()
        return float(price_data['price'])
    except Exception as e:
        print(f"Error fetching BTC price: {e}")
        return None

def update_data():
    """Background task to update data"""
    global current_btc_price, current_equity, current_position, last_update_time
    
    while True:
        try:
            # Fetch new data
            btc_price = fetch_btc_price()
            
            # Initialize MT5 and get data
            if initialize_mt5():
                account_info = mt5.account_info()
                equity = account_info.equity if account_info else None
                
                positions = mt5.positions_get()
                position = None
                if positions is not None:
                    for pos in positions:
                        if pos.symbol.startswith("BTC"):
                            position = "Buy" if pos.type == mt5.ORDER_TYPE_BUY else "Sell"
                            break
                
                mt5.shutdown()
                
                # Update global variables with thread safety
                with data_lock:
                    current_time = datetime.now()
                    
                    if btc_price:
                        current_btc_price = btc_price
                        btc_history.append({'timestamp': current_time, 'price': btc_price})
                        if len(btc_history) > MAX_HISTORY_LENGTH:
                            btc_history.pop(0)
                    
                    if equity:
                        current_equity = equity
                        equity_history.append({'timestamp': current_time, 'equity': equity})
                        if len(equity_history) > MAX_HISTORY_LENGTH:
                            equity_history.pop(0)
                    
                    current_position = position
                    last_update_time = current_time
            
        except Exception as e:
            print(f"Error in update_data: {e}")
        
        # Sleep for 0.5 seconds before next update
        time.sleep(0.5)

def create_charts():
    """Create charts with current data"""
    try:
        with data_lock:
            if not btc_history or not equity_history:
                return None
            
            # Create BTC price chart
            btc_df = pd.DataFrame(btc_history)
            btc_fig = go.Figure()
            btc_fig.add_trace(go.Scatter(
                x=btc_df['timestamp'],
                y=btc_df['price'],
                name='BTC Price',
                line=dict(color='#f2a900', width=2)
            ))
            btc_fig.update_layout(
                title='BTC Price',
                yaxis=dict(title='Price (USDT)'),
                plot_bgcolor='#f8f9fa',
                paper_bgcolor='#f8f9fa',
                height=400,
                margin=dict(t=30, b=30, l=50, r=50)
            )
            
            # Create Equity chart
            equity_df = pd.DataFrame(equity_history)
            equity_fig = go.Figure()
            equity_fig.add_trace(go.Scatter(
                x=equity_df['timestamp'],
                y=equity_df['equity'],
                name='MT5 Equity',
                line=dict(color='#2ecc71', width=2)
            ))
            equity_fig.update_layout(
                title='MT5 Equity',
                yaxis=dict(title='Equity (USD)'),
                plot_bgcolor='#f8f9fa',
                paper_bgcolor='#f8f9fa',
                height=400,
                margin=dict(t=30, b=30, l=50, r=50)
            )
            
            return {
                'btc_chart': json.dumps(btc_fig, cls=plotly.utils.PlotlyJSONEncoder),
                'equity_chart': json.dumps(equity_fig, cls=plotly.utils.PlotlyJSONEncoder)
            }
    except Exception as e:
        print(f"Error creating charts: {e}")
        return None

@app.route('/')
def index():
    charts = create_charts()
    return render_template('index.html',
                         btc_price=current_btc_price,
                         equity=current_equity,
                         btc_position=current_position,
                         charts=charts)

@app.route('/update_data')
def get_updated_data():
    with data_lock:
        data = {
            "btc_price": current_btc_price,
            "equity": current_equity,
            "btc_position": current_position
        }
        
        # Only update charts every 2 seconds
        if last_update_time and (datetime.now() - last_update_time).total_seconds() >= 2:
            data["charts"] = create_charts()
            
        return jsonify(data)

if __name__ == '__main__':
    # Start the background update thread
    update_thread = threading.Thread(target=update_data, daemon=True)
    update_thread.start()
    
    app.run(debug=True, use_reloader=False)
