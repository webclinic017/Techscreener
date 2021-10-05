import io
from backtesting import Backtest
import backtesting as bt
from .company_data import Strategies
from .data_pipeline import pipeline_intraday
import matplotlib.pyplot as plt
import matplotlib as mpl

# if you pass the column and the dataset it will give you the data of that column in the list format
def dataFormatting(column,data):
  columnList = []
  if data.index.name == column:
    date_time = data.index.strftime("%b %d %Y %-I:%M %p")
    dateTimeList = date_time.tolist()
    columnList= dateTimeList
  else:
    columnPriceList = data['Close'].tolist()
    columnList = columnPriceList
  return columnList

    


def company_ranking(companies):
    return_percentage = {}
    companyCloseList = {}
    DateDict = {}
    for x in companies:
        company = x
        df = pipeline_intraday(x)
        companyList = dataFormatting('CLose',df)
        DateList = dataFormatting('date',df)
        companyCloseList[f'{company}'] = companyList
        DateDict[f'{company}'] = DateList
        for keys in Strategies:
            bt = Backtest(df, Strategies[keys], cash=100000, commission=0.002)
            company_strategy = bt.run()
            return_percentage[f"{company}_{keys}"] = company_strategy
    return_array = sorted(
        return_percentage.items(), key=lambda x: x[1][6], reverse=True
    )
    return return_array,companyCloseList,DateDict


def strategy_backtest(company, strategy):
    x = pipeline_intraday(company)
    ClosePriceList = dataFormatting('CLose',x)
    DateList = dataFormatting('date',x)
    bt = Backtest(x, Strategies[strategy], cash=100000, commission=0.002)
    company_stats = bt.run()
    return company_stats,ClosePriceList,DateList
