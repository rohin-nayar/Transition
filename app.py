import pandas as pd
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px

# Load and prepare the data
df = pd.read_csv('Data/Records_csv.csv')

# Convert 'Date' from string to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Ensure 'Body Weight (kg)' is numeric and handle missing values
df['Body Weight (kg)'] = pd.to_numeric(df['Body Weight (kg)'], errors='coerce')
df['Body Weight (kg)'] = df['Body Weight (kg)'].ffill()  # Use direct method to forward fill

# Initialize the app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H3('My First App with Data and a Graph'),
    html.Hr(),
    dcc.RadioItems(
        options=[{'label': 'Body Weight (kg)', 'value': 'Body Weight (kg)'},
                 {'label': 'Duration (min)', 'value': 'Duration (min)'}],
        value='Body Weight (kg)',
        id='controls-and-radio-item'
    ),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(id='controls-and-graph')
])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.line(df, x="Date", y=col_chosen, title='Progression Over Time')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
