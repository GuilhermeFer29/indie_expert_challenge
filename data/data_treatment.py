import pandas as pd

'''Funcao que le o arquivo excel e preenchendo 
    os valores NaN com 0    
    e depois e salvando em um arquivo csv com o mesmo nome''' 

def tratamento_dos_dados():
    # ACTIVITIES
    
    df_activities = pd.read_excel('./xlsx/moskit_activities.xlsx')

    df_activities = df_activities.fillna(value=0, inplace=False )



    print(df_activities)


    #Salvando o arquivo csv  
    df_activities.to_csv('./csv/moskit_activities.csv', index=False)

    # COMPANIES
    df_companies = pd.read_excel('./xlsx/moskit_companies.xlsx')
    df_companies = df_companies.fillna(0, inplace=False )



    print(df_companies)

    #Salvando o arquivo csv  
    df_companies.to_csv('./csv/moskit_companies.csv', index=False)

    # CONTACTS
    df_contacts = pd.read_excel('./xlsx/moskit_contacts.xlsx')
    df_contacts = df_contacts.fillna(0, inplace=False)
    print(df_contacts)

    #Salvando o arquivo csv  
    df_contacts.to_csv('./csv/moskit_contacts.csv', index=False)

    # CUSTOM_FIELDS
    df_custom_fields = pd.read_excel('./xlsx/moskit_custom_fields.xlsx')
    df_custom_fields = df_custom_fields.fillna(0, inplace=False , )
    print(df_custom_fields)

    #Salvando o arquivo csv  
    df_custom_fields.to_csv('./csv/moskit_custom_fields.csv', index=False)    

    # DEALS
    df_deals = pd.read_excel('./xlsx/moskit_deals.xlsx')
    df_deals = df_deals.fillna(0, inplace=False )
    print(df_deals)

    #Salvando o arquivo csv  
    df_deals.to_csv('./csv/moskit_deals.csv', index=False)                                              

    # LOSTREASONS
    df_lostreasons = pd.read_excel('./xlsx/moskit_lostreasons.xlsx')
    df_lostreasons = df_lostreasons.fillna(0, inplace=False ) 

    #Salvando o arquivo csv            
    df_lostreasons.to_csv('./csv/moskit_lostreasons.csv', index=False)       


    # PIPELINES
    df_pipelines = pd.read_excel('./xlsx/moskit_pipelines.xlsx')
    df_pipelines = df_pipelines.fillna(0, inplace=False )  

    #Salvando o arquivo csv  
    df_pipelines.to_csv('./csv/moskit_pipelines.csv', index=False)

    # STAGES
    df_stages = pd.read_excel('./xlsx/moskit_stages.xlsx')
    df_stages = df_stages.fillna(0, inplace=False )

    #Salvando o arquivo csv                              
    df_stages.to_csv('./csv/moskit_stages.csv', index=False)

    # USERS
    df_users = pd.read_excel('./xlsx/moskit_users.xlsx')
    df_users = df_users.fillna(0, inplace=False )

    #Salvando o arquivo csv  
    df_users.to_csv('./csv/moskit_users.csv', index=False)  
    
if __name__ == "__main__":
    tratamento_dos_dados()
