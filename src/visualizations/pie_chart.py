# Funções para criar gráficos
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st
import visualizations.bar_chart as bc

def plot_pie_chart_svg(status_count):
    # Calcular os tamanhos para cada status
    sizes = status_count.groupby('status')['count'].sum()
    labels = sizes.index
    values = sizes.values
    explode = (0.1, 0, 0)
    # Definir cores para cada status
    status_colors = {
        'LOST': 'red',
        'WON': 'green',
        'OPEN': 'orange'
    }

    
    # Criar o gráfico
    fig = go.Figure(data=[go.Pie( labels=labels, values=values + explode, textinfo='label+percent', hole=.3, marker=dict(colors=[status_colors.get(label, 'gray') for label in labels]))])

    # Exibir o gráfico
    st.plotly_chart(fig, use_container_width=True)
    
    
    

