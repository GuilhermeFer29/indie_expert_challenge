import pandas as pd
import os

def tratar_e_salvar_excel_para_csv(xlsx, csv):
    # Lê o arquivo Excel
    df = pd.read_excel(xlsx)
    
    # Preenche valores NaN com 0
    df = df.fillna(0, inplace=False)
    
    # Remove as linhas duplicadas
    df.drop_duplicates(inplace=True)
    
    # Salva o DataFrame em formato CSV
    df.to_csv(csv, index=False)
    
    # Imprime o DataFrame para conferência
    print(df)

def tratamento_dos_dados():
    # Diretórios dos arquivos
    pasta_xlsx = './xlsx/'
    pasta_csv = './csv/'

    # Lista de arquivos para processar (nome do arquivo sem a extensão)
    arquivos = [
        'moskit_activities',
        'moskit_companies',
        'moskit_contacts',
        'moskit_custom_fields',
        'moskit_deals',
        'moskit_lostreasons',
        'moskit_pipelines',
        'moskit_stages',
        'moskit_users'
    ]

    # Para cada arquivo, chama a função de tratamento e conversão
    for arquivo in arquivos:
        xlsx = os.path.join(pasta_xlsx, f'{arquivo}.xlsx')
        csv = os.path.join(pasta_csv, f'{arquivo}.csv')
        
        # Chama a função para tratar e salvar o arquivo
        tratar_e_salvar_excel_para_csv(xlsx, csv)

if __name__ == "__main__":
    tratamento_dos_dados()
    