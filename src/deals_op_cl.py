import streamlit as st
import pandas as pd
import ast

# Carregar arquivos CSV
deals_file = "../data/csv/moskit_deals.csv"
users_file = "../data/csv/moskit_users.csv"


# Ler os arquivos
deals_df = pd.read_csv(deals_file)
users_df = pd.read_csv(users_file)

deals_df['createdby'] = deals_df['createdby'].str.extract(r'"id":\s*(\d+)')
deals_df['createdby'] = pd.to_numeric(deals_df['createdby'], errors='coerce')

# Verificar se as colunas 'id' e 'name' existem   
if 'id' not in users_df.columns or 'name' not in users_df.columns:
    st.error("A tabela de usuários deve conter as colunas 'id' e 'name'.")
    st.stop()
    
merged_df = pd.merge(deals_df[['createdby', 'status']], users_df[['id', 'name']], left_on='createdby', right_on='id', how='left')

# Substituir 'createdby' pelo nome do usuário
merged_df['createdby'] = merged_df['name']


# Agrupar por nome de usuário e status, contando os deals
status_count = merged_df.groupby(['createdby', 'status']).size().reset_index(name='count')

# Ordenar por quantidade de deals (opcional)
status_count = status_count.sort_values(by='count', ascending=False)

# Exibir o resultado no Streamlit
st.title("Contagem de Status por Usuário")
st.dataframe(status_count)

# Criar gráfico de barras para visualizar os dados
st.subheader("Gráfico de Contagem por Status e Usuário")
pivot_table = status_count.pivot(index='createdby', columns='status', values='count').fillna(0)
st.bar_chart(pivot_table)