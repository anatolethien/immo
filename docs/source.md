# Dataset Documentation

## Overview

This document provides a detailed description of the dataset, including the number of records, columns, and their data types. The dataset contains information about [dataset's purpose].

## Data Dictionary

| Column Name    | Data Type   | Description                                                                   |
|----------------|-------------|-------------------------------------------------------------------------------|
| id_mutation    | String      | Année de la transaction - id de la transaction                                |
| date_mutation  | Date      | Date de la transaction                                                     |
| numero_disposition       | Int      | The category of the data point                                                |
| nature_mutation          | String       | type de vente : vente de bien ou bien immo à construire ou en cours de contruction                            |
| valeur_fonciere    | Float      | Valeur immobiliaire du bien                              |
| adresse_numero    | Float      | Numéro de la rue                              |
| adresse_suffixe    | Sring      | si le numéro de la rue est un Bis ou pas                              |
| adresse_nom_voie    | Int      |                               |
| code_postal    | Int      | code postal                              |
| code_commune    | Int      | code commune                              |
| nom_commune    | String      | nom de la ville / village                             |
| code_departement    | Int      | numéro du département                              |
| ancien_nom_commune    | String      | ancien code commune                              |
| ancien_code_commune    | Int      | ancien code commune                              |
| ancien_nom_commune    | Int      | ancien code commune                              |
| ancien_code_commune    | Int      | ancien code commune                              |
| ancien_code_commune    | Int      | ancien code commune                              |
| ancien_code_commune    | Int      | ancien code commune                              |
| ancien_code_commune    | Int      | ancien code commune                              |
| ancien_code_commune    | Int      | ancien code commune                              |

## Data Quality

The dataset has been cleaned and verified for accuracy. However, it is always recommended to perform additional data validation and cleaning steps before using the data for analysis.

## Usage

This dataset can be used for various purposes, including:

- Exploratory data analysis
- Predictive modeling
- Time series analysis
- Hypothesis testing

## Limitations

- The dataset does not include any missing values. If missing values were present, they would have been handled appropriately during data cleaning.
- The dataset is not balanced with respect to the categories. Some categories may have more records than others.

## References

- [Dataset Source]
- [Additional References]
