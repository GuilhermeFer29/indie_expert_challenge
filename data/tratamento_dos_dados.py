import pandas as pd

# Lendo o arquivo excel e preenchendo os valores nulos com 0 e salvando em um arquivo csv com o mesmo nome

# ACTIVITIES
df_activities = pd.read_excel('moskit_activities.xlsx')
df_activities = df_activities.fillna(0, inplace=False , downcast='infer')
print(df_activities)
df_activities.to_csv('./csv/moskit_activities.csv', index=False)

# COMPANIES
df_companies = pd.read_excel('moskit_companies.xlsx')
df_companies = df_companies.fillna(0, inplace=False , downcast='infer')
print(df_companies)
df_companies.to_csv('./csv/moskit_companies.csv', index=False)

# CONTACTS
df_contacts = pd.read_excel('moskit_contacts.xlsx')
df_contacts = df_contacts.fillna(0, inplace=False , downcast='infer')
print(df_contacts)
df_contacts.to_csv('./csv/moskit_contacts.csv', index=False)

# CUSTOM_FIELDS
df_custom_fields = pd.read_excel('moskit_custom_fields.xlsx')
df_custom_fields = df_custom_fields.fillna(0, inplace=False , downcast='infer')
print(df_custom_fields)
df_custom_fields.to_csv('./csv/moskit_custom_fields.csv', index=False)    

# DEALS
df_deals = pd.read_excel('moskit_deals.xlsx')
df_deals = df_deals.fillna(0, inplace=False , downcast='infer')
print(df_deals)
df_deals.to_csv('./csv/moskit_deals.csv', index=False)                                              

# LOSTREASONS
df_lostreasons = pd.read_excel('moskit_lostreasons.xlsx')
df_lostreasons = df_lostreasons.fillna(0, inplace=False , downcast='infer')                 
df_lostreasons.to_csv('./csv/moskit_lostreasons.csv', index=False)                        

# PIPELINES
df_pipelines = pd.read_excel('moskit_pipelines.xlsx')
df_pipelines = df_pipelines.fillna(0, inplace=False , downcast='infer')                 
df_pipelines.to_csv('./csv/moskit_pipelines.csv', index=False)

# STAGES
df_stages = pd.read_excel('moskit_stages.xlsx')
df_stages = df_stages.fillna(0, inplace=False , downcast='infer')                                 
df_stages.to_csv('./csv/moskit_stages.csv', index=False)   
   

