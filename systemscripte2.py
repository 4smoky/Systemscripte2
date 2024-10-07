#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################
##      Author : 4smoky      ##
#####################

# Python libraries
import importlib
import subprocess
import shutil
import socket
import time
import yt_dlp
from PIL import Image
from rembg import remove
import os
import xml.etree.ElementTree as ET

# Set environment variables
os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["ONNX_RUNTIME_EXECUTION_PROVIDERS"] = "CPUExecutionProvider"

# Translations dictionary
translations = {
    "de": {
        "hello": "Hallo",
        "welcome": "Ich hoffe es gefällt dir und hilft dir ein bisschen ;) du solltest beachten, dass du ein paar Bibliotheken bzw. Pakete brauchst, damit alles funktioniert",
        "required_packages": "Du solltest beachten, dass du ein paar Bibliotheken bzw. Pakete brauchst, damit alles funktioniert",
        "package_list": "ffmpeg inxi duf yt_dlp nmap--> python imports : rembg ytdlp pillow",
        "what_to_do": "Was möchtest du tun?",
        "main_menu": "Hauptmenü:",
        "quit": "Beenden",
        "choose_category": "Wählen Sie eine Kategorie: ",
        "back_to_main": "Zurück zum Hauptmenü",
        "choose_option": "Wählen Sie eine Option: ",
        "press_enter": "Drücken Sie Enter, um fortzufahren",
        "invalid_choice": "Ungültige Auswahl. Bitte versuchen Sie es erneut.",
        "goodbye": "Auf Wiedersehen!",
        "system_tools": "Systemtools",
        "system_info": "Systeminfo",
        "show_storage": "Speicherplatz mit duf anzeigen",
        "package_management": "Paketverwaltung",
        "backup_packages": "Pakete sichern",
        "restore_packages": "Pakete wiederherstellen",
        "network_tools": "Netzwerktools",
        "ssh_bannergrab": "SSH Bannergrab",
        "nmap_scanner": "Nmap Scanner",
        "media_tools": "Medientools",
        "youtube_download": "YouTube Download",
        "remove_background": "Hintergrund entfernen",
        "mp4_to_mp3": "MP4 zu MP3 konvertieren",
        "compress_image": "Bild komprimieren",
        "create_gif": "GIF erstellen",
        "video_to_gif": "Video zu GIF",
        "enter_ip_address": "Geben Sie die IP-Adresse ein:",
        "enter_url": "Geben Sie die URL ein:",
        "enter_mp4_path": "Geben Sie den Pfad zur MP4-Datei ein:",
        "enter_mp3_path": "Geben Sie den Speicherort für die MP3-Datei ein:",
        "enter_image_path": "Geben Sie den Pfad zum Bild ein:",
        "enter_compressed_image_path": "Geben Sie den Speicherort für das komprimierte Bild ein:",
        "enter_folder_path": "Geben Sie den Pfad zum Ordner ein:",
        "enter_gif_path": "Geben Sie den Speicherort für das GIF ein:",
        "enter_frame_duration": "Geben Sie die Dauer der Frames in Millisekunden ein:",
        "enter_video_path": "Geben Sie den Pfad zum Video ein:",
        "enter_start_time": "Geben Sie die Startzeit ein (im Format hh:mm:ss):",
        "enter_duration": "Geben Sie die Dauer ein (in Sekunden):",
    },
    "en": {
        "hello": "Hello",
        "welcome": "I hope you like it and it helps you a bit ;) you should note that you need a few libraries or packages for everything to work",
        "required_packages": "You should note that you need a few libraries or packages for everything to work",
        "package_list": "ffmpeg inxi duf yt_dlp nmap--> python imports : rembg ytdlp pillow",
        "what_to_do": "What would you like to do?",
        "main_menu": "Main Menu:",
        "quit": "Quit",
        "choose_category": "Choose a category: ",
        "back_to_main": "Back to Main Menu",
        "choose_option": "Choose an option: ",
        "press_enter": "Press Enter to continue",
        "invalid_choice": "Invalid choice. Please try again.",
        "goodbye": "Goodbye!",
        "system_tools": "System Tools",
        "system_info": "System Info",
        "show_storage": "Show storage with duf",
        "package_management": "Package Management",
        "backup_packages": "Backup Packages",
        "restore_packages": "Restore Packages",
        "network_tools": "Network Tools",
        "ssh_bannergrab": "SSH Bannergrab",
        "nmap_scanner": "Nmap Scanner",
        "media_tools": "Media Tools",
        "youtube_download": "YouTube Download",
        "remove_background": "Remove Background",
        "mp4_to_mp3": "Convert MP4 to MP3",
        "compress_image": "Compress Image",
        "create_gif": "Create GIF",
        "video_to_gif": "Video to GIF",
        "enter_ip_address": "Enter the IP address:",
        "enter_url": "Enter the URL:",
        "enter_mp4_path": "Enter the path to the MP4 file:",
        "enter_mp3_path": "Enter the location for the MP3 file:",
        "enter_image_path": "Enter the path to the image:",
        "enter_compressed_image_path": "Enter the location for the compressed image:",
        "enter_folder_path": "Enter the path to the folder:",
        "enter_gif_path": "Enter the location for the GIF:",
        "enter_frame_duration": "Enter the frame duration in milliseconds:",
        "enter_video_path": "Enter the path to the video:",
        "enter_start_time": "Enter the start time (in hh:mm:ss format):",
        "enter_duration": "Enter the duration (in seconds):",
    },
    "nmap_scan_options": {
        "de": {
            "1": "-sS --> SYN Stealth Scan (Schneller, unauffälliger Scan, benötigt root-Rechte)",
            "2": "-sV --> Versionserkennungs-Scan (Erkennt Dienste/Versionen auf offenen Ports)",
            "3": "-A --> Aggressive Scan (Aktiviert OS-Erkennung, Versionsscan, Skript-Scan und Traceroute)",
            "4": "-Pn --> Ping Scan überspringen (Behandelt alle Hosts als online)",
            "5": "-p --> Alle Ports scannen (Scannt alle 65535 Ports)",
            "6": "-V --> Ausführliche Ausgabe (Erhöht den Detailgrad der Ausgabe)",
            "7": "-T4 --> Schnelle Scan-Zeitplanung (Aggressivere Zeitplanung für schnelleren Scan)",
        },
        "en": {
            "1": "-sS --> SYN Stealth Scan (Fast, stealthy scan, requires root privileges)",
            "2": "-sV --> Version detection scan (Detects services/versions on open ports)",
            "3": "-A --> Aggressive scan (Enables OS detection, version scan, script scan, and traceroute)",
            "4": "-Pn --> Skip ping scan (Treats all hosts as online)",
            "5": "-p --> Scan all ports (Scans all 65535 ports)",
            "6": "-V --> Verbose output (Increases the level of detail in the output)",
            "7": "-T4 --> Fast scan timing (More aggressive timing for faster scans)",
        },
    },
}


# Function to translate text
def translate(key):
    return translations[current_language].get(key, key)


# Function to choose language
def choose_language():
    while True:
        lang = input("Choose language (de/en): ").lower()
        if lang in ["de", "en"]:
            return lang
        print("Invalid choice. Please enter 'de' for German or 'en' for English.")


# Choose language at the beginning of the program
current_language = choose_language()


# Function to clear the screen
def clear():
    os.system("clear" if os.name == "posix" else "cls")


# Clear the screen
clear()


# Colors
class Color:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"


# Banner
BANNER_TEXT = r"""
..######..##....##..######..########.########.##.....##..######...######..########..####.########..########.########
.##....##..##..##..##....##....##....##.......###...###.##....##.##....##.##.....##..##..##.....##....##....##......
.##.........####...##..........##....##.......####.####.##.......##.......##.....##..##..##.....##....##....##......
..######.....##.....######.....##....######...##.###.##..######..##.......########...##..########.....##....######..
.......##....##..........##....##....##.......##.....##.......##.##.......##...##....##..##...........##....##......
.##....##....##....##....##....##....##.......##.....##.##....##.##....##.##....##...##..##...........##....##......
..######.....##.....######.....##....########.##.....##..######...######..##.....##.####.##...........##....########
"""

# Calculate terminal width
WIDTH = shutil.get_terminal_size().columns

# Banner
print("*" * WIDTH)
banner_centered = BANNER_TEXT.center(WIDTH)
print(f"{Color.CYAN}{banner_centered}{Color.RESET}")
print("*" * WIDTH)
# Time for banner display
time.sleep(4)
# Clear the screen
clear()


# System Tools
class SystemTools:
    @staticmethod
    def inxi():
        print(f"\n{translate('system_info')}:")
        try:
            subprocess.run(["inxi", "-Fxxxz"], check=True)
            print(translate("system_info_success"))
        except subprocess.CalledProcessError:
            print(translate("system_info_error"))

    @staticmethod
    def duf():
        print(f"\n{translate('show_storage')}:")
        try:
            subprocess.run(["duf"], check=True)
        except subprocess.CalledProcessError:
            print(translate("duf_error"))


# Package Management
class PackageManagement:
    @staticmethod
    def backup_sichern():
        print(f"\n{translate('backup_packages')}:")
        try:
            subprocess.run(["pacman -Qeq > Pakete.txt"], shell=True, check=True)
            print(translate("backup_packages_success"))
        except subprocess.CalledProcessError:
            print(translate("backup_packages_error"))

    @staticmethod
    def backup_wiederherstellen():
        print(f"\n{translate('restore_packages')}:")
        try:
            subprocess.run(["sudo pacman -S $(cat Pakete.txt)"], shell=True, check=True)
            print(translate("restore_packages_success"))
        except subprocess.CalledProcessError:
            print(translate("restore_packages_error"))


# Network Tools
class NetworkTools:
    @staticmethod
    def bannergrab():
        print("\nSSH Bannergrab")
        ip = input(translate("enter_ip_address"))
        try:
            with socket.socket() as s:
                s.settimeout(10)  # Set timeout to 10 seconds
                s.connect((ip, 22))

                # Receive data with a timeout
                start_time = time.time()
                chunks = []
                while (
                    time.time() - start_time < 5
                ):  # Wait a maximum of 5 seconds for data
                    try:
                        chunk = s.recv(1024)
                        if not chunk:
                            break
                        chunks.append(chunk)
                    except socket.timeout:
                        break

                answer = b"".join(chunks)

                if answer:
                    print("\n--- SSH Banner Information ---")
                    print(answer)  # Show raw bytes

                    # Try various encodings
                    encodings = ["utf-8", "iso-8859-1", "windows-1252", "ascii"]
                    decoded = None
                    for encoding in encodings:
                        try:
                            decoded = answer.decode(encoding)
                            break
                        except UnicodeDecodeError:
                            continue

                    if decoded:
                        print(
                            f"Decoded Banner: {decoded.strip()}"
                        )  # Show decoded banner information
                        print("\n--- Security Assessment ---")
                        if (
                            "diffie-hellman-group1-sha1" in decoded
                            or "3des-cbc" in decoded
                        ):
                            print(
                                "Warning: The server supports outdated algorithms like 'diffie-hellman-group1-sha1' and '3des-cbc'."
                            )
                            print(
                                "Recommendation: These algorithms should be disabled to enhance security."
                            )
                        else:
                            print(
                                "The server does not use any known outdated algorithms."
                            )

                        print("\nSSH Bannergrab executed successfully.")
                    else:
                        print(
                            "Could not decode the received data. Here are the raw bytes:"
                        )
                        print(answer)
                else:
                    print("No data received.")

        except Exception as e:
            print(f"Error during SSH Bannergrab: {e}")

        # Always prompt to continue
        input("\nPress Enter to continue...")

    @staticmethod
    def nmap_scanner():
        print(f"\n{translate('nmap_scanner')}")

        # Scan options with detailed explanations
        scan_options = {
            "1": {
                "name": translations["nmap_scan_options"][current_language]["1"],
                "cmd": "-sS",
                "desc": translations["nmap_scan_options"][current_language]["1"],
            },
            "2": {
                "name": translations["nmap_scan_options"][current_language]["2"],
                "cmd": "-sV",
                "desc": translations["nmap_scan_options"][current_language]["2"],
            },
            "3": {
                "name": translations["nmap_scan_options"][current_language]["3"],
                "cmd": "-A",
                "desc": translations["nmap_scan_options"][current_language]["3"],
            },
            "4": {
                "name": translations["nmap_scan_options"][current_language]["4"],
                "cmd": "-Pn",
                "desc": translations["nmap_scan_options"][current_language]["4"],
            },
            "5": {
                "name": translations["nmap_scan_options"][current_language]["5"],
                "cmd": "-p-",
                "desc": translations["nmap_scan_options"][current_language]["5"],
            },
            "6": {
                "name": translations["nmap_scan_options"][current_language]["6"],
                "cmd": "-v",
                "desc": translations["nmap_scan_options"][current_language]["6"],
            },
            "7": {
                "name": translations["nmap_scan_options"][current_language]["7"],
                "cmd": "-T4",
                "desc": translations["nmap_scan_options"][current_language]["7"],
            },
        }

        # Show scan options
        print("\nAvailable scan options:")
        for key, value in scan_options.items():
            print(f"{key}. {value['name']}")

        # User selects scan options
        choices = input(
            "\nChoose one or more scan options (separated by commas, e.g., 1,3,4,6 would execute nmap -sS -A -Pn -V): "
        ).split(",")
        selected_options = [
            scan_options[choice.strip()]
            for choice in choices
            if choice.strip() in scan_options
        ]

        if not selected_options:
            print("No valid option selected. Using default scan (-sV).")
            selected_options = [scan_options["2"]]

        # Target IP or hostname
        target = input("\nEnter the target IP or hostname: ")

        # Create nmap command
        nmap_cmd = (
            "nmap " + " ".join([opt["cmd"] for opt in selected_options]) + f" {target}"
        )
        use_sudo = any(opt["cmd"] in ["-sS", "-A"] for opt in selected_options)

        if use_sudo:
            nmap_cmd = "sudo " + nmap_cmd

        # Show the complete nmap command
        print(f"\nExecuted nmap command: {nmap_cmd}")

        # Execute nmap scan
        print(f"\nScanning {target}...")
        try:
            result = subprocess.run(
                nmap_cmd + " -oX -", shell=True, capture_output=True, text=True
            )

            if result.returncode != 0:
                print(f"Error executing nmap: {result.stderr}")
                return

            # Parse the XML output
            root = ET.fromstring(result.stdout)

            # Output the results
            print("\nScan results:")
            for host in root.findall(".//host"):
                address = host.find("address").get("addr")
                print(f"\nHost: {address}")

                # OS detection
                os = host.find(".//osclass")
                if os is not None:
                    print(f"Operating System: {os.get('osfamily')} {os.get('osgen')}")

                # Open ports
                for port in host.findall(".//port"):
                    portid = port.get("portid")
                    protocol = port.get("protocol")
                    state = port.find("state").get("state")
                    service = port.find("service")
                    if service is not None:
                        service_name = service.get("name")
                        product = service.get("product", "")
                        version = service.get("version", "")
                        print(
                            f"Port {portid}/{protocol} is {state}: {service_name} {product} {version}"
                        )

        except Exception as e:
            print(f"An error occurred: {e}")

        print("\nScan completed.")


# Media Tools
class MediaTools:
    @staticmethod
    def youtube_dl():
        print(f"\n{translate('youtube_download')}:")
        url = input(f"{translate('enter_url')}: ")
        ydl_opts = {}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Video successfully downloaded!")
        except Exception as e:
            print(f"Error downloading: {e}")

    @staticmethod
    def rembg():
        print(f"\n{translate('remove_background')}:")
        input_path = input("Gib den Pfad des Bildes ein: ")
        output_path = input("Speicherpfad: ")

        try:
            inp = Image.open(input_path)
            output = remove(inp)  # Here the CPU is used
            output.save(output_path)
            print("Background removed and saved.")
        except FileNotFoundError:
            print("The specified file was not found.")
        except Exception as e:
            print("An error occurred:", str(e))

    @staticmethod
    def convert_mp4_to_mp3():
        input_file = input(translate("enter_mp4_path"))
        output_file = input(translate("enter_mp3_path"))

        try:
            command = f"ffmpeg -i '{input_file}' -vn -acodec libmp3lame -q:a 2 '{output_file}'"
            subprocess.run(command, shell=True, check=True)
            print(f"Conversion completed. MP3 file saved as: {output_file}")
        except subprocess.CalledProcessError:
            print("Error during conversion. Please ensure ffmpeg is installed.")

    @staticmethod
    def compress_image():
        input_file = input(translate("enter_image_path"))
        output_file = input(translate("enter_compressed_image_path"))
        quality = int(input(translate("enter_quality")))

        try:
            with Image.open(input_file) as img:
                img.save(output_file, optimize=True, quality=quality)
            print(f"Image compressed and saved as: {output_file}")
        except Exception as e:
            print(f"Error during image compression: {e}")

    @staticmethod
    def create_gif():
        folder_path = input(translate("enter_folder_path"))
        output_file = input(translate("enter_gif_path"))
        duration = int(input(translate("enter_frame_duration")))

        try:
            images = []
            for file in sorted(os.listdir(folder_path)):
                if file.endswith((".png", ".jpg", ".jpeg")):
                    file_path = os.path.join(folder_path, file)
                    images.append(Image.open(file_path))

            images[0].save(
                output_file,
                save_all=True,
                append_images=images[1:],
                duration=duration,
                loop=0,
            )
            print(f"GIF created and saved as: {output_file}")
        except Exception as e:
            print(f"Error during GIF creation: {e}")

    @staticmethod
    def video_to_gif():
        input_file = input(translate("enter_video_path"))
        output_file = input(translate("enter_gif_path"))
        start_time = input(translate("enter_start_time"))
        duration = input(translate("enter_duration"))

        try:
            # Extract part of the video and convert to GIF
            command = f"ffmpeg -ss {start_time} -i '{input_file}' -t {duration} -vf 'fps=10,scale=320:-1:flags=lanczos' -c:v gif '{output_file}'"
            subprocess.run(command, shell=True, check=True)
            print(f"GIF created and saved as: {output_file}")
        except subprocess.CalledProcessError:
            print("Error during conversion. Please ensure ffmpeg is installed.")


# Start of the script with greeting
print(f"\n{translate('hello')}")
time.sleep(1)
print(f"\n{translate('welcome')}")
print(f"\n{translate('required_packages')}")
print(f"\n{translate('package_list')}")
time.sleep(1)
print(f"\n{translate('what_to_do')}")
time.sleep(0.5)


# Menu creation
class Menu:
    def __init__(self):
        self.categories = {
            "1": {
                "name": translate("system_tools"),
                "submenu": {
                    "1": (translate("system_info"), SystemTools.inxi),
                    "2": (translate("show_storage"), SystemTools.duf),
                },
            },
            "2": {
                "name": translate("package_management"),
                "submenu": {
                    "1": (
                        translate("backup_packages"),
                        PackageManagement.backup_sichern,
                    ),
                    "2": (
                        translate("restore_packages"),
                        PackageManagement.backup_wiederherstellen,
                    ),
                },
            },
            "3": {
                "name": translate("network_tools"),
                "submenu": {
                    "1": (translate("ssh_bannergrab"), NetworkTools.bannergrab),
                    "2": (translate("nmap_scanner"), NetworkTools.nmap_scanner),
                },
            },
            "4": {
                "name": translate("media_tools"),
                "submenu": {
                    "1": (translate("youtube_download"), MediaTools.youtube_dl),
                    "2": (translate("remove_background"), MediaTools.rembg),
                    "3": (translate("mp4_to_mp3"), MediaTools.convert_mp4_to_mp3),
                    "4": (translate("compress_image"), MediaTools.compress_image),
                    "5": (translate("create_gif"), MediaTools.create_gif),
                    "6": (translate("video_to_gif"), MediaTools.video_to_gif),
                },
            },
        }

    def display_main_menu(self):
        print(f"\n{translate('main_menu')}")
        for key, category in self.categories.items():
            print(f"{key}. {category['name']}")
        print(f"q. {translate('quit')}")

    def display_submenu(self, category):
        print(f"\n{self.categories[category]['name']} {translate('submenu')}:")
        for key, (name, _) in self.categories[category]["submenu"].items():
            print(f"{key}. {name}")
        print(f"r. {translate('back_to_main')}")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input(f"\n{translate('choose_category')}")

            if choice == "q":
                print(translate("goodbye"))
                break

            if choice in self.categories:
                while True:
                    self.display_submenu(choice)
                    sub_choice = input(f"\n{translate('choose_option')}")

                    if sub_choice == "r":
                        break

                    if sub_choice in self.categories[choice]["submenu"]:
                        _, function = self.categories[choice]["submenu"][sub_choice]
                        function()
                        input(f"\n{translate('press_enter')}")
                    else:
                        print(translate("invalid_choice"))
            else:
                print(translate("invalid_choice"))


if __name__ == "__main__":
    menu = Menu()
    menu.run()
