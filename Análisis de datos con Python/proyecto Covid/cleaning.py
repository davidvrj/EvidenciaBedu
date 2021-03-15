#%%
import pandas as pd
import janitor
#%%
raw = pd.read_csv("data/210228COVID19MEXICO.csv",
                  dtype={"ENTIDAD_NAC":str,
                         "ENTIDAD_RES":str,"MUNICIPIO_RES":str})
#%%
# Describiendo el conjunto de datos
raw.head()
#%%
raw.shape
raw.size
raw.columns
# Como se puede observar el data set contiene mas de 5 millones de observaciones y 40 columnas
#%%
raw.dtypes
# Los primeros pasos son: renombrar las columnas para dejar un formato mas homogeneizado para trabajar, trnsformar los tipos de datos si es necesario, eliminar columnas irrelevantes para el analisis etc.
#%%
raw = raw.clean_names()
#%%
raw.columns
#%%
raw = raw.drop(columns = ["fecha_actualizacion"])

raw = raw.assign(clave_entidad_municipio = raw.entidad_res+raw.municipio_res)

#%%
# Un primer problema que nos encontramos aqui es que necesitamos contar con la entidad federativa asi como el municipio, no solo su clave, por lo tanto se solucionara con una serie de joins
municipios = pd.read_excel("data/201128 Catalogos.xlsx", sheet_name= "Catálogo MUNICIPIOS",
                          dtype={"CLAVE_MUNICIPIO":str,
                                 "CLAVE_ENTIDAD":str})
# para esto necesitamos la dependencia openpyxl
entidades = pd.read_excel("data/201128 Catalogos.xlsx",sheet_name= "Catálogo de ENTIDADES",
                           dtype={"CLAVE_ENTIDAD":str})
#%%
entidades = entidades.clean_names()
municipios = municipios.clean_names()
#%%
#entidades = entidades.assign(clave_municipio = list(map(int,entidades.clave_entidad)))

#municipios = municipios.assign(clave_municipio = list(map(int,entidades.clave_entidad)))
entidades = entidades.drop(columns = "abreviatura")
#%%
entidades_municipios = entidades.merge(municipios,how = "left",
                                       on = "clave_entidad")
entidades_municipios = (
    entidades_municipios.assign(clave_entidad_municipio =
                                entidades_municipios.clave_entidad+entidades_municipios.clave_municipio)
)
#%%
raw = (raw
        .merge(entidades_municipios, how = "left", on = "clave_entidad_municipio")
        )
#%%
# Para nuestro analisis necesitaremos el conjunto de casos positivos, esto supuso un problema al saber como filtrar correctamente los casos positivos por día
# Pero en general , los casos positivos son el conjunto de casos que tengan resultado de muestra positivo o que se clasifiquen positivos por asociación epidemiológica o por dictaminación (solo para defunciones). Se filtran todos los casos positivos (CLASIFICACION_FINAL valores “1”, “2” y “3”) registrados en la base de datos.
confirmed = raw.query("clasificacion_final in [1,2,3]")

# ahora solo queda agrupar y contar por entidades y municipio para cada
# fecha y tendriamos las series de tiempo para cada municipio y estado de confirmados

