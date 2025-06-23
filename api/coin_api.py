from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/coins")
def get_coin_prices():
    symbols = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'BNBUSDT', 'USDTUSDT']
    coin_data = []

    for symbol in symbols:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            coin_data.append({
                "symbol": symbol,
                "price": round(float(data["lastPrice"]), 2),
                "change": round(float(data["priceChangePercent"]), 2)
            })
    return coin_data
