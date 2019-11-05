# Raspberry Pi Sense HAT

Sense HAT je přídavná senzorová karta pro Raspberry Pi, vyrobená speciálně po misi Astro Pi.

Obsahuje matici 8x8 RGB LED, pětitlačítkový joystick a následující senzory: Gyroskop, Akcelerometr, Magnetometr, Teploměr, Tlakoměr, Vlhkoměr

* Oficiální stránky: https://www.raspberrypi.org/products/sense-hat/

Integrace se serverem TMEP.cz
----
- Skript: [sensehat_tmep_raw.py](sensehat_tmep_raw.py)
- Tento skrip vyčte hodnotu teploty a tlaku z destičky, zobrazí je v linuxové konzoli a na matici LED diod (jen teplotu) a zároveň obě hodnoty odešle na server [https://www.tmep.cz](tmep.cz).
- **Ve skriptu je nutné správně nastavit hodnotu ```guid``` a subdomenu ```url```, tak jak jste je zvolili při registraci na serveru tmep.cz**
- Ukázka výstupu linuxové konzole:
```
START--------------------------------
Sense HAT tmep.cz
Cas a datum: 13:12:08, 05.11.2019
Teplota: 22.6 °C
Vlhkost: 54.3 %
Tlak: 976.3 hPa

Odesilam URL: http://subdomena.tmep.cz/?GUID=22.6&humV=54.3
OK. Odeslano na server.

Zobrazuji teplotu na LED matici.

KONEC--------------------------------
```
- Pro opakované měření (například zde 5 minut) je nutné do cronu přidat:
```
# Logovani teploty z desticky Sense HAT
*/5 * * * * python3 /home/pi/sensehat/sensehat_tmep_raw.py &>/dev/null
```
- Kód vychází z: https://wiki.tmep.cz/doku.php?id=zarizeni:raspberry_pi a https://charlieblog.eu/clanek-raspberry-pi-meteostanice-sense-hat

Sensors
----
- Skript: [sensehat_sensors.py](sensehat_sensors.py) - měření teploty, vlhkosti a tlaku s výpisem do konzole. Teplota se zobrazí na LED matici. Zohledňuje korekci teploty CPU.
