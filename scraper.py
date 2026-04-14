import requests
import json
from bs4 import BeautifulSoup
import re

FUNDS = ["PHE"]

def get_fund(code):
    url = f"https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod={code}"

    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    text = r.text

    price = re.search(r"Son Fiyat \(TL\)\s*([\d,]+)", text)
    change = re.search(r"Günlük Getiri \(%\)\s*%([\d,]+)", text)

    return {
        "code": code,
        "price": float(price.group(1).replace(",", ".")) if price else None,
        "change": float(change.group(1).replace(",", ".")) if change else None
    }

data = [get_fund(f) for f in FUNDS]

with open("funds.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
