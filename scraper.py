import requests
import json

FUNDS = ["PHE"]

def get_fund(code):
    url = "https://www.tefas.gov.tr/api/DB/BindComparisonFundReturns"

    payload = {
        "fontip": "YAT",
        "sfontur": "",
        "fonkod": code,
        "bastarih": "",
        "bittarih": ""
    }

    r = requests.post(url, json=payload)

    # DEBUG (çok önemli)
    print(r.text[:300])

    data = r.json()

    if not data.get("data"):
        return {
            "code": code,
            "price": None,
            "change": None
        }

    row = data["data"][0]

    return {
        "code": code,
        "price": row.get("FONFIYAT"),
        "change": row.get("GUNLUKGETIRI")
    }

result = [get_fund(f) for f in FUNDS]

with open("funds.json", "w") as f:
    json.dump(result, f, indent=2)
