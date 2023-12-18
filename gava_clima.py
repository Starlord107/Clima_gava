import requests
import json
#Aqui pedimos la fecha en formato año-mes
ym = input("fecha en formato YYYY-MM: ")
#Guardamos la url de la api
api_url=f"https://archive-api.open-meteo.com/v1/archive?latitude=41.306&longitude=2.001&start_date={ym}-01&end_date={ym}-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"
#Guardamos la respuesta de la api en formato json
response=requests.get(api_url)
dades=json.loads(response.text)
#Tmax es la primera temperatura maxima del mes
Tmax = dades["daily"]["temperature_2m_max"][0]
#La longitud de la lista de temperaturas maximas
ltmax = len(dades["daily"]["temperature_2m_max"])
#Bucle para encontrar la temperatura maxima del mes
for i in range(ltmax):
    if Tmax < dades["daily"]["temperature_2m_max"][i]:
        Tmax = dades["daily"]["temperature_2m_max"][i]
#Tmin es la primera temperatura minima del mes
Tmin = dades["daily"]["temperature_2m_min"][0]
#La longitud de la lista de temperaturas minimas
ltmin = len(dades["daily"]["temperature_2m_min"])
#Bucle para encontrar la temperatura minima del mes
for i in range(ltmin):
    if Tmin > dades["daily"]["temperature_2m_min"][i]:
        Tmin = dades["daily"]["temperature_2m_min"][i]
#dpluja es el numero de dias que ha llovido
dpluja = 0
#La longitud de la lista de precipitaciones
lprec = len(dades["daily"]["precipitation_sum"])
#Bucle para encontrar los dias que ha llovido
for i in range(lprec):
    if dades["daily"]["precipitation_sum"][i] > 0:
        dpluja = dpluja + 1

print("Tmax=",Tmax, "ºC", "Tmin=", Tmin, "ºC", "Dies de pluja:",dpluja)