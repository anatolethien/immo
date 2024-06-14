from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('../data/dvf.csv')

# Convert 'date_mutation' to datetime
df['date_mutation'] = pd.to_datetime(df['date_mutation'])

# Initialize the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div(children=[
    html.H1(children='Analyse des Transactions Immobilières'),

    dcc.Graph(
        id='transaction-count-over-time',
        figure=px.line(df.groupby('date_mutation').size().reset_index(name='count'), x='date_mutation', y='count', title='Nombre de Transactions au Fil du Temps')
    ),

    dcc.Graph(
        id='transaction-count-by-commune',
        figure=px.bar(df['nom_commune'].value_counts().reset_index(), x='nom_commune', y='count', title='Nombre de Transactions par Commune')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
