import streamlit as st
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
