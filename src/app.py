from currencyapicom import Client
from fastapi import FastAPI

from config import Config
from validators import Convert

app = FastAPI()


@app.post("/convert/")
async def convert(data: Convert):
    client = Client(Config.CURRENCY_API_KEY)
    exchanges = client.latest()["data"]
    rate_to = exchanges[data.to_currency]["value"]
    rate_from = exchanges[data.from_currency]["value"]
    dollar_amount = 1 / rate_from * data.value
    value = dollar_amount * rate_to
    return {"value": value}
