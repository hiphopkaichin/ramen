from django.shortcuts import render
import requests   # Web からデータを取ってくる時に使う
import bs4        # スクレイピング
import re

# Create your views here.
def appmain(request):
    while True:
        res = requests.get('https://tabelog.com/ramen/tokyo/rank/')
