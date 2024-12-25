# Funções auxiliares (cálculos, transformação de dados)

# Ranquear Funil de vendas De onde mais acessou
# Ranquear Funil de vendas Por quem mais criou contatos ok

# proximo  deals Open e Closed por vendedor grafico pizza ou barras

# ranque de leads que fechou com o concorrente
'''import streamlit as st
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
st.bar_chart(pivot_table)'''






'''import streamlit as st
import pandas as pd
import ast

# Título do aplicativo
st.title("Ranking de Usuários por Contatos Criados")

# Carregar arquivos CSV
contacts_file = "../data/csv/moskit_contacts.csv"
users_file = "../data/csv/moskit_users.csv"

if contacts_file and users_file:
    # Ler os arquivos
    contacts_df = pd.read_csv(contacts_file)
    users_df = pd.read_csv(users_file)

    # Extrair o ID de createdby
    contacts_df['createdby_id'] = contacts_df['createdby'].apply(lambda x: ast.literal_eval(x).get('id'))

    # Contar quantos contatos cada usuário criou
    createdby_count = contacts_df['createdby_id'].value_counts().reset_index()
    createdby_count.columns = ['id', 'created_count']

    # Cruzar com os dados dos usuários
    ranked_users = pd.merge(createdby_count, users_df, on='id', how='left')

    # Ordenar pelo número de contatos criados em ordem decrescente
    ranked_users = ranked_users.sort_values(by='created_count', ascending=False)

    # Exibir os dados no Streamlit
    st.subheader("Ranking de Usuários")
    st.write(ranked_users[['id', 'name', 'username', 'created_count', ]])

    # Baixar o resultado como CSV
    csv = ranked_users.to_csv(index=False)
    st.download_button(
        label="Baixar Ranking como CSV",
        data=csv,
        file_name="ranking_usuarios.csv",
        mime="text/csv",
    )
else:
    st.info("Por favor, faça o upload dos dois arquivos para começar.")
'''