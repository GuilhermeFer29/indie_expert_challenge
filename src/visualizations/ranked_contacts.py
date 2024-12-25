import pandas as pd
import streamlit as st
import function_contacts as fc



def process_contacts_and_users(contacts_file, users_file):
    if contacts_file and users_file:
        # Ler os arquivos
        contacts_df = pd.read_csv(contacts_file)
        users_df = pd.read_csv(users_file)

        # Extrair o ID de createdby
        contacts_df = fc.preprocess_contacts(contacts_file, users_file)

        # Cruzar com os dados dos usuários
        ranked_users = fc.merge_contacts_with_users(contacts_df, users_df)
        
        # Ordenar pelo número de contatos criados em ordem decrescente
        ranked_users = fc.group_and_count_contacts(ranked_users)
        
        # Exibir os dados no Streamlit
        st.subheader("Ranking de Usuários")
        st.write(ranked_users[['id', 'name', 'username', 'created_count']])

        # Baixar o resultado como CSV
        return  contacts_file, users_file


