from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY=os.getenv("api_key")

app=FastAPI()

@app.get("/currency/pair/{initial}/{target}")
def currency_conversion(initial:str,target:str):
    url=f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}&base_currency={initial.upper()}&currencies={target.upper()}'
    response=requests.get(url)
    if response.status_code!=200:
        return JSONResponse(content={'error':'not found'},status_code=response.status_code)
    return JSONResponse(content=response.json(),status_code=response.status_code)

@app.get("/currency/historical/{code}/{date}/{month}/{year}")
def currency_history(code:str,date:str,month:str,year:str):
    url=f'https://api.freecurrencyapi.com/v1/historical?apikey={API_KEY}&date={year}-{month}-{date}&base_currency={code.upper()}'
    response1=requests.get(url)
    if response1.status_code!=200:
        return JSONResponse(content={'error':'not found'},status_code=response1.status_code)
    return JSONResponse(content=response1.json(),status_code=response1.status_code)