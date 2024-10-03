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
def inxi():
     print("\nDu hast Speicherplatz gewählt:")
     try:
          subprocess.run(["duf"], check=True)
     except subprocess.CalledProcessError:
       print("Fehler beim Ausführen von duf. Ist es installiert?")

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
print("\nffmpeg inxi duf yt_dlp --> python imports : rembg ytdlp pillow  ")
time.sleep(1)
print("\nWas möchtest du tun?")
time.sleep(0.5)


# Options - Erstellung des Auswahlmenü
options = ["Systeminfo ",
           "Speicherplatz mit duf Anzeigen ",
           "Speichern aller installierten Pakete in eine Textdatei --> nur für eine Arch Linux-Distro",
           "Installieren der Pakete von der erstellten Textdatei --> nur für eine Arch Linux-Distro",
           "Netzwerk SSH Bannergrab",
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

  if choice == "1":  #Systeminfo
      inxi()
  elif choice == "2":
      print("\nDu hast Speicherplatz gewählt:")
      try:
          subprocess.run(["duf"], check=True)
      except subprocess.CalledProcessError:
          print("Fehler beim Ausführen von duf. Ist es installiert?")

  elif choice == "3":
      print("\nDu hast Backup der Pakete gewählt:")
      try:
          subprocess.run(["pacman -Qeq > Pakete.txt"], shell=True, check=True)
          print("Pakete erfolgreich nach Pakete.txt gesichert.")
      except subprocess.CalledProcessError:
          print("Fehler beim Ausführen von pacman. Ist dies eine Arch Linux-Distribution?")


  elif choice == "4":
      print("\nDu hast Installieren der Pakete gewählt:")
      try:
          subprocess.run(["sudo pacman -S $(cat Pakete.txt)"], shell=True, check=True)
          print("Pakete erfolgreich von Pakete.txt installiert.")
      except subprocess.CalledProcessError:
          print("Fehler beim Installieren der Pakete. Existiert die Datei Pakete.txt?")

  elif choice == "5":
      print("\nNetzwerk SSH Bannergrab")
      ip = input("Geben Sie die IP-Adresse ein: ")
      try:
          with socket.socket() as s:
              s.settimeout(5)
              s.connect((ip, 22))
              answer = s.recv(1024)
              print(answer.decode())
              print("SSH Bannergrab erfolgreich ausgeführt.")
      except Exception as e:
          print(f"Fehler beim SSH Bannergrab: {e}")

  elif choice == "6":
      print("\nDu willst von YouTube ein Video herunterladen:")
      url = input("Enter URL: ")
      ydl_opts = {}
      try:
          with yt_dlp.YoutubeDL(ydl_opts) as ydl:
              ydl.download([url])
          print("Video erfolgreich heruntergeladen!")
      except Exception as e:
          print(f"Fehler beim Herunterladen: {e}")

  elif choice == "7":
      print("\nDu willst den Hintergrund von einem Bild entfernen:")
      try:
          from rembg import remove
      except ImportError:
          print("Das Modul 'rembg' ist nicht installiert. Bitte installieren Sie es mit 'pip install rembg'.")
          continue

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
  elif choice == "8":
      convert_mp4_to_mp3()
  elif choice == "9":
      compress_image()
  elif choice == "10":
      create_gif()
  elif choice == "11":  # Video zu GIF
    video_to_gif()
  elif choice == "12":
      print("\nGoodbye")
      break

  else:
      print("\nFalsche Eingabe!!")

  input("\nDrücken Sie Enter, um fortzufahren")

