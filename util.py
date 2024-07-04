import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

types = {
    'id_mutation': 'object',
    'date_mutation': 'object',
    'numero_disposition': 'object',
    'nature_mutation': 'object',
    'valeur_fonciere': 'float',
    'adresse_numero': 'object',
    'adresse_suffixe': 'object',
    'adresse_nom_voie': 'object',
    'adresse_code_voie': 'object',
    'code_postal': 'object',
    'code_commune': 'object',
    'nom_commune': 'object',
    'code_departement': 'object',
    'ancien_code_commune': 'object',
    'ancien_nom_commune': 'object',
    'id_parcelle': 'object',
    'ancien_id_parcelle': 'object',
    'numero_volume': 'object',
    'lot1_numero': 'object',
    'lot1_surface_carrez': 'object',
    'lot2_numero': 'object',
    'lot2_surface_carrez': 'object',
    'lot3_numero': 'object',
    'lot3_surface_carrez': 'object',
    'lot4_numero': 'object',
    'lot4_surface_carrez': 'object',
    'lot5_numero': 'object',
    'lot5_surface_carrez': 'object',
    'nombre_lots': 'int',
    'code_type_local': 'object',
    'type_local': 'object',
    'surface_reelle_bati': 'object',
    'nombre_pieces_principales': 'object',
    'code_nature_culture': 'object',
    'nature_culture': 'object',
    'code_nature_culture_speciale': 'object',
    'nature_culture_speciale': 'object',
    'surface_terrain': 'float',
    'longitude': 'float',
    'latitude': 'float',
    'section_prefixe': 'object'
}

def load_df(file_path):
    df = pd.read_csv(
        filepath_or_buffer=file_path,
        sep=',',
        decimal='.',
        dtype=types
    )
    df['date_mutation'] = pd.to_datetime(df['date_mutation'])
    df.drop_duplicates(
        subset='id_mutation',
        inplace=True
    )
    return df

if __name__ == '__main__':
    df = load_df('data/dvf.csv')
    print(df.shape)
