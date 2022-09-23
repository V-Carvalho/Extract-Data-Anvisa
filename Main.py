import numpy as np
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

firebase_credentials = credentials.Certificate('firebase_credentials.json')
firebase_admin.initialize_app(firebase_credentials)
db = firestore.client()


def extract_data():
    # Extraindo oa dados da planiha
    table = pd.read_excel('production_preco_remedios_2022_08_12.xlsx', engine='openpyxl')
    df = pd.DataFrame(
        table,
        columns=[
            'SUBSTANCIA',
            'LABORATORIO',
            'EAN 1',
            'NOME PRODUTO',
            'CLASSE TERAPEUTICA',
            'COMPOSICAO',
            'PMC 0%',
            'PMC 20%',
            'TARJA',
        ]
    )

    # Percorrendo os dados e inserindo em um array
    medicines = []
    for i in range(len(df)):
        medicines.append(
            {
                'id': i + 1,
                'substance': np.unicode_(df.loc[i, 'SUBSTANCIA']),
                'laboratory': np.unicode_(df.loc[i, 'LABORATORIO']),
                'ean': np.unicode_(df.loc[i, "EAN 1"]),
                'productName': np.unicode_(df.loc[i, 'NOME PRODUTO']),
                'therapeuticClass': np.unicode_(df.loc[i, 'CLASSE TERAPEUTICA']),
                'composition': np.unicode_(df.loc[i, 'COMPOSICAO']),
                'pmcLow': np.unicode_(df.loc[i, 'PMC 0%']),
                'pmcHigh': np.unicode_(df.loc[i, 'PMC 20%']),
                'tarja': np.unicode_(df.loc[i, 'TARJA']),
            }
        )
    # Chamando função que inseri os dados no banco
    insert_data_firebase(medicines)


def insert_data_firebase(medicines):
    for medicine in medicines:
        # if medicine['id'] < 19000:
        if medicine['id'] >= 19000:  # parou no 18999
            db.collection('remedios-anvisa').document().set({
                'id': int(medicine['id']),
                'substance': medicine['substance'],
                'laboratory': medicine['laboratory'],
                'ean': medicine['ean'],
                'productName': medicine['productName'],
                'therapeuticClass': medicine['therapeuticClass'],
                'composition': medicine['composition'],
                'pmcLow': medicine['pmcLow'],
                'pmcHigh': medicine['pmcHigh'],
                'tarja': medicine['tarja'],
            })
            print(medicine['id'])


if __name__ == '__main__':
    extract_data()
