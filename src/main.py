import pie_chart as pc
from bar_chart import bar_chart

def main():
# Carregar Graficos   
    bar_chart('deals_df', 'users_df','contacts_df', 'status_count')
# Careegar Grafico Pie Chart        
    pc.plot_pie_chart_contacts()
    
# Executar a função principal
if __name__ == "__main__":
    main()
