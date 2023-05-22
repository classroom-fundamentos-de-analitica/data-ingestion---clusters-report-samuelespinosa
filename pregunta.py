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
def ingest_data():
    pattern=r"(\s*)(\d{1,5})(\s{4,})(\d{1,5})(\s{4,})(\d{1,2},\d\s*%)(\s{4,})([a-zA-Z\-\s\,\n\\(\\).\\\/]*)"
    f=open("clusters_report.txt",'r')
    li=list(map(list,re.findall(pattern,f.read())))
    f.close()
    new_li=[]
    for i in li: new_li.append([int(i[1]),int(i[3]),float(i[5][:-2].replace(',','.')),re.sub('\.\s*','',re.sub('\s+',' ',i[7]))])
    new_li[5][3]=new_li[5][3][:-1]
    return pd.DataFrame(new_li,columns=['cluster',
                                        'cantidad_de_palabras_clave',
                                        'porcentaje_de_palabras_clave',
                                        'principales_palabras_clave'])
