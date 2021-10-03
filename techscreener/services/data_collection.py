from .strategy_backtesting import company_ranking
from .company_data import stocks
print('the file is getting executed')
largeCapReturns,LargeClosePriceList = company_ranking(stocks['Large-Cap Stocks'])
mediumCapReturns,MediumClosePriceList = company_ranking(stocks['Medium-Cap Stocks'])