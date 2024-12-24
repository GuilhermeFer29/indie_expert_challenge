import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Função para carregar os arquivos CSV
def load_data(deals_path, users_path):
    deals_df = pd.read_csv(deals_path)
    users_df = pd.read_csv(users_path)
    return deals_df, users_df

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

def plot_bar_chart(status_count):
    # Definir cores para cada status
    status_colors = {
        'LOST': 'red',
        'WON': 'green',
        'OPEN': 'orange'
    }

    # Garantir que a coluna 'status' está correta e não tenha valores inesperados
    status_count['color'] = status_count['status'].apply(lambda x: status_colors.get(x, 'gray'))  # Default 'gray' caso algum status não esteja no mapeamento

    # Plotando com Matplotlib
    plt.figure(figsize=(10, 6))
    sns.barplot(x='createdby', y='count', hue='status', data=status_count, palette=status_colors)

    # Título e rótulos
    plt.title("Contagem de Status por Usuário", fontsize=16)
    plt.xlabel("Usuário", fontsize=12)
    plt.ylabel("Contagem de Deals", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.legend(title="Status")
    plt.tight_layout()

    # Exibir o gráfico no Streamlit
    st.pyplot(plt)


# Função principal para carregar e processar os dados
def main():
    deals_file = "../data/csv/moskit_deals.csv"
    users_file = "../data/csv/moskit_users.csv"
    
    # Carregar dados
    deals_df, users_df = load_data(deals_file, users_file)
    
    # Preprocessar dados
    deals_df = preprocess_deals(deals_df)

    # Verificar se as colunas essenciais estão presentes
    if 'id' not in users_df.columns or 'name' not in users_df.columns:
        st.error("A tabela de usuários deve conter as colunas 'id' e 'name'.")
        st.stop()

    # Realizar o merge entre deals e users
    merged_df = merge_deals_with_users(deals_df, users_df)
    
    # Substituir 'createdby' pelo nome do usuário
    merged_df['createdby'] = merged_df['name']

    # Remover as colunas desnecessárias (id e name)
    merged_df.drop(columns=['id', 'name'], inplace=True)

    # Verificar se existem valores nulos após o merge
    if merged_df['createdby'].isnull().any():
        st.warning("Alguns registros não encontraram correspondência para o nome do usuário.")

    # Agrupar e contar os deals
    status_count = group_and_count_deals(merged_df)

    # Ordenar por quantidade de deals (opcional)
    status_count = status_count.sort_values(by='count', ascending=False)

    # Exibir resultados
    st.title("Contagem de Status por Usuário")
    st.dataframe(status_count)

    # Criar gráfico de barras customizado
    plot_bar_chart(status_count)

    # Exibir gráficos no Streamlit
    

# Executar a função principal
if __name__ == "__main__":
    main()
