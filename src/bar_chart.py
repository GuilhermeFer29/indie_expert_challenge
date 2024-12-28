import function.function_deals as fd
import streamlit as st
import altair as alt

def bar_chart():
    # Caminhos para os arquivos
    deals_file = "src/data/csv/moskit_deals.csv"
    users_file = "src/data/csv/moskit_users.csv"
    contacts_file = "src/data/csv/moskit_contacts.csv"

    # Carregar os dados
    deals_df, users_df, contacts_df = fd.load_data(deals_file, users_file, contacts_file)

    # Preprocessar dados
    deals_df = fd.preprocess_deals(deals_df)

    # Verificar se as colunas essenciais estão presentes
    if 'id' not in users_df.columns or 'name' not in users_df.columns:
        st.error("A tabela de usuários deve conter as colunas 'id' e 'name'.")
        st.stop()

    # Realizar o merge entre deals e users
    merged_df = fd.merge_deals_with_users(deals_df, users_df)
    
    # Substituir 'createdby' pelo nome do usuário
    merged_df['createdby'] = merged_df['name']
    merged_df.drop(columns=['id', 'name'], inplace=True)

    # Aviso sobre valores nulos
    null_count = merged_df['createdby'].isnull().sum()
    if null_count > 0:
        st.warning(f"Existem {null_count} registros sem correspondência de usuário.")

    # Agrupar e contar os deals
    status_count = fd.group_and_count_deals(merged_df)
    status_count = status_count.sort_values(by='count', ascending=False)
    status_colors = {
        "lost": "red",
        "won": "orange",
        "open": "green"
    }

# Gráfico de barras com Altair e mapeamento de cores
    bar_chart = alt.Chart(status_count).mark_bar().encode(
    x='count:Q',
    y=alt.Y('createdby:N', sort='-x'),
    color=alt.Color('status:N', scale=alt.Scale(domain=list(status_colors.keys()), range=list(status_colors.values()))),
    tooltip=['createdby', 'status', 'count']
).properties(
    title="Status de Quantidade de Ofertas por Vendedor"
)

    st.altair_chart(bar_chart, use_container_width=True)
    
    return status_count, deals_df, users_df, contacts_df


'''
def bar_chart(deals_df, users_df,contacts_df, status_count):
    # Carregar os dados
    deals_file = "src/data/csv/moskit_deals.csv" 
    users_file = "src/data/csv/moskit_users.csv"
    contacts_file = "src/data/csv/moskit_contacts.csv"
    
    deals_df, users_df, contacts_df = fd.load_data(deals_file, users_file, contacts_file)

    # Carregar dados
    deals_df, users_df, contacts_df = fd.load_data(deals_file, users_file, contacts_file)
    # Preprocessar dados
    deals_df = fd.preprocess_deals(deals_df)

    # Verificar se as colunas essenciais estão presentes
    if 'id' not in users_df.columns or 'name' not in users_df.columns:
        st.error("A tabela de usuários deve conter as colunas 'id' e 'name'.")
        st.stop()

    # Realizar o merge entre deals e users
    merged_df = fd.merge_deals_with_users(deals_df, users_df)
    
    # Substituir 'createdby' pelo nome do usuário
    merged_df['createdby'] = merged_df['name']

    # Remover as colunas desnecessárias (id e name)
    merged_df.drop(columns=['id', 'name'], inplace=True)

    # Verificar se existem valores nulos após o merge
    if merged_df['createdby'].isnull().any():
        st.warning("Alguns registros não encontraram correspondência para o nome do usuário.")

    # Agrupar e contar os deals
    status_count = fd.group_and_count_deals(merged_df)

    # Ordenar por quantidade de deals 
    status_count = status_count.sort_values(by='count', ascending=False)
    # Exibir resultados
    st.subheader(" Status de  Quantidade de Ofertas por :red[Vendedor] (Barras) ")
    st.bar_chart(status_count, x= "createdby", y="count", color="status", horizontal=True)
    
    return status_count , deals_df, users_df , contacts_df'''