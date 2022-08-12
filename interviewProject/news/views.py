from django.shortcuts import render
import requests

# Create your views here.
def news(request):
    url=f'https://newsapi.org/v2/everything?q=tesla&from=2022-03-15&sortBy=publishedAt&apiKey=c44ccd05c93046a998834b8b915c3f05'
    req=requests.get(url).json()
    print(req)
    return render(request , 'news/news.html')
