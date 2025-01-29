# BTC and Equity Dashboard

A real-time dashboard that displays Bitcoin prices from Binance and MetaTrader 5 account equity, built with Flask and interactive Plotly charts.

## 🌟 Features

- Real-time BTC price updates from Binance
- Live MT5 account equity tracking
- Interactive charts with Plotly
- BTC position indicator (Buy/Sell/No Position)
- Responsive design for all devices
- Thread-safe data handling
- Optimized performance with background updates

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/DeepanshuTIET/BTC-and-equity.git
   cd BTC-and-equity
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MT5 Credentials**
   Create a `.env` file in the root directory:
   ```env
   MT5_LOGIN=your_login_number
   MT5_PASSWORD=your_password
   MT5_SERVER=your_server_name
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the dashboard**
   Open `http://127.0.0.1:5000` in your web browser

## 📦 Dependencies

- Flask
- MetaTrader5
- Plotly
- Pandas
- Requests
- python-dotenv
- Threading (Python standard library)

## 🔧 Configuration

The application uses environment variables for MT5 configuration:
- `MT5_LOGIN`: Your MT5 account login number
- `MT5_PASSWORD`: Your MT5 account password
- `MT5_SERVER`: Your MT5 server name

## 🎯 Features in Detail

### Real-time Data Updates
- BTC price updates every 0.5 seconds
- MT5 equity tracking with live updates
- Position status monitoring for BTC trades

### Interactive Charts
- Separate charts for BTC price and MT5 equity
- Real-time updates with smooth animations
- Responsive design that adapts to screen size

### Performance Optimizations
- Background thread for data updates
- Thread-safe data handling
- Efficient MT5 connection management
- Optimized chart updates (every 2 seconds)
- Reduced memory footprint

## 🔒 Security

- Sensitive credentials stored in `.env` file
- `.env` file excluded from version control
- Secure MT5 connection handling

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Repository Information

- **Owner**: DeepanshuTIET
- **Repository**: [BTC-and-equity](https://github.com/DeepanshuTIET/BTC-and-equity)
- **Branch**: main
- **Visibility**: Public

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This application is for educational purposes only. Trading cryptocurrencies and forex carries significant risk. Always do your own research and trade responsibly.
