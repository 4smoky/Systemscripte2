#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################
##      Author : 4smoky      ##
#####################

##Python bibliotheken

import importlib
import subprocess
import shutil
import socket
import time
import yt_dlp
from PIL import Image
import os
import subprocess
import xml.etree.ElementTree as ET

# Funktion zum Löschen des Bildschirms
def clear():
  # Bildschirm löschen
  os.system('clear' if os.name == 'posix' else 'cls')


# Bildschirm löschen
clear()

# Colors - Farben
class Color:
  RED = '\033[91m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RESET = '\033[0m'

# Banner
BANNER_TEXT = r"""
..######..##....##..######..########.########.##.....##..######...######..########..####.########..########.########
.##....##..##..##..##....##....##....##.......###...###.##....##.##....##.##.....##..##..##.....##....##....##......
.##.........####...##..........##....##.......####.####.##.......##.......##.....##..##..##.....##....##....##......
..######.....##.....######.....##....######...##.###.##..######..##.......########...##..########.....##....######..
.......##....##..........##....##....##.......##.....##.......##.##.......##...##....##..##...........##....##......
.##....##....##....##....##....##....##.......##.....##.##....##.##....##.##....##...##..##...........##....##......
..######.....##.....######.....##....########.##.....##..######...######..##.....##.####.##...........##....########
.########..##....##
.##.....##..##..##.
.##.....##...####..
.########.....##...
.##.....##....##...
.##.....##....##...
.########.....##...
.##.........######..##.....##..#######..##....##.##....##
.##....##..##....##.###...###.##.....##.##...##...##..##.
.##....##..##.......####.####.##.....##.##..##.....####..
.##....##...######..##.###.##.##.....##.#####.......##...
.#########.......##.##.....##.##.....##.##..##......##...
.......##..##....##.##.....##.##.....##.##...##.....##...
.......##...######..##.....##..#######..##....##....##...










"""

# Calculate terminal width
WIDTH = shutil.get_terminal_size().columns

# Banner
print('*' * WIDTH)
banner_centered = BANNER_TEXT.center(WIDTH)
print(f"{Color.RED}{banner_centered}{Color.RESET}")
print('*' * WIDTH)
# zeit für banneranzeige
time.sleep(4)
# Bildschirm löschen
clear()

# def --- die Funktionen -- Python Functions
#

#Systeminfo anzeige mit inxi
def inxi():
    print("\nDu hast die Systeminfo gewählt:")
    try:
        subprocess.run(["inxi", "-Fxxxz"], check=True)
        print("Systeminfo erfolgreich ausgeführt.")
    except subprocess.CalledProcessError:
       print("Fehler beim Ausführen von inxi. Ist es installiert?")

# Speicherplatz mit duf
def duf():
     print("\nDu hast Speicherplatz gewählt:")
     try:
          subprocess.run(["duf"], check=True)
     except subprocess.CalledProcessError:
       print("Fehler beim Ausführen von duf. Ist es installiert?")

#Backup der installierten Pakete zu einer text datei
def backup_sichern():
    print("\nDu hast Backup der Pakete gewählt:")
    try:
          subprocess.run(["pacman -Qeq > Pakete.txt"], shell=True, check=True)
          print("Pakete erfolgreich nach Pakete.txt gesichert.")
    except subprocess.CalledProcessError:
          print("Fehler beim Ausführen von pacman. Ist dies eine Arch Linux-Distribution?")

#Wiedeeherstellen des Backups mittels der gesicherten txt datei
def backup_wiederherstellen():
    print("\nDu hast Installieren der Pakete gewählt:")
    try:
          subprocess.run(["sudo pacman -S $(cat Pakete.txt)"], shell=True, check=True)
          print("Pakete erfolgreich von Pakete.txt installiert.")
    except subprocess.CalledProcessError:
          print("Fehler beim Installieren der Pakete. Existiert die Datei Pakete.txt?")

# SSH-Bannergrab
def bannergrab():
  print("\nNetzwerk SSH Bannergrab")
  ip = input("Geben Sie die IP-Adresse ein: ")
  try:
      with socket.socket() as s:
          s.settimeout(5)
          s.connect((ip, 22))

          # Empfange Daten mit einem Timeout
          start_time = time.time()
          chunks = []
          while time.time() - start_time < 3:  # Warte maximal 3 Sekunden auf Daten
              try:
                  chunk = s.recv(1024)
                  if not chunk:
                      break
                  chunks.append(chunk)
              except socket.timeout:
                  break

          answer = b''.join(chunks)

          # Versuche verschiedene Encodings
          encodings = ['utf-8', 'iso-8859-1', 'windows-1252', 'ascii']
          decoded = None
          for encoding in encodings:
              try:
                  decoded = answer.decode(encoding)
                  break
              except UnicodeDecodeError:
                  continue

          if decoded:
              print("\n--- SSH Banner Information ---")
              print(decoded)

              # Sicherheitsbewertung
              print("\n--- Sicherheitsbewertung ---")
              if "diffie-hellman-group1-sha1" in decoded or "3des-cbc" in decoded:
                  print("Warnung: Der Server unterstützt veraltete Algorithmen wie 'diffie-hellman-group1-sha1' und '3des-cbc'.")
                  print("Empfehlung: Diese Algorithmen sollten deaktiviert werden, um die Sicherheit zu erhöhen.")
              else:
                  print("Der Server verwendet keine bekannten veralteten Algorithmen.")

              print("\nSSH Bannergrab erfolgreich ausgeführt.")
          else:
              print("Konnte die empfangenen Daten nicht dekodieren. Hier sind die rohen Bytes:")
              print(answer)

  except Exception as e:
      print(f"Fehler beim SSH Bannergrab: {e}")

#Nmap scanner
def nmap_scanner():
    print("\nNmap Netzwerkscanner")

    # Scan-Optionen mit detaillierten Erklärungen
    scan_options = {
        "1": {"name": "-sS --> SYN Stealth Scan", "cmd": "-sS", "desc": "Schneller, unauffälliger Scan (benötigt root-Rechte)"},
        "2": {"name": "-sV --> Versionserkennungs-Scan", "cmd": "-sV", "desc": "Erkennt Dienste/Versionen auf offenen Ports"},
        "3": {"name": "-A --> Aggressive Scan", "cmd": "-A", "desc": "Aktiviert OS-Erkennung, Versionsscan, Skript-Scan und Traceroute"},
        "4": {"name": "-Pn --> Ping Scan überspringen", "cmd": "-Pn", "desc": "Behandelt alle Hosts als online - überspringt die Erkennungsphase"},
        "5": {"name": "-p --> Alle Ports scannen", "cmd": "-p-", "desc": "Scannt alle 65535 Ports"},
        "6": {"name": "-V --> Ausführliche Ausgabe", "cmd": "-v", "desc": "Erhöht den Detailgrad der Ausgabe"},
        "7": {"name": "-T4 --> Schnelle Scan-Zeitplanung", "cmd": "-T4", "desc": "Aggressivere Zeitplanung für schnelleren Scan"}
    }

    # Zeige Scan-Optionen an
    print("\nVerfügbare Scan-Optionen:")
    for key, value in scan_options.items():
        print(f"{key}. {value['name']} ({value['desc']})")

    # Benutzer wählt Scan-Optionen
    choices = input("\nWählen Sie eine oder mehrere Scan-Optionen (durch Kommas getrennt, z.B. 1,3,4,6 würde folgedes ausführen nmap -sS -A -Pn -V): ").split(',')
    selected_options = [scan_options[choice.strip()] for choice in choices if choice.strip() in scan_options]

    if not selected_options:
        print("Keine gültige Option ausgewählt. Verwende Standard-Scan (-sV).")
        selected_options = [scan_options["2"]]

    # Ziel-IP oder Hostname
    target = input("\nGeben Sie die Ziel-IP oder den Hostnamen ein: ")

    # Erstelle nmap-Befehl
    nmap_cmd = "nmap " + " ".join([opt["cmd"] for opt in selected_options]) + f" {target}"
    use_sudo = any(opt["cmd"] in ["-sS", "-A"] for opt in selected_options)

    if use_sudo:
        nmap_cmd = "sudo " + nmap_cmd

    # Zeige den vollständigen nmap-Befehl an
    print(f"\nAusgeführter nmap-Befehl: {nmap_cmd}")

    # Führe nmap-Scan aus
    print(f"\nFühre Scan auf {target} aus...")
    try:
        result = subprocess.run(nmap_cmd + " -oX -", shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Fehler beim Ausführen von nmap: {result.stderr}")
            return

        # Parsen der XML-Ausgabe
        root = ET.fromstring(result.stdout)

        # Ausgabe der Ergebnisse
        print("\nScan-Ergebnisse:")
        for host in root.findall('.//host'):
            address = host.find('address').get('addr')
            print(f"\nHost: {address}")

            # OS-Erkennung
            os = host.find('.//osclass')
            if os is not None:
                print(f"Betriebssystem: {os.get('osfamily')} {os.get('osgen')}")

            # Offene Ports
            for port in host.findall('.//port'):
                portid = port.get('portid')
                protocol = port.get('protocol')
                state = port.find('state').get('state')
                service = port.find('service')
                if service is not None:
                    service_name = service.get('name')
                    product = service.get('product', '')
                    version = service.get('version', '')
                    print(f"Port {portid}/{protocol} ist {state}: {service_name} {product} {version}")

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

    print("\nScan abgeschlossen.")



#Youtube video herunterladen
def youtube_dl():
  print("\nDu willst von YouTube ein Video herunterladen:")
  url = input("Enter URL: ")
  ydl_opts = {}
  try:
      with yt_dlp.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])
      print("Video erfolgreich heruntergeladen!")
  except Exception as e:
      print(f"Fehler beim Herunterladen: {e}")


#Hintergrund eines bildes entfernen
def rembg():
  print("\nDu willst den Hintergrund von einem Bild entfernen:")
  try:
      from rembg import remove
  except ImportError:
      print("Das Modul 'rembg' ist nicht installiert. Bitte installieren Sie es mit 'pip install rembg'.")
      return

  input_path = input("Gib den Pfad des Bildes ein: ")
  output_path = input("Speicherpfad: ")

  try:
      inp = Image.open(input_path)
      output = remove(inp)
      output.save(output_path)
      print("Hintergrund entfernt und gespeichert.")
  except FileNotFoundError:
      print("Die angegebene Datei wurde nicht gefunden.")
  except Exception as e:
      print("Ein Fehler ist aufgetreten:", str(e))

#
#Mp4 zu Mp3
def convert_mp4_to_mp3():
    input_file = input("Geben Sie den Pfad zur MP4-Datei ein: ")
    output_file = input("Geben Sie den Pfad für die MP3-Datei ein: ")

    try:
        command = f"ffmpeg -i '{input_file}' -vn -acodec libmp3lame -q:a 2 '{output_file}'"
        subprocess.run(command, shell=True, check=True)
        print(f"Konvertierung abgeschlossen. MP3-Datei gespeichert als: {output_file}")
    except subprocess.CalledProcessError:
        print("Fehler bei der Konvertierung. Stellen Sie sicher, dass ffmpeg installiert ist.")

#Bild Komprimieren
def compress_image():
    input_file = input("Geben Sie den Pfad zum Bild ein: ")
    output_file = input("Geben Sie den Pfad für das komprimierte Bild ein: ")
    quality = int(input("Geben Sie die Qualität (1-95) ein: "))

    try:
        with Image.open(input_file) as img:
            img.save(output_file, optimize=True, quality=quality)
        print(f"Bild komprimiert und gespeichert als: {output_file}")
    except Exception as e:
        print(f"Fehler bei der Bildkomprimierung: {e}")

# gif erstelllen aus bildern in einem ordner
def create_gif():
    folder_path = input("Geben Sie den Pfad zum Ordner mit den Bildern ein: ")
    output_file = input("Geben Sie den Pfad für die GIF-Datei ein: ")
    duration = int(input("Geben Sie die Dauer jedes Frames in Millisekunden ein: "))

    try:
        images = []
        for file in sorted(os.listdir(folder_path)):
            if file.endswith((".png", ".jpg", ".jpeg")):
                file_path = os.path.join(folder_path, file)
                images.append(Image.open(file_path))

        images[0].save(output_file, save_all=True, append_images=images[1:], duration=duration, loop=0)
        print(f"GIF erstellt und gespeichert als: {output_file}")
    except Exception as e:
        print(f"Fehler bei der GIF-Erstellung: {e}")

#Video zu gif mit eingabe von start and endzeit
def video_to_gif():
    input_file = input("Geben Sie den Pfad zur Videodatei ein: ")
    output_file = input("Geben Sie den Pfad für die GIF-Datei ein: ")
    start_time = input("Geben Sie den Startpunkt ein (Format: HH:MM:SS): ")
    duration = input("Geben Sie die Dauer ein (Format: HH:MM:SS): ")

    try:
        # Extrahiere den Teil des Videos und konvertiere zu GIF
        command = f"ffmpeg -ss {start_time} -i '{input_file}' -t {duration} -vf 'fps=10,scale=320:-1:flags=lanczos' -c:v gif '{output_file}'"
        subprocess.run(command, shell=True, check=True)
        print(f"GIF erstellt und gespeichert als: {output_file}")
    except subprocess.CalledProcessError:
        print("Fehler bei der Konvertierung. Stellen Sie sicher, dass ffmpeg installiert ist.")


# Begin des scripts mit Begrüßung

print("\nHallo")
time.sleep(1)
print("\nIch hoffe es gefällt dir und hilft dir ein bisschen ;) du solltes beachten das ein paar bibliotheken bzw packete brauchst damit alles funktioniert ")
print("\nDu solltes beachten das ein paar bibliotheken bzw packete brauchst damit alles funktioniert ")
print("\nffmpeg inxi duf yt_dlp nmap--> python imports : rembg ytdlp pillow  ")
time.sleep(1)
print("\nWas möchtest du tun?")
time.sleep(0.5)


# Options - Erstellung des Auswahlmenü
options = ["Systeminfo ",
           "Speicherplatz mit duf Anzeigen ",
           "Speichern aller installierten Pakete in eine Textdatei --> nur für eine Arch Linux-Distro",
           "Installieren der Pakete von der erstellten Textdatei --> nur für eine Arch Linux-Distro",
           "Netzwerk SSH Bannergrab",
           "Nmap Netzwerkscanner",
           "YouTube DL",
           "Hintergrund entfernen",
           "MP4 zu MP3 konvertieren",
           "Bild komprimieren",
           "GIF von Bildern aus einem ordner erstellen",
           "Video zu GIF (eingabe start und endzeit)",
           "Beenden"]

# Endless loop  -- Endlos schleife
while True:
  for index, option in enumerate(options, start=1):
      print(f"\n{index}. {option}")

  # User selection  - Benutzerauswahl
  choice = input("\nDeine Auswahl: ")

  if choice == "1":  #Systeminfo anzeigen
      inxi()
  elif choice == "2": #Speicherplatz mit duf (disk usage with duf)
      duf()
  elif choice == "3": #installierte Pakete in eine Text datei sichern (nur für arch distros)
      backup_sichern()
  elif choice == "4": #Pakete aus der gesicherten Text datei wiederherstellen (nur für arch distros)
      backup_wiederherstellen()
  elif choice == "5": #Netzwerk SSH Bannergrab
      bannergrab()
  elif choice == "6":  # Nmap Netzwerkscanner
     nmap_scanner()
  elif choice == "7": #Youtube video download
      youtube_dl()
  elif choice == "8": #Hintergrund eines bildes entfernen
      rembg()
  elif choice == "9": #Mp3 aus einer mp4 erstellenn
      convert_mp4_to_mp3()
  elif choice == "10": #bild komprimieren
      compress_image()
  elif choice == "11": #gif erstellen aus einem ordner mit bildern
      create_gif()
  elif choice == "12":  # Video zu GIF mit zeiteingabe
    video_to_gif()
  elif choice == "13": #exit - beenden
      print("\nGoodbye")
      break

  else:
      print("\nFalsche Eingabe!!")

  input("\nDrücken Sie Enter, um fortzufahren")

