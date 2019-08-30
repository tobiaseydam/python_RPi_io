# python_RPi_io

## Installation

1) Image auf micro-sd-card
2) ssh-Datei auf boot-Partition, ggf auf wpa-supplicant.conf, falls Raspberry Pi in WLAN eingebunden werden soll
3) Betriebssystem updaten:
        
        sudo apt-get update 
        sudo apt-get upgrade

4) Python und git installieren

        sudo apt-get install build-essential python-dev python-openssl git

5) pip installieren

        sudo apt-get install python3-pip

6) Python-Bibliotheken installieren

        sudo pip3 install adafruit_DHT
        sudo pip3 install django
        sudo pip3 install django-crispy-forms
        sudo pip3 install rpyc
        sudo pip3 install paho-mqtt

7) git-Repository klonen

        sudo git clone https://github.com/tobiaseydam/python_RPi_io.git

8) In Verzeichnis wechseln

        cd /python_RPi_io/rpi_io/rpi_io

9) Settings.py anpassen: IP-Addresse des RPi in ALLOWED_HOSTS eintragen

        ALLOWED_HOSTS = ["192.168.178.60"]

10) Server starten

        cd ..
        sudo python3 manage.py runserver 0.0.0.0:8000

11) rpyc-Server starten (in neuem Terminal)

        cd gpio_manager/
        sudo python3 rpycmain.py