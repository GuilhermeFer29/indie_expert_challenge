import pandas as pd
import ast

# Função para extrair o ID de 'createdby' e garantir que ele seja numérico
def preprocess_contacts(contacts_df, users_df):
# Verificar se 'createdby' é uma string
    if contacts_df['createdby'].dtype != 'object':
        contacts_df['createdby'] = contacts_df['createdby'].astype(str)

    # Tentar extrair o ID de 'createdby' se for uma string com estrutura JSON-like
    try:
        contacts_df['createdby_id'] = contacts_df['createdby'].apply(lambda x: ast.literal_eval(x).get('id') if isinstance(x, str) else None)
    except (ValueError, SyntaxError):
        raise ValueError("Os valores na coluna 'createdby' não estão no formato esperado (JSON-like).")

    # Contar quantos contatos cada usuário criou
    createdby_count = contacts_df['createdby_id'].value_counts().reset_index()
    createdby_count.columns = ['id', 'created_count']

    # Cruzar com os dados dos usuários
    processed_contacts = pd.merge(createdby_count, users_df, on='id', how='left')
    return processed_contacts


# Função para realizar o merge entre Contacts e users
def merge_contacts_with_users(contacts_df, users_df):
    return pd.merge(contacts_df[['createdby', 'status']], users_df[['id', 'name']], left_on='createdby', right_on='id', how='left')

# Função para agrupar e contar os Contacts por usuário e status
def group_and_count_contacts(merged_df):
    return merged_df.groupby(['createdby', 'status']).size().reset_index(name='count')

def process_contacts_and_users(contacts_file, users_file):
    # Carregar os arquivos
    contacts_df = pd.read_csv(contacts_file)
    users_df = pd.read_csv(users_file)

    # Pré-processar os contatos
    processed_contacts = preprocess_contacts(contacts_df, users_df)

    # Ordenar pelo número de contatos criados em ordem decrescente
    processed_contacts = processed_contacts.sort_values(by='created_count', ascending=False)


