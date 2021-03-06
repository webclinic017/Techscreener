from .strategy_storage import *

stocks = {
    "Large-Cap Stocks": {
        "AAPL": "Apple",
    },
    "Medium-Cap Stocks": {
        "LAD": "Lithia Motors, Inc.",
    },
    "Small-Cap Stocks": {
        "PRLB" : 'ProtoLab Inc.',
    }
}

# crud
analysis_companies = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "TSLA": "Tesla",
    "GOOG": "Google",
    "NFLX": "Netflix",
    "GOOGL": "Alphabet Inc Class A",
    "AMZN": "Amazon",
    "FB": "Facebook",
    "BRK-B": "Berkshire Hathaway Inc. Class B",
    "BRK-A": "Berkshire Hathaway Inc. Class A",
    "TSM": "Taiwan Semiconductor Mfg. Co. Ltd.",
    "NVDA": "NVIDIA Corporation",
    "V": "Visa Inc",
    "JPM": "JPMorgan Chase and Co.",
    "BABA": "Alibaba Group Holding Ltd",
    "JNJ": "Johnson & Johnson",
    "WMT": "Walmart Inc",
    "UNH": "UnitedHealth Group Inc.",
    "BAC": "Bank of America Corp",
    "PG": "Procter & Gamble Co",
    "HD": "Home Depot Inc",
    "ASML": "ASML Holding NV",
    "MA": "Mastercard Inc",
    "PYPL": "PayPal Holdings",
    "DIS": "Walt Disney Co",
    "ADBE": "Adobe Inc",
    "TM": "Toyota Motor Corp",
    "CMCSA": "Comcast Corporation",
    "PFE": "Pfizer Inc.",
    "NKE": "Nike Inc",
    "CSCO": "Cisco Systems Inc",
    "LLY": "Eli Lily And Co",
    "NFLX": "Netflix Inc",
    "ORCL": "Oracle Corporation",
    "CRM": "salesforce.com, inc.",
    "ABBV": "Abbvie Inc",
    "LAD": "Lithia Motors, Inc.",
    "DOX": "Amdocs Limited",
    "DLB": "Dolby Laboratories",
    "PEN": "Penumbra, Inc.",
    "BAP": "Credicorp Ltd.",
    "BSAC": "Banco Santerder - Chile",
    "AIZ": "Assurant, Inc.",
    "UAA": "Under Armour, Inc.",
    "GRFS": "Grifols,SA",
    "FSLR": "First Solar, Inc.",
    "WAL": "Western Alliance Bancorporation",
    "VRT": "Vertiv Holding, LLC",
    "XPO": "XPO Logistics, Inc.",
    "STOR": "Store Capital Corporation",
    "LSI": "Life Storage, Inc.",
    "GWRE": "Guidewire Software, Inc",
    "CMA": "Comerica Incorporated",
    "TRGP": "Targa Resources",
    "NI": "NiSource Inc",
    "OC": "Owens Corning Inc",
    "GL": "Globe Life Inc.",
    "BAK": "Braskem SA",
    "CF": "CF Industries Holdings, Inc",
    "COLD": "American Realty Trust",
    "G": "Genpact Limited",
    "OLED": "Universal Display Corporation",
    "CREE": "Cree, Inc.",
    "UGI": "UGI Corp",
    "SMAR": "Smartshet Inc.",
    "SYNH": "Syneos Health, Inc",
    "HRC": "Hill-Rom Holdings Inc",
    "CONE": "CyrusOne Inc",
    "ZNGA": "Zynga Inc.",
    "UTHR": "United Therapeutics",
    "JNPR": "Juniper Networks",
}

# static
Strategies = {
    "SmaCross": SmaCross,
    "SmaxCrossSmay": SmaxCrossSmay,
    "SmaCrossthree": SmaCrossthree,
    "EMASMASMA": EMASMASMA,
    "EMAEMASMA": EMAEMASMA,
    "EMAEMAEMA": EMAEMAEMA,
    "EMASMARSI": EMASMARSI,
    "EMASMA-dual": EMASMA_dual
}

# static
outcome_variables = [
    "Return [%]",
    "Buy and Hold Return [%]",
    "Return (Ann.) [%]",
    "Volatility (Ann.) [%]",
    "Sharpe Ratio",
    "Sortino Ratio",
    "Calmar Ratio",
]

# semi static
strategy_description = {
    "EMASMARSI": {
        "buy condition": [
            "weekly RSI(30) ??? daily RSI(30) > 70",
            "Close > MA(10) > MA(20) > MA(50) > MA(100)",
        ],
        "sell condition": [
            "Daily close is more than 2 percent below MA(10)",
            "8 percent fixed stop loss is hit",
        ],
    },
    "SmaCross": {
        "buy condition": ["SMA 10 greater than closing price"],
        "sell condition": ["SMA 20 less than closing price"],
    },
    "SmaxCrossSmay": {
        "buy condition": ["SMA 10 greater than SMA 20,x<y"],
        "sell condition": ["SMA 10 is less than SMA 20"],
    },
    "SmaCrossthree": {
        "buy condition": [
            "SMA 10 is greater than the closing price",
            "SMA 20 is greater than the closing price",
            "SMA 30 is greater than the closing price",
        ],
        "sell condition": [
            "SMA 10 is less than the closing price",
            "SMA 20 is less than the closing price",
            "SMA 30 is less than the closing price",
        ],
    },
    "EMASMASMA": {
        "buy condition": [
            "EMA 15 is greater than the closing price",
            "SMA 20 is greater than the closing price",
            "SMA 30 is greater than the closing price",
        ],
        "sell condition": [
            "EMA 15 is greater than the closing price",
            "SMA 20 is greater than the closing price",
            "SMA 30 is greater than the closing price",
        ],
    },
    "EMAEMASMA": {
        "buy condition": [
            "EMA 5 is greater than the closing price",
            "EMA 10 is greater than the closing price",
            "SMA 30 is greater than the closing price",
        ],
        "sell condition": [
            "EMA 5 is less than the closing price",
            "EMA 10 is less than the closing price",
            "SMA 30 is less than the closing price",
        ],
    },
    "EMAEMAEMA": {
        "buy condition": [
            "EMA 5 is greater than the closing price",
            "EMA 10 is greater than the closing price",
            "EMA 30 is greater than the closing price",
        ],
        "sell condition": [
            "EMA 5 is less than the closing price",
            "EMA 10 is less than the closing price",
            "SMA 30 is less than the closing price",
        ],
    },
    "EMASMA-dual": {
        "buy condition": [
            "SMA 20 crosses above SMA 30",
            "SMA 30 crosses above the EMA 5",
            "SMA 40 crosses over the EMA 5",
            "SMA 20 crosses over the EMA 5",
        ],
        "sell condition": [
            "Closing price crosses over EMA 5",
            "Closing price crosses over SMA 30",
            "Closing price crosses over SMA 40 ",
        ],
    },
}
