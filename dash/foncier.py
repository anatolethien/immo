from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('../data/dvf.csv')

# Convert 'valeur_fonciere' and 'surface_reelle_bati' to float
df['valeur_fonciere'] = pd.to_numeric(df['valeur_fonciere'], errors='coerce')
df['surface_reelle_bati'] = pd.to_numeric(df['surface_reelle_bati'], errors='coerce')

# Filter the data to include transactions for Toulouse and exclude transactions for Toulouse
df_toulouse = df[df['nom_commune'] == 'TOULOUSE']
df_no_toulouse = df[df['nom_commune'] != 'TOULOUSE']

# Calculate the IQR for 'valeur_fonciere' for Toulouse and excluding Toulouse
Q1_toulouse = df_toulouse['valeur_fonciere'].quantile(0.25)
Q3_toulouse = df_toulouse['valeur_fonciere'].quantile(0.75)
IQR_toulouse = Q3_toulouse - Q1_toulouse

Q1_no_toulouse = df_no_toulouse['valeur_fonciere'].quantile(0.25)
Q3_no_toulouse = df_no_toulouse['valeur_fonciere'].quantile(0.75)
IQR_no_toulouse = Q3_no_toulouse - Q1_no_toulouse

# Filter out outliers based on 'valeur_fonciere' for Toulouse and excluding Toulouse
df_toulouse_filtered = df_toulouse[(df_toulouse['valeur_fonciere'] >= Q1_toulouse - 1.5 * IQR_toulouse) & (df_toulouse['valeur_fonciere'] <= Q3_toulouse + 1.5 * IQR_toulouse)]
df_no_toulouse_filtered = df_no_toulouse[(df_no_toulouse['valeur_fonciere'] >= Q1_no_toulouse - 1.5 * IQR_no_toulouse) & (df_no_toulouse['valeur_fonciere'] <= Q3_no_toulouse + 1.5 * IQR_no_toulouse)]

# Initialize the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div(children=[
    html.H1(children='Analyse de la Valeur Foncière des Transactions Immobilières'),

    dcc.Graph(
        id='estimated-value-vs-size-all',
        figure=px.scatter(df, x='surface_reelle_bati', y='valeur_fonciere', title='Valeur Foncière vs. Taille du Bâtiment (Toutes les Transactions)')
    ),

    dcc.Graph(
        id='estimated-value-vs-size-toulouse',
        figure=px.scatter(df_toulouse_filtered, x='surface_reelle_bati', y='valeur_fonciere', title='Valeur Foncière vs. Taille du Bâtiment à Toulouse (Sans Valeurs Aberrantes)')
    ),

    dcc.Graph(
        id='estimated-value-vs-size-no-toulouse',
        figure=px.scatter(df_no_toulouse_filtered, x='surface_reelle_bati', y='valeur_fonciere', title='Valeur Foncière vs. Taille du Bâtiment Hors Toulouse (Sans Valeurs Aberrantes)')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
