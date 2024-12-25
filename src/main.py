import streamlit as st
import function_deals as fd
import function_contacts as fc
from visualizations.ranked_contacts import process_contacts_and_users
from visualizations.pie_chart import plot_pie_chart_svg

# Função principal para carregar e processar os dados
def main():
    deals_file = "../data/csv/moskit_deals.csv"
    users_file = "../data/csv/moskit_users.csv"
    contacts_file = "../data/csv/moskit_contacts.csv"
    users_file = "../data/csv/moskit_users.csv"
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

    # Ordenar por quantidade de deals (opcional)
    status_count = status_count.sort_values(by='count', ascending=False)

    # Exibir resultados
    st.title("Contagem de Status por Usuário")
    st.dataframe(status_count)
    st.subheader("Ranking de Usuários")
    st.write(fc.process_contacts_and_users(contacts_file, users_file))
    # Exibir gráficos
    plot_pie_chart_svg(status_count)
    process_contacts_and_users(contacts_file, users_file)
    fc.processed_contacts = fc.preprocess_contacts(contacts_df, users_df)
    

# Executar a função principal
if __name__ == "__main__":
    main()