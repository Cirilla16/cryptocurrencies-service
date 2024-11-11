import datetime

import httpx
from fastapi import Header, Query, FastAPI
from typing import Optional, List, Dict
import pandas as pd
from fastapi import APIRouter

from app.models.response import CommRes

crypto_currencies_router = APIRouter(prefix="/crypto-currencies", tags=["Crypto Currencies"])
router = crypto_currencies_router

ALPHA_VANTAGE_BASE_URL = "https://www.alphavantage.co/query"
API_KEY = "14AKOXBPYLKCAI2R"

@router.get("/currencies/query_physical_currencies", response_model=CommRes[List[Dict[str,str]]], summary="", description="")
async def query_physical_currencies():
    physical_data_path='../resources/physical_currency_list.csv'
    physical_data=read_csv_currency_file(physical_data_path)
    return CommRes(data=physical_data)

@router.get("/currencies/query_digital_currencies", response_model=CommRes[List[Dict[str,str]]], summary="", description="")
async def query_digital_currencies():
    digital_data_path='../resources/digital_currency_list.csv'
    digital_data=read_csv_currency_file(digital_data_path)
    return CommRes(data=digital_data)



def read_csv_currency_file(path:str)->List[Dict[str,str]]:
    try:
        currency_data = pd.read_csv(path)
        print("CSV file successfully read. Here are the first few rows:")
        print(currency_data.head())
        return currency_data.to_dict(orient='records')
    except FileNotFoundError:
        print(f"File not found at: {path}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

@router.get("/exhange-rate/query", response_model=CommRes[Dict], summary="", description="")
async def query_exchange_rate(from_currency: str = Query('BTC', description=""),to_currency: str = Query('USD', description="")):
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
            print(data)
            return CommRes(data=data)
        else:
            print(f"Error: {response.status_code}")
