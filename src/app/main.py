import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
environment = os.getenv('ENV', 'product')
print(f'pwd: {os.getcwd()}, env: {environment}')
load_dotenv(f'./src/{environment}.env')
if not os.path.exists(f'./src/{environment}.env'):
    load_dotenv(f'./{environment}.env')

from fastapi.middleware.cors import CORSMiddleware
from src.app.routers.cryptocurrencies_api import crypto_currencies_router

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://host.docker.internal:5173",
    "http://localhost:53",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(crypto_currencies_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
