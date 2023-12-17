#%%
import support_ETL as sup
import pandas as pd
#%%
lista_archivos = ["clientes.csv", "ventas.csv", "productos.csv"]
dicc = sup.lectura(lista_archivos)

# %%
for archivo in lista_archivos:
    
    nombre = archivo.split(".")[0]
    print(nombre.upper())
    sup.exploracion_dataframe(dicc[nombre])
    print("___________________________")

#%%
for key in dicc.keys():
    sup.col_minuscula(dicc[key])

# %%
df_productos= dicc["productos"].reset_index()
new_keys = ['id', 'nombre_producto', 'categoría', 'precio', 'origen', 'descripción', 'descripción 2']
sup.cambiar_columnas(df_productos, new_keys)

# %%
df_clientes = dicc["clientes"]
df_ventas = dicc["ventas"]
sup.columnas_cat(df_clientes)

df_productos["descripción 2"] = df_productos["descripción 2"].fillna("Unknown")

# %%
df = sup.mergear(df_clientes,df_ventas,df_productos)
# %%
sup.guardar_df(df, "csv_final")