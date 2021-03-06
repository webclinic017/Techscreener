from django.shortcuts import redirect, render
from django import template
from django.http import JsonResponse
from requests.api import request
from requests.models import Response
register=template.Library()
from rest_framework.views import APIView
import pandas as pd
import json
import ast
#import plotly
#import plotly.express as px 
from services.data_collection import largeCapReturns, mediumCapReturns,LargeClosePriceList,LargeDateList,MediumDateList,MediumClosePriceList,smallCapReturns,smallClosePriceList,smallDateList
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
            DateList = LargeDateList
        elif index == 'Medium-Cap Stocks':
            return_array = mediumCapReturns
            closePriceList =  MediumClosePriceList
            DateList = MediumDateList
        else:
            return_array = smallCapReturns
            closePriceList = smallClosePriceList
            DateList = smallDateList

        return render(request, "main/ranking.html", { 'return_array': return_array, 'outcome_variables': outcome_variables, 'strategy_description': strategy_description, 'close': closePriceList, 'date': DateList })
    
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
        closing_price = data.iloc[-1,-9]
        ClosePriceList = data['Close'].tolist()
        volume = data.iloc[-1,-8]
        df = data.iloc[-11:-1,-5:-1]
        DateList = dataFormatting('date',data)
        #fig = px.line(data, x = data.index, y = ["Close","SMA10"])
        #graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return render(request, "main/visualization.html", { 'DateList':DateList,'ClosePriceList':ClosePriceList,'closing_price': closing_price, 'volume': volume, 'company': company, 'tables': [df.to_html()], 'titles': ['SMA','BB_BBM','BB_BBH','BB_BBL','MACD','RSI']})

class GraphView(APIView):
    def post(self, request):
        close_price = request.data['ClosePriceList']
        close_price = ast.literal_eval(close_price)
        ind = [0,1,2,3,4,5,6,7,8,9]
        close_price = pd.Series(close_price[:10],index=ind)
        indicator = request.data['indicator']
        value = request.data['value']
        value = int(value)
        if indicator == 'SMA':
            indicator_data = trend.sma_indicator(close = close_price, window = value, fillna = True)
        elif indicator == 'EMA':
            indicator_data = trend.ema_indicator(close= close_price ,window =value, fillna = True)
        else:
            indicator_data = momentum.rsi(close= close_price, window=12)

        indicator_data = indicator_data[:50]
        indicator_data = [int(x) for x in indicator_data]
        data = ','.join(map(str, indicator_data))

        return JsonResponse({ 'data': data }, safe=True)

class StrategyView(APIView):
    def post(self, request):
        if not hasattr(request, 'username'):
            response = redirect('/login?message=Login to view the page')
            return response
        company = request.data['company']
        strategy = request.data['strategy']
        # The ClosePriceList is a python list that has all the all the close prices in the list format.
        company_statistics,ClosePriceList,DateList = strategy_backtest(company,strategy)

        
        return render(request, "main/strategy.html", { 
            'company': company, 'strategy': strategy, 'company_statistics': company_statistics, 'strategy_description': strategy_description, 'outcome_variables': outcome_variables, 'close': ClosePriceList, 'date': DateList
         })