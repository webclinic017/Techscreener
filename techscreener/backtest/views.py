from django.shortcuts import redirect, render
from rest_framework.views import APIView
import pandas as pd
import plotly
import plotly.express as px 
from services.data_collection import largeCapReturns, mediumCapReturns
from services.company_data import analysis_companies, Strategies,outcome_variables, stocks, strategy_description
from services.data_pipeline import pipeline_intraday
from ta import momentum
from ta import trend
from ta.volatility import BollingerBands
from ta.volume import MFIIndicator
from services.strategy_backtesting import company_ranking, strategy_backtest

# Create your views here.

class RankingView(APIView):
    def post(self, request):
        index = request.data['index']
        stocks = Stocks[index]
        if index == 'Large-Cap Stocks':
            return_array = largeCapReturns
        else:
            return_array = mediumCapReturns

        return render(request, "main/ranking.html", { 'return_array': return_array, 'outcome_variables': outcome_variables, 'strategy_description': strategy_description })

class VisualizationView(APIView):
    def post(self, request):
        company = request.data['company']
        data = pipeline_intraday(company)
        data['SMA10'] = trend.sma_indicator(close = data['Close'], window = 10, fillna = False)

        return render(request, "main/ranking.html", { 'return_array': return_array, 'outcome_variables': outcome_variables, 'strategy_description': strategy_description })

        # Bollinger Bands
        indicator_bb = BollingerBands(close=data["Close"], window=12, window_dev=2)
        data['BB_BBM'] = indicator_bb.bollinger_mavg() # middle band
        #data['BB_BBH'] = indicator_bb.bollinger_hband() # high band
        #data['BB_BBL'] = indicator_bb.bollinger_lband() # low band
        data['MACD'] = trend.macd(close=data["Close"], window_slow = 26, window_fast=12)

        # RSI
        data['RSI'] = momentum.rsi(close=data["Close"], window=12)

        # MFI
        indicator_mfi = MFIIndicator(high=data['High'],low=data['Low'],close=data['Close'],volume=data['Volume'],window=12,fillna=False)
        data['MFI'] = indicator_mfi.money_flow_index()
        closing_price = data.iloc[-1,-9]
        volume = data.iloc[-1,-8]
        df = data.iloc[-11:-1,-5:-1]
        fig = px.line(data, x = data.index, y = ["Close","SMA10"])
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return render(request, "main/visualization.html", { 'closing_price': closing_price, 'volume': volume, 'company': company, 'tables': [df.to_html()], 'titles': ['SMA','BB_BBM','BB_BBH','BB_BBL','MACD','RSI','MFI'], 'graphJSON': graphJSON })

class StrategyView(APIView):
    def post(self, request):
        company = request.data['company']
        strategy = request.data['strategy']
        company_statistics = strategy_backtest(company,strategy)
        
        return render(request, "main/strategy.html", { 
            'company': company, 'strategy': strategy, 'company_statistics': company_statistics, 'strategy_description': strategy_description, 'outcome_variables': outcome_variables
         })