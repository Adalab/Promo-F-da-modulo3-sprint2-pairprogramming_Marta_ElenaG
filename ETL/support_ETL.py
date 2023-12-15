#%%
import pandas as pd
import numpy as np
#%%
def lectura(lista):
    diccionario = {}
    for file in lista:
        nombre = file.split(".")[0]
        try:
            diccionario[nombre] = pd.read_csv(file)
        except:
            diccionario[nombre] = pd.read_csv(file,on_bad_lines='skip')
    return diccionario
    
# %%
# una vez que tengamos nuestro DataFrame preparado con todas las columnas que queremos vamos a crear una función que no haga una exploración inicial del conjunto de datos
def exploracion_dataframe(dataframe):
    print(f"La estructura del dataframe es: {dataframe.shape}")
    print(f"Las columnas del dataframe es: {dataframe.columns}")
    print(f"La información del dataframe es: {dataframe.info()}")
    print(f"Los duplicados que tenemos en el conjunto de datos son: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")
    
    # generamos un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos["%_nulos"])
    
    print("\n ..................... \n")
    print(f"Los tipos de las columnas son:")
    display(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    
    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    
    for col in dataframe_categoricas.columns:
        print(f"La columna {col} tiene las siguientes valore únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()))

    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas numéricas son: ")
    dataframe_numericas = dataframe.select_dtypes(include=np.number)
    for col in dataframe_numericas.columns:
        print(f"La columna {col} tiene las siguientes valore únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()))
# %%
# Country todos Spain

#%%
#CAMBIAR COLUMNAS DE PRODUCTOS
def cambiar_columnas(df, lista_columnas):
    keys = df.columns.tolist()
    diccionario_columnas = dict(zip(keys,lista_columnas))
    df.rename(columns = diccionario_columnas, inplace = True)


# %%
