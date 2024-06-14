from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('../data/dvf.csv')

# Convert 'date_mutation' to datetime and 'valeur_fonciere' to float
df['date_mutation'] = pd.to_datetime(df['date_mutation'])
df['valeur_fonciere'] = pd.to_numeric(df['valeur_fonciere'], errors='coerce')

# Initialize the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div(children=[
    html.H1(children='Analyse de la Valeur Foncière des Transactions Immobilières'),

    dcc.Graph(
        id='estimated-value-over-time',
        figure=px.line(df.groupby('date_mutation')['valeur_fonciere'].mean().reset_index(), x='date_mutation', y='valeur_fonciere', title='Valeur Foncière Moyenne au Fil du Temps')
    ),

    dcc.Graph(
        id='estimated-value-by-commune',
        figure=px.bar(df.groupby('nom_commune')['valeur_fonciere'].mean().reset_index(), x='nom_commune', y='valeur_fonciere', title='Valeur Foncière Moyenne par Commune')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
