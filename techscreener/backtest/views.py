from django.shortcuts import redirect, render
from django import template
register=template.Library()
from rest_framework.views import APIView
import pandas as pd
import json
#import plotly
#import plotly.express as px 
from services.data_collection import largeCapReturns, mediumCapReturns,LargeClosePriceList,MediumClosePriceList
from services.company_data import analysis_companies, Strategies,outcome_variables, stocks, strategy_description
from services.data_pipeline import pipeline_intraday
from ta import momentum
from ta import trend
from ta.volatility import BollingerBands
from ta.volume import MFIIndicator
from services.strategy_backtesting import dataFormatting, strategy_backtest


# Create your views here.

class RankingView(APIView):
    def post(self, request):
        if not hasattr(request, 'username'):
            response = redirect('/login?message=Login to view the page')
            return response
        index = request.data['index']
        # The closePriceList is a dictionary that has all the all the close prices in the list format
        # The prices can be accessed like this 
        # list = companyCloseList['<company ticker>']
        if index == 'Large-Cap Stocks':
            return_array = largeCapReturns
            closePriceList = LargeClosePriceList
        else:
            return_array = mediumCapReturns
            closePriceList =  MediumClosePriceList
        
        return render(request, "main/ranking.html", { 'return_array': return_array, 'outcome_variables': outcome_variables, 'strategy_description': strategy_description })
    
    @register.filter(name='split')
    def split(value):
        """
            Returns the value turned into a list.
        """
        dic = value.split('_')
        return dic

    def get_value(dic,i):
        """
            Returns the value turned into a list.
        """
        return dic[i]
    
    register.filter(get_value)

class VisualizationView(APIView):
    def post(self, request):
        if not hasattr(request, 'username'):
            response = redirect('/login?message=Login to view the page')
            return response
        company = request.data['company']
        data = pipeline_intraday(company)
        data['SMA10'] = trend.sma_indicator(close = data['Close'], window = 10, fillna = False)

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
        #fig = px.line(data, x = data.index, y = ["Close","SMA10"])
        #graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return render(request, "main/visualization.html", { 'closing_price': closing_price, 'volume': volume, 'company': company, 'tables': [df.to_html()], 'titles': ['SMA','BB_BBM','BB_BBH','BB_BBL','MACD','RSI','MFI']})

class StrategyView(APIView):
    def post(self, request):
        if not hasattr(request, 'username'):
            response = redirect('/login?message=Login to view the page')
            return response
        company = request.data['company']
        strategy = request.data['strategy']
        # The company Close list is a python list that has all the all the close prices in the list format
        company_statistics,companyList = strategy_backtest(company,strategy)
        
        return render(request, "main/strategy.html", { 
            'company': company, 'strategy': strategy, 'company_statistics': company_statistics, 'strategy_description': strategy_description, 'outcome_variables': outcome_variables
         })