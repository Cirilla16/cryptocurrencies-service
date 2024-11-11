import datetime
from typing import List, Dict
import httpx
from fastapi import HTTPException

from app.services.base import BaseService
import pandas as pd
ALPHA_VANTAGE_BASE_URL = "https://www.alphavantage.co/query"
API_KEY = "14AKOXBPYLKCAI2R"

class CryptoCurrenciesService(BaseService):
    def __init__(self):
        super().__init__()

    def read_csv_currency_file(self,path: str) -> List[Dict[str, str]]:
        try:
            currency_data = pd.read_csv(path)
            print("CSV file successfully read. Here are the first few rows:")
            print(currency_data.head())
            return currency_data.to_dict(orient='records')
        except FileNotFoundError:
            print(f"File not found at: {path}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    async def query_exchange_rate(self, from_currency: str,to_currency: str):
        url = 'https://www.alphavantage.co/query'
        PARAMS = {
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": from_currency,
            "to_currency": to_currency,
            "apikey": API_KEY
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(ALPHA_VANTAGE_BASE_URL, params=PARAMS)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Error: {response.status_code}")
    async def get_fx_daily(self, from_symbol: str, to_symbol: str, start_date: datetime.datetime, end_date: datetime.datetime):
        params = {
            "function": "FX_DAILY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "apikey": API_KEY,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(ALPHA_VANTAGE_BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                return await self.filter_by_time(data['Time Series FX (Daily)'], start_date, end_date)
            else:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Failed to fetch data from Alpha Vantage API: {response.text}"
                )
    async def get_fx_weekly(self, from_symbol: str, to_symbol: str, start_date: datetime.datetime, end_date: datetime.datetime):
        params = {
            "function": "FX_WEEKLY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "apikey": API_KEY,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(ALPHA_VANTAGE_BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                return await self.filter_by_time(data['Time Series FX (Weekly)'], start_date, end_date)
            else:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Failed to fetch data from Alpha Vantage API: {response.text}"
                )
    async def get_fx_monthly(self, from_symbol: str, to_symbol: str, start_date: datetime.datetime, end_date: datetime.datetime):
        params = {
            "function": "FX_MONTHLY",
            "from_symbol": from_symbol,
            "to_symbol": to_symbol,
            "apikey": API_KEY,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(ALPHA_VANTAGE_BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                return await self.filter_by_time(data['Time Series FX (Monthly)'], start_date, end_date)
            else:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Failed to fetch data from Alpha Vantage API: {response.text}"
                )
    async def filter_by_time(self, data: Dict, start_date: datetime.datetime, end_date: datetime.datetime):
        filtered_data = {}
        for key, value in data.items():
            if start_date <= datetime.datetime.strptime(key, "%Y-%m-%d") <= end_date:
                filtered_data[key] = value
        return filtered_data