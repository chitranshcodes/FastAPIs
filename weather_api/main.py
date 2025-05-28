from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

app=FastAPI()

load_dotenv()
API_KEY=os.getenv("API_KEY")

templates=Jinja2Templates(directory="templates")

@app.get("/weather/city/{c}")
def weather(c:str):
    url=f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={c}"
    response=requests.get(url)
    if response.status_code!=200:
        return JSONResponse(content={'error':'not found'},status_code=response.status_code)
    return JSONResponse(content=response.json())

@app.get("/weather-ui/city/{c}")
def weatherui(request:Request,c:str):
    url=f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={c}"
    response=requests.get(url)
    if response.status_code==200:
        return templates.TemplateResponse("weather.html",{"request":request,'data':response.json(),'city':c})
    return templates.TemplateResponse("weather.html",{"request":request,'data':None,'city':c})