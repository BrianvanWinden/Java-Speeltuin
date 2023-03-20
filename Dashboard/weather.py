import dash 
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly as pl 
import requests
import polars
import pandas as pd 

app = dash.Dash(__name__)

cats = ['temperature', 'relative_humidity']


def update_data ():
    weather_request = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.01&longitude=4.36&hourly=temperature_2m,relativehumidity_2m')
    json = weather_request.json()
    df = pd.DataFrame(json)
    # df2 = polars.DataFrame(json)
    return df#, df2




if __name__ == '__main__':
    print(cats)
    
    data, data2 = update_data()
    print(data)
    # print(data2)