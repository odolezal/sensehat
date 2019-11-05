###################
#SenseHat a tmep.cz (verze "RAW" - bez korekce teploty z CPU)
#Kod poslepoval a upravil: www.odolezal.cz
#ze zdroju:
#http://wiki.tmep.cz/doku.php?id=zarizeni:raspberry_pi
#https://charlieblog.eu/clanek-raspberry-pi-meteostanice-sense-hat
#enjoy
###################
import datetime
import httplib2
from time import sleep
from sense_hat import SenseHat
from random import randint

sense = SenseHat()

#definuj barvy
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
orange = (255, 128, 0)

#nahodna barva
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)

#vycisti matici
sense.clear()

#vyctu teplotu z cidla tlaku
t = sense.get_temperature_from_pressure()
#alternativne lze vycist teplotu z cidla vlkosti - mene presne podle pozorovani
 #th = sense.get_temperature_from_humidity()

#vyctu tlak
p = sense.get_pressure()

#vyctu vlhkost
h = sense.get_humidity()

#zaokrouhli hodnoty na jedno desetine misto
t_r = round(t, 1)
p_r = round(p, 1)
h_r = round(h, 1)

#prevod z "float" na "string"
t_r_s = str(t_r)
p_r_s = str(p_r)
h_r_s = str(h_r)

#definuj cas
now = datetime.datetime.now()
date_time = now.strftime("%H:%M:%S, %d.%m.%Y")

#vypis do konzole
print("START--------------------------------")
print("Sense HAT tmep.cz")
print("Cas a datum:", date_time)
print("Teplota:", t_r, "°C")
print("Vlhkost:", h_r, "%")
print("Tlak:", p_r, "hPa")
print(" ")

#zasilani dat na tmep.cz
url = "http://subdomena.tmep.cz/?"
guid = "XXXYYYZZZ"
requesturl = url + guid + "=" + t_r_s + "&humV=" + h_r_s
print("Odesilam URL: " + requesturl)
resp, content = httplib2.Http().request(requesturl)
if resp.status == 200:
 print("OK. Odeslano na server.")
else:
 print("CHYBA! Neodeslano na server!")
print(" ")

#zobraz hodnoty na LED matici
print("Zobrazuji teplotu na LED matici.")
print(" ")
sense.set_rotation(180)
sense.show_message(t_r_s, text_colour=(r, g, b), scroll_speed=0.11)

print("KONEC--------------------------------")
