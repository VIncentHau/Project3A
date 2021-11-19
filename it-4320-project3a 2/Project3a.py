
from datetime import datetime
import requests
import pygal
import json

print('Stock Data Visualizer')
print('-------------------------')

def askCharts():
    print('\nChart Types:')
    print('------------------')
    print('1. Bar')
    print('2. Line') 

    while(True):
        try:
            chartType = int(input('\nEnter the chart type you want(1, 2): '))
            if chartType == 1:
                print('chartType == 1:')
            elif chartType == 2:
                print('chartType == 2:')
            elif chartType not in range(1,3): 
                print("ERROR: Invalid Option! Select 1 or 2")
                continue
        except ValueError: 
            print("ERROR: Invalid Option! Select 1 or 2")
            continue
        else:
            break
    return chartType
    

def askTimeSeries(stockSymbol):
    stock = stockSymbol
    print('\nSelect the Time Series of the chart you want to generate:')
    print('----------------------------------------------------------------')
    print('1. Intraday')
    print('2. Daily')
    print('3. Weekly')
    print('4. Monthly')
    
    while(True):
        try:
            timeSeries = int(input('\nEnter  time series option (1, 2, 3, 4): '))
            apiKey = 'YY5C93IGQ19VMJXQ'
            if timeSeries == 1:
                #intraday
                url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + stock + '&interval=60min&apikey=' + apiKey
            elif timeSeries == 2:
                #daily
                url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock + '&apikey=' + apiKey
            elif timeSeries == 3:
                #weekly
                url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + stock + '&apikey=' + apiKey
            elif timeSeries == 4:
                #monthly
                url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + stock + '&apikey=' + apiKey
            elif timeSeries not in range(1,5): 
                print("ERROR: Invalid Option! Select 1 or 2 or 3 or 4")
                continue
        except ValueError: 
            print("ERROR: Invalid Option! Select 1 or 2 or 3 or 4")
            continue
        else:
            break
    r = requests.get(url)
    data = r.json()
    return data, timeSeries
    



def checkDates():
    format = "%Y-%m-%d"
    while(True):
        try:
            startDate = input('\nEnter the start date (format: YYYY-MM-DD): ')
            endDate = input('\nEnter the end date (format: YYYY-MM-DD): ')
            datetime.strptime(startDate, format)
            datetime.strptime(endDate, format)
            if endDate < startDate:
                print("End date must be after start date")
                continue
            break
        except ValueError as e:
            print("Incorrect start date format, should be YYYY-MM-DD")
            continue
        else:
            break
    return startDate, endDate

#7. Generate a graph and open in the user’s default browser.
def generateGraph(stockSymbol, chartType, timeSeries, data, startDate, endDate):
    
    format2 = "%Y-%m-%d %H:%M:%S"
    format = "%Y-%m-%d"
    high = []
    low =[]
    close =[]
    open = []
    dateList = []
    stock = stockSymbol
    chart = chartType
    timeS = timeSeries
    sd = startDate
    ed = endDate
    datetime.strptime(sd, format)
    datetime.strptime(ed, format)
    dataList = data
    

    
    if timeS == 1:
        for date in dataList['Time Series (60min)']:
            datetime.strptime(date, format2)
            if date > ed:
                continue 
            if date <= sd:
                break
            dateList.append(date)
            open.append(dataList['Time Series (60min)'][date]['1. open'])
            high.append(dataList['Time Series (60min)'][date]['2. high'])
            low.append(dataList['Time Series (60min)'][date]['3. low'])
            close.append(dataList['Time Series (60min)'][date]['4. close'])

    if timeS == 2:
        for date in dataList['Time Series (Daily)']:
            datetime.strptime(date, format)
            if date > ed:
                continue 
            if date <= sd:
                break
            dateList.append(date)
            open.append(dataList['Time Series (Daily)'][date]['1. open'])
            high.append(dataList['Time Series (Daily)'][date]['2. high'])
            low.append(dataList['Time Series (Daily)'][date]['3. low'])
            close.append(dataList['Time Series (Daily)'][date]['4. close'])

    if timeS == 3:
        for date in dataList['Weekly Time Series']:
            datetime.strptime(date, format)
            if date > ed:
                continue 
            if date <= sd:
                break
            dateList.append(date)
            open.append(dataList['Weekly Time Series'][date]['1. open'])
            high.append(dataList['Weekly Time Series'][date]['2. high'])
            low.append(dataList['Weekly Time Series'][date]['3. low'])
            close.append(dataList['Weekly Time Series'][date]['4. close'])
            
    if timeS == 4:
        for date in dataList['Monthly Time Series']:
            datetime.strptime(date, format)
            if date > ed:
                continue 
            if date <= sd:
                break
            dateList.append(date)
            open.append(dataList['Monthly Time Series'][date]['1. open'])
            high.append(dataList['Monthly Time Series'][date]['2. high'])
            low.append(dataList['Monthly Time Series'][date]['3. low'])
            close.append(dataList['Monthly Time Series'][date]['4. close'])

    openFloat = [float(item) for item in open]
    highFloat = [float(item) for item in high]
    lowFloat = [float(item) for item in low]
    closeFloat = [float(item) for item in close]

    if chart == 1:
        bar = pygal.Bar(x_label_rotation=90)
        bar.title = stock
        bar.x_labels = map(str, dateList)
        bar.add('Open', openFloat)
        bar.add('High', highFloat)
        bar.add('Low', lowFloat)
        bar.add('Close', closeFloat)
        bar.render_in_browser()

    if chart == 2:
        line = pygal.Line(x_label_rotation=90)
        line.title = stock
        line.x_labels = map(str, dateList)
        line.add('Open', openFloat)
        line.add('High', highFloat)
        line.add('Low', lowFloat)
        line.add('Close', closeFloat)
        line.render_in_browser()

    
    


def main():
    repeat = True
    while(repeat):
        while(True):
            try:
                stockSymbol = input('\nEnter stock symbol: ')
                chartType = askCharts()
                data, timeSeries = askTimeSeries(stockSymbol)
                startDate, endDate = checkDates()
                generateGraph(stockSymbol, chartType, timeSeries, data, startDate, endDate)
            except ValueError:
                print("ERROR: Invalid Option!")
                continue
            else:
                 break
        more_stocks = input("Would you like to view more stock data? (y/n): ")
        if (more_stocks != "y"):
            repeat = False
        
main()