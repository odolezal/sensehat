###################
#SenseHat "Meteo"
#Kod poslepoval a upravil: www.odolezal.cz
#ze zdroju:
#https://charlieblog.eu/clanek-raspberry-pi-meteostanice-sense-hat
#enjoy
###################
import os
import datetime
from time import sleep
from sense_hat import SenseHat

#funkce vycteni teploty z CPU
def get_cpu_temperature():
  res = os.popen('vcgencmd measure_temp').readline()
  return(res.replace("temp=","").replace("'C\n",""))

sense = SenseHat()

#definuj barvy
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)

while True:
  sense.clear()

#korekce teploty
#https://www.raspberrypi.org/forums/viewtopic.php?f=104&t=111457
  t = sense.get_temperature()
  cpu = get_cpu_temperature()
  cpu_int = int(float(cpu))
  tc = t - ((cpu_int - t)/ 1.5)

  #tp = sense.get_temperature_from_pressure()
  #th = sense.get_temperature_from_humidity()
  p = sense.get_pressure()

#korekce vlhkosti
  h = sense.get_humidity()
  hc = h * (2.5 - 0.029 * tc)

#zaokrouhli hodnotu na dve desetina mista
  tc_r = round(tc, 2)
  p_r = round(p, 2)
  hc_r = round(hc, 2)

#prevod z "float" na "str"
  tc_r_s = str(tc_r)
  p_r_s = str(p_r)
  hc_r_s = str(hc_r)

#vypis do konzole
  print("--------------------------------")
  print("Cas:", datetime.datetime.now())
  print("Teplota:", tc_r, "°C (po korekci)")
  print("Vlhkost:", hc_r, "R% (po korekci)")
  print("Tlak:", p_r, "hPa")
  print("--------------------------------")

#zobraz hodnoty na LED matici
  #sense.show_message("Hello", text_colour=red, back_colour=white, scroll_speed=0.3)
  #msg = "%s, %s, %s" % (tc_r_s,hc_r_s,p_r_s)
  sense.show_message(tc_r_s, text_colour=blue, scroll_speed=0.09)
  #sense.show_message(hc_r_s, text_colour=yellow, scroll_speed=0.09)
  #sense.show_message(p_r_s, text_colour=green, scroll_speed=0.09)

#pauza
  print("Dalsi mereni za 60 vterin...")
  sleep(60)
