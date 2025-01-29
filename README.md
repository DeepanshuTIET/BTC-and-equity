# BTC Price and MT5 Equity Dashboard

A real-time dashboard application that displays Bitcoin (BTC) price from Binance and MetaTrader 5 account equity, built with Flask and Plotly.

## Features

- Real-time BTC price updates from Binance API (0.1-second intervals)
- Live MT5 account equity tracking (0.1-second intervals)
- Separate interactive charts for BTC price and MT5 equity
- Visual BTC position indicator (Buy/Sell status)
- Responsive design for desktop and mobile devices

## Prerequisites

- Python 3.7 or higher
- MetaTrader 5 terminal installed and configured
- Active internet connection for Binance API access

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Ensure your MetaTrader 5 terminal is:
   - Installed and running
   - Logged in with valid credentials
   - Properly configured for trading

2. The application will automatically connect to:
   - Binance public API for BTC prices
   - Local MT5 terminal for account equity and position data

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

3. The dashboard will display:
   - Current BTC price in USDT
   - Current MT5 account equity
   - Real-time charts for both metrics
   - Current BTC position status (Buy/Sell/No Position)

## Dashboard Components

### Price Display
- Real-time BTC price from Binance
- Account equity from MT5

### Charts
- Interactive BTC price chart
- Interactive MT5 equity chart
- Both charts update every 0.1 seconds

### Position Indicator
- Color-coded position status
  - Green: Buy position
  - Red: Sell position
  - Grey: No position
- Visual dot indicator
- Clear position text display

## Technical Details

- **Frontend**: HTML5, CSS3, JavaScript with jQuery
- **Backend**: Python Flask
- **Charts**: Plotly.js
- **Data Sources**:
  - Binance API for BTC prices
  - MetaTrader 5 Python package for trading data
- **Update Frequency**: 0.1 seconds for all real-time data

## Error Handling

The application includes comprehensive error handling for:
- Binance API connection issues
- MT5 terminal connection problems
- Data processing errors

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Binance for providing the cryptocurrency price API
- MetaQuotes for the MetaTrader 5 platform and Python integration
- Plotly team for the interactive charting library
