import pandas as pd
import ast
import streamlit as st

def load_csv(file_path):
    
    return pd.read_csv(file_path)

# Função para extrair o ID de 'createdby' e garantir que ele seja numérico
def preprocess_contacts(contacts_df, users_df):
    contacts_df['createdby'] = contacts_df['createdby'].str.extract(r'"id":\s*(\d+)')
    contacts_df['createdby'] = pd.to_numeric(contacts_df['createdby'], errors='coerce')
    return contacts_df , users_df

# Função para realizar o merge entre Contacts e users
def merge_contacts_with_users(contacts_df, users_df):
    return pd.merge(contacts_df[['createdby']], users_df[['id', 'name']], left_on='createdby', right_on='id', how='left')

# Função para agrupar e contar os Contacts por usuário e status
def group_and_count_contacts(merged_df):
    return merged_df.groupby(['createdby']).size().reset_index(name='count')

def process_contacts_and_users(contacts_df, users_df):
    # Carregar os arquivos
    contacts_df = load_csv(file_path='../data/csv/moskit_contacts.csv')
    users_df = load_csv(file_path='../data/csv/moskit_users.csv')

    # Extrair o ID de 'createdby' e garantir que ele seja numérico
    contacts_df, users_df = preprocess_contacts(contacts_df, users_df)
    return contacts_df, users_df


