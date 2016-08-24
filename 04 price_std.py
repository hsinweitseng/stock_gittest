# coding: utf-8
# testd on github on Mac
# introduce additonal 30 days STD
# Test with iAwriter with Textwrangler
# It is good with working no problem at all between iAwriter and Textwrangler. 08/18/16


import time
import datetime
import numpy as np
import matplotlib.pyplot as plt     # to resolve the problem. install Python(x,y) form google. Sometimes need to reboot
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick
import datetime

eachStock = 'AAPL','GOOG','MSFT','CMG','AMZN','EBAY','TSLA','T','MU','NUGT','WDC'

barrier = 40


def movingaverage(values,window):
	weights = np.repeat(1.0, window)/window
	smas = np.convolve(values,weights,'valid') 
	return smas
	

def stockList():
	allStockList = np.loadtxt(stockListFile.csv,delimiter=',')
	return allStockList

def graphData(stock,MA1,MA2):
	try:
		
		stockFile = stock+'.txt'
		date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',',unpack=True,
															  converters={ 0: mdates.strpdate2num('%Y%m%d')})

		x = 0
		y = len(date)
		candleAr = []
		while x < y:
			appendLine = date[x],openp[x],closep[x],highp[x],lowp[x],volume[x]
			candleAr.append(appendLine)
			x+=1

		Av1 = movingaverage(closep,MA1)
		Av2 = movingaverage(closep,MA2)

		SP = len(date[MA2-1:])
		
		fig = plt.figure()
		ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4)
		candlestick(ax1,candleAr,width=1, colorup='g',colordown='r')

		ax1.plot(date[-SP:],Av1[-SP:])
		ax1.plot(date[-SP:],Av2[-SP:])
	

		plt.ylabel('Stock Price')
		ax1.grid(True)

		ax2 = plt.subplot2grid((5,4),(4,0),sharex=ax1, rowspan=1, colspan=4)
		ax2.bar(date,volume)
		ax2.axes.yaxis.set_ticklabels([])
		ax2.grid(True)
		plt.ylabel('Volume')
		ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
		ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

		ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
		ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

		for label in ax1.xaxis.get_ticklabels():
			label.set_rotation(90)

		for label in ax2.xaxis.get_ticklabels():
			label.set_rotation(45)

		plt.subplots_adjust(left=.10,bottom=.19,right=.93,top=.95)
		
		title_plot=stock+'stock price'+char(deviation(stock))
		print(title_plot)
		
		plt.suptitle(stock+'Stock Price')

		plt.setp(ax1.get_xticklabels(), visible=False)

		plt.subplots_adjust(hspace=0)

		print datetime.datetime.now()
		
		plt.show()
		
		fig.savefig(stock+'.png')
		

	except Exception, e:
		print 'failed main loop', str(e)

def deviation(stock):
	stockFile = stock+'.txt'
	date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',',unpack=True,converters={ 0: mdates.strpdate2num('%Y%m%d')})  
		#calculate deviation
	deviation_ave = np.average(closep)
	std = np.std(closep)
	final_std = 100*std/deviation_ave
	deviation_delta = closep - deviation_ave
	deviation_delta_sqrt = np.sqrt((deviation_delta-deviation_ave)*(deviation_delta-deviation_ave))
		
	Final_std = 100*(deviation_delta_sqrt-deviation_ave)/deviation_ave
		
	return final_std
		
		
def stock_ave(stock):
	stockFile = stock+'.txt'
	date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile, delimiter=',',unpack=True,converters={ 0: mdates.strpdate2num('%Y%m%d')})
		
	#calculate deviation
	deviation_ave = np.average(closep)
	std = np.std(closep)
	return deviation_ave

def stockFilter(deviationLimit):
	for stock in eachStock:
		if deviation(stock)>deviationLimit:
			print('high deviation stock = '+stock)
			
		else:
			print('low deviation stock = '+stock)


#for stock in eachStock:
#    graphData(stock,12,26)
#    print stock
#    time.sleep(5)
print('---------------')
stockFilter(barrier)
