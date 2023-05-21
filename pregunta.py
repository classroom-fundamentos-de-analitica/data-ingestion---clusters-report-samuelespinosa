"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re
from io import StringIO
def ingest_data():
    pattern=r"(\s*)(\d{1,5})(\s{4,})(\d{1,5})(\s{4,})(\d{1,2},\d\s*%)(\s{4,})([a-zA-Z\-\s\,\n\\(\\).\\\/]*)"
    f=open("clusters_report.txt",'r')
    li=list(map(list,re.findall(pattern,f.read())))
    new_li=[['cluster','cantidad_de_palabras_clave','porcentaje_de_palabras_clave','principales_palabras_clave']]
    for i in li: new_li.append([i[1],i[3],i[5],re.sub('\.\s+','',re.sub('\s+',' ',i[7]))])
    return pd.DataFrame(new_li)
ingest_data()

