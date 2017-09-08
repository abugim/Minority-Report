
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Occurrence classification

def filtro_contem(coluna, regex):
    return coluna.str.contains(regex, case=False)

def classify_occurrences(df):
    
    class_col = df['Class'].astype(str)

    #domesticos
    family = filtro_contem(class_col, r'(?:\b201[1-6])')

    #ofensas sexuais e estupro
    sex_offense = filtro_contem(class_col, r'(?:\b171[1-8]$)')
    rape_crime = filtro_contem(class_col, r'(?:\b21\d$)')

    #lacerny
    larceny = filtro_contem(class_col, r'(?:\b6[1-3][1-9])')

    #robbery
    robbery = filtro_contem(class_col, r"(?:\b3[1-4][1-8])")

    auto_theft = filtro_contem(class_col, r'\b7[1-3]')

    burg = filtro_contem(class_col, r"(?:\b5[1-3][1-9])")
    #drogas/posse de drogas/
    drug = filtro_contem(class_col, r"(?:\b18[1-6][1-8])")

    #ameaça de violencia
    assault = filtro_contem(class_col, r"(?:\b8[1-2][1-5])")

    #AGGRAVATED ASSAULT
    agg_assault = filtro_contem(class_col, r"(?:\b4[1-4][1-5])")

    #vandalismo ou dano objetos/propriedades/ incendio criminoso
    vandalism= filtro_contem(class_col, r"(?:\b14[1-2][1-7]|\b1431)")

    #falsificacao cartao de credito/documentos/cheques etc 
    forgery = filtro_contem(class_col, r"(?:\b101[1-4])")

    #fraude de checks
    badcheck = filtro_contem(class_col, r"(?:\b11[1-2][1-3])")

    #miscleaneos não crimes (infracao, mau compartamento, delito, pessoa/veiculo suspeito)
    #morte naturallost property|porperty
    #perda de posse/abandono de propriedade/recuperaçao
    #desaparecimento, incendio, vadiagem (menor de idade), trespassing, incidente doente mental

    misc = filtro_contem(class_col, r"(?:\b29\d\d)")

    misc_trafic = filtro_contem(class_col, r"(?:\b28\d\d)")

    #leis bebidas alcolicas
    liquor = filtro_contem(class_col, r"(?:\b221[1-7])")

    #suicide
    suicide = filtro_contem(class_col, r"(?:\b261[1-6]|\b262[1-6])")

    #disparo de arma de fogo
    weapon_offense = filtro_contem(class_col, r"(?:\b15[1-4][1-3])")

    #outros crimes class 27xx
    #violaccao ordem de restrição 
    other_offenses = filtro_contem(class_col, r"(?:\b27\d\d)")

    #homicidios
    homicide = filtro_contem(class_col, r"(?:\b11[1-6]$)")

    #desvio de verba
    embezzle = filtro_contem(class_col, r"(?:\b121[1-4]|\b122[1-4])")

    #incidentes, acidentes animals
    animal = filtro_contem(class_col, r"(?:\b3[0-1]\d{2})")

    #crimes por juvenis class 2313 e 2314
    juvenile = filtro_contem(class_col, r"(?:\b211[1-4])")

    #conduta desordeira
    disordely = filtro_contem(class_col, r"(?:\b241[1-3])")

    # roubo de propriedade
    stolen_prop = filtro_contem(class_col, r"(?:\b1311)")

    arson = filtro_contem(class_col, r"(?:\b9[1-3][1-3])")

    vice = filtro_contem(class_col, r'(?:\b161[3-4])')
    
    categorias = [family,
                  sex_offense,
                  rape_crime,
                  larceny,
                  robbery,
                  badcheck,
                  drug,
                  assault,
                  agg_assault,
                  vandalism, 
                  forgery,
                  misc,
                  liquor,
                  suicide,
                  weapon_offense,
                  homicide,
                  embezzle,
                  animal,
                  juvenile,
                  disordely,
                  stolen_prop,
                  auto_theft,
                  burg,
                  misc_trafic,
                  arson,
                  vice,
                  other_offenses]

    cat_str = ['Family offenses',
                  'Sex offenses',
                  'Rape',
                  'Larceny',
                  'Robbery',
                  'Bad checks',
                  'Drugs',
                  'Assault',
                  'Aggravated assault',
                  'Vandalism', 
                  'Forgery',
                  'Miscelaneous',
                  'Liquor laws',
                  'Suicide',
                  'Weapon_offenses',
                  'Homicide',
                  'Embezzle',
                  'Animal offenses',
                  'Juvenile',
                  'Disordely conduct',
                  'Stolen property',
                  'Auto theft',
                  'Burglary',
                  'Miscelaneous traffic',
                  'Arson',
                  'Vice',
                  'Other offenses']
    
    df['Category'] = ''
    for categoria, nome_categoria in zip(categorias, cat_str):
        df.loc[categoria, 'Category'] = nome_categoria


# In[3]:


# Dataset conversion

def dataset_conversion(df):
    df['Dispatch Date / Time'] = pd.to_datetime(df['Dispatch Date / Time'])
    df['Start Date / Time'] = pd.to_datetime(df['Start Date / Time'])
    df['End Date / Time'] = pd.to_datetime(df['End Date / Time'])
    
    df['Zip Code'] = pd.to_numeric(df['Zip Code'].fillna(-1), downcast='integer')
    df['PRA'] = pd.to_numeric(df['PRA'].fillna(-1), downcast='integer')    
    df['Address Number'] = pd.to_numeric(df['Address Number'].fillna(-1), downcast='integer') 

