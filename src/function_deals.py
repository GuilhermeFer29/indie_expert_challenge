import pandas as pd

# Função para carregar os arquivos CSV
def load_data(deals_path, users_path, contacts_path):
    deals_df = pd.read_csv(deals_path)
    users_df = pd.read_csv(users_path)
    contacts_df = pd.read_csv(contacts_path)
    return deals_df, users_df ,contacts_df

# Função para extrair o ID de 'createdby' e garantir que ele seja numérico
def preprocess_deals(deals_df):
    deals_df['createdby'] = deals_df['createdby'].str.extract(r'"id":\s*(\d+)')
    deals_df['createdby'] = pd.to_numeric(deals_df['createdby'], errors='coerce')
    return deals_df

# Função para realizar o merge entre deals e users
def merge_deals_with_users(deals_df, users_df):
    return pd.merge(deals_df[['createdby', 'status']], users_df[['id', 'name']], left_on='createdby', right_on='id', how='left')

# Função para agrupar e contar os deals por usuário e status
def group_and_count_deals(merged_df):
    return merged_df.groupby(['createdby', 'status']).size().reset_index(name='count')



