import dash

from dash import dcc, html, Input, Output

import dash.exceptions

import pandas as pd

import datetime

import plotly.graph_objs as go


# Read historical data

historical_data = pd.read_csv('historical_data.csv', names=['Timestamp', 'Price'])


app = dash.Dash(__name__)


def generate_daily_report(df):
  
  
daily_volatility = df['Price'].std()

max_price = df['Price'].max()

min_price = df['Price'].min()

 # Replace this function with your logic to generate the daily report

return html.Div([

html.P(f"Today's open price: {df['Price'].iloc[0]}"),

html.P(f"Today's close price: {df['Price'].iloc[-1]}"),

html.P(f"Today's volatility: {daily_volatility}"),

html.P(f"Today's maximum price: {max_price}"),

html.P(f"Today's minimum price: {min_price}")

])

app.layout = html.Div([

html.H1("EUR/USD Price"),

html.H2("Daily Report"),

html.Div(id='daily-report', children=generate_daily_report(historical_data)),


dcc.Graph(id="live-graph", animate=True),


dcc.Interval(

id='interval-component',

interval=1 * 1000,  # in milliseconds (1 second)

n_intervals=0

),
  
  
dcc.Interval(

id='interval-component-daily',

interval=60 * 1000,  # in milliseconds (1 minute)

n_intervals=0

)
 
  )]

@app.callback(

dash.dependencies.Output('price', 'children'),

dash.dependencies.Input('interval-component', 'n_intervals'))
  
def update_price(n):

with open('price.txt', 'r') as f:

price = f.read().strip()

return f"Current Price: {price}"


@app.callback(

dash.dependencies.Output('live-graph', 'figure'),

dash.dependencies.Input('interval-component', 'n_intervals'))

def update_graph(n):

df = pd.read_csv('historical_data.csv', names=['Timestamp', 'Price'])

fig = go.Figure(data=[go.Scatter(x=df['Timestamp'], y=df['Price'], mode='lines', name='EUR/USD')])

  
return fig


@app.callback(

Output('daily-report', 'children'),

Input('interval-component-daily', 'n_intervals')

)

def update_daily_report(n):

now = datetime.datetime.now()

if now.hour >= 20:

df = pd.read_csv('historical_data.csv', names=['Timestamp', 'Price'])

  
return generate_daily_report(df)

else:

raise dash.exceptions.PreventUpdate


if __name__ == '__main__':

app.run_server(debug=False, host='0.0.0.0', port=8052)


  
  
  
  

 
