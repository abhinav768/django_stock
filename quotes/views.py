from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://finnhub.io/api/v1/quote?symbol=" + ticker + "&token=cqp2vd1r01qthdu8phngcqp2vd1r01qthdu8pho0")
        api_request_full = requests.get("https://finnhub.io/api/v1/stock/profile2?symbol=" + ticker + "&token=cqp2vd1r01qthdu8phngcqp2vd1r01qthdu8pho0")
        try:
            api = json.loads(api_request.content)
            api1 = json.loads(api_request_full.content)
        except Exception as e:
            api = "Error..."
            api1 = "Error..."
        return render(request, 'home.html', {'api': api, 'api1': api1})
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})


def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        output = []
        output1 = []
        output2 = []
        for ticker_item in ticker:
            api_request = requests.get("https://finnhub.io/api/v1/quote?symbol=" + str(ticker_item) + "&token=cqp2vd1r01qthdu8phngcqp2vd1r01qthdu8pho0")
            api_request_full = requests.get("https://finnhub.io/api/v1/stock/profile2?symbol=" + str(ticker_item) + "&token=cqp2vd1r01qthdu8phngcqp2vd1r01qthdu8pho0")
            try:
                api = json.loads(api_request.content)
                api1 = json.loads(api_request_full.content)
                api.update(api1)
                # output1.append(api)
                # output2.append(api1)
                output.append(api)
            except Exception as e:
                api = "Error..."
                api1 = "Error..."
            
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted!"))
    return redirect(delete_stock)


def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})
    

    # cqp2vd1r01qthdu8phngcqp2vd1r01qthdu8pho0