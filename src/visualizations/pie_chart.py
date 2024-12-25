# Funções para criar gráficos
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import streamlit as st


def plot_pie_chart_svg(status_count):
    # Calcular os tamanhos para cada status
    sizes = status_count.groupby('status')['count'].sum()
    labels = sizes.index
    values = sizes.values

    # Definir cores para cada status
    status_colors = {
        'LOST': 'red',
        'WON': 'green',
        'OPEN': 'orange'
    }
    colors = [status_colors.get(label, 'gray') for label in labels]

    # Criar o gráfico de pizza
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)

    # Título
    plt.title("Distribuição de Status", fontsize=16)

    # Salvar o gráfico em um buffer SVG
    svg_buffer = BytesIO()
    plt.savefig(svg_buffer, format='svg', bbox_inches='tight')
    plt.close()

    # Exibir o gráfico SVG no Streamlit
    svg_buffer.seek(0)
    svg_content = svg_buffer.getvalue().decode('utf-8')
    st.write("Gráfico de Pizza (SVG):")
    st.markdown(f'<svg>{svg_content}</svg>', unsafe_allow_html=True)
