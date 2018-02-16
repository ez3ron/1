Die Zip-Datei in das Verzeichnis /home/pi oder ein anderes Zielverzeichnis auf dem Raspberry Pi kopieren.

Ein Terminalfenster öffnen:

In das Benutzerverzeichnis vechseln z.B.:
cd /home/pi

wiringPi instakllieren (falls nicht schon geschehen:
sudo apt-get update
sudo apt-get install git-core
git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin
./build
---------- wiringPi installiert -------------

In das Verzeichnis wechseln in dem die zip-Datei entpackt wurde:
cd /home/pi/plotter-cdrom

Das Programm kompillieren:
gcc plotter-cdrom.c -I/usr/local/include -L/usr/local/lib -lwiringPi -lm -o plotter-cdrom

Programm starten mit:
sudo ./plotter-cdrom
