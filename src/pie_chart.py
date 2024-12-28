import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from function.function_contacts import preprocess_contacts, group_and_count_contacts

def merge_contacts_with_users_via_deals(contacts_df, users_df):
    return pd.merge(
        contacts_df[['createdby']],  # Substituir 'deals_df' por 'contacts_df'
        users_df[['id', 'name']],
        left_on='createdby',
        right_on='id',
        how='left'
    )

def plot_pie_chart_contacts():
    
    # Carregar os dados
    contacts_file = "src/data/csv/moskit_contacts.csv"
    users_file = "src/data/csv/moskit_users.csv"
    contacts_df = pd.read_csv(contacts_file)
    users_df = pd.read_csv(users_file)

    # Pré-processar os dados
    contacts_df, users_df = preprocess_contacts(contacts_df, users_df)    
    merged_df = merge_contacts_with_users_via_deals(contacts_df, users_df)    
    merged_df['createdby'] = merged_df['name'] 
    grouped_contacts = group_and_count_contacts(merged_df)

    # Definir os dados para o gráfico
    labels = grouped_contacts['createdby']  # Nomes dos usuários
    values = grouped_contacts['count']     # Contagem de contatos

    # Criar o gráfico de pizza
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                textinfo='label+percent',
                hole=.3,
                marker=dict(colors=['blue', 'green', 'orange', 'red'])
            )
        ]
    )

  
    st.subheader("Gráfico de Contatos por :red[Vendedor] (Pizza)")
    st.plotly_chart(fig, use_container_width=True)
