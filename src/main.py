import pie_chart as pc
from bar_chart import bar_chart
import streamlit as st
def main():
    
    st.subheader("Este  :red[Dashboard]  apresenta análises de vendas e desempenho de equipe para facilitar a tomada de decisão.")
    
# Carregar Graficos   
    bar_chart()
# Careegar Grafico Pie Chart        
    pc.plot_pie_chart_contacts()
    
    st.markdown("## **Objetivo do :red[Projeto]**")
    
    multi = '''
    O objetivo do projeto é apresentar de forma clara e objetiva o desempenho da equipe de vendas,
    facilitando a tomada de decisão e o acompanhamento de desempenho de cada membro da equipe.
    Facilitando a visualização de dados e a análise de resultados, o que pode contribuir para o aumento
    da eficiência e qualidade dos negócios.
    Tecnica utilizada ao longo do projeto: Python, Streamlit, Pandas, Matplotlib, Plotly.
    para mais informações acesse o link: [GitHub](https://github.com/GuilhermeFer29/indie_expert_challenge)
    '''
    st.markdown(multi)
    
# Executar a função principal
if __name__ == "__main__":
    main()
