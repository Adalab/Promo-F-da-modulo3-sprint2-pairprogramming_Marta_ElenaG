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
# %%
df_productos= dicc["productos"].reset_index()
new_keys = ['ID', 'Nombre_Producto', 'Categoría', 'Precio', 'Origen', 'Descripción', 'Descripción 2']
sup.cambiar_columnas(df_productos, new_keys)

# %%
