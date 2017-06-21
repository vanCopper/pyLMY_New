#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2017/6/21'
import urllib3
import json
def getNowWeather():
    url_weather = 'https://api.seniverse.com/v3/weather/now.json?key=t53ihxakgsjlolg3&location=shanghai&language=zh-Hans&unit=c'
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    r = http.request('GET', url_weather)
    context = r.data
    weather_json = json.loads(context, encoding='utf-8')
    weather = weather_json["results"][0]["now"]
    print(weather)
    return weather

def getDaysWeather():
    url_weather = 'https://api.seniverse.com/v3/weather/daily.json?key=t53ihxakgsjlolg3&location=shanghai&language=zh-Hans&unit=c&start=0&days=3'
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    r = http.request('GET', url_weather)
    context = r.data
    weather_json = json.loads(context, encoding='utf-8')
    daily_forecast = weather_json['results'][0]['daily']
    print(daily_forecast)
    return daily_forecast
