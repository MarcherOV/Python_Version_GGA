README
Project Description
This Python project enables automatic recording of GPS data in GGA and NMEA formats and adds Google Maps links for coordinates obtained from GGA sentences. It is especially useful for real-time location tracking using a Raspberry Pi that works with a GNSS (Global Navigation Satellite System) module. The project is designed for Linux-based systems (e.g., Raspberry Pi OS), providing real-time geolocation tracking by coordinates.

Key Features
1)Connects to a GNSS module via UART to read NMEA messages.
2)Records all NMEA messages in a designated file.
3)Filters and saves only GGA messages in a separate file, including Google Maps links for each set of coordinates.
4)Configures Raspberry Pi GPIO to control GNSS module power.

Project Structure

The project consists of two main files:

-test2.py: The main script for reading GNSS data, logging it into files, and integrating Google Maps to visualize GGA coordinates.
-googl_maps_api.py: A module that processes GGA messages and creates Google Maps links for static location representation based on obtained coordinates.

Functionality Overview of Each Module

test2.py
1)Importing Libraries: Imports necessary libraries (serial, time, RPi.GPIO) for reading GNSS data, handling time, and working with GPIO on Raspberry Pi. The googl_maps_api module handles GGA message processing.

2)The log_gga_and_nmea Function: This function implements GNSS data reading, filtering, and file logging:
-GPIO Setup: Configures GPIO on Raspberry Pi to activate the GNSS module.
-File Name Prompt: Prompts the user for file names for recording both GGA and all NMEA data.
-Serial Port Initialization: Connects to the GNSS module with a specified serial port and baud rate.
-GNSS Activation: Sends a command to enable the GNSS module.
-Data Processing: Reads all NMEA data in a loop, separating it into all NMEA messages and GGA messages.
  -All NMEA messages are logged in nmea_file.
  -Only GGA messages are logged in gga_file, with each GGA entry followed by a Google Maps link for easy visualization.
-Disabling GNSS and Cleaning GPIO: The function disables the GNSS module and cleans up GPIO settings when the script stops.

googl_maps_api.py

1)API_KEY: Google Maps API key, required for generating static map links.

2)The create_google_maps_link(lat, lon) Function: Creates a Google Maps Static API link with the provided latitude and longitude, displayed for each GGA message.

3)The process_gga_sentence(sentence) Function:

-Accepts a GGA sentence, extracts latitude and longitude.
-Converts coordinates from GGA format to decimal format.
-Uses create_google_maps_link to create a Google Maps link and returns it for logging in the GGA data file.

Example Usage
To run the program:
python3 test2.py

The program will prompt for file names:
Enter the file name for GGA data: gga_data.txt
Enter the file name for all NMEA data: nmea_data.txt

After running, GNSS module data will be recorded in the specified files:
gga_data.txt:
$GNGGA,092751.000,5321.6802,N,00630.3372,W,1,8,1.03,58.9,M,46.9,M,,*47
# Google Maps: https://maps.googleapis.com/maps/api/staticmap?center=53.36134,-6.50562&zoom=15&size=600x300&markers=color:red|53.36134,-6.50562&key=Your_API_Key
nmea_data.txt:
$GNGGA,092751.000,5321.6802,N,00630.3372,W,1,8,1.03,58.9,M,46.9,M,,*47
$GNGLL,5321.6802,N,00630.3372,W,092751.000,A,A*55

Configuration
-Serial port settings, like port and baud rate, can be configured in log_gga_and_nmea() in test2.py:
log_gga_and_nmea('/dev/ttyAMA0', 115200)
-The Google Maps API key is set in googl_maps_api.py:
API_KEY = 'Your_API_Key'

Dependencies
Required Python libraries:

-serial for serial port communication.
-RPi.GPIO for working with GPIO on Raspberry Pi.
-re for regular expressions used to parse GGA messages.

To install dependencies, run:
pip install pyserial RPi.GPIO


README
1. Opis projektu
Ten projekt w Pythonie umożliwia automatyczne zapisywanie danych GPS w formatach GGA i NMEA oraz dodaje linki do Google Maps dla współrzędnych uzyskanych z sentencji GGA. Jest to szczególnie przydatne do śledzenia lokalizacji w czasie rzeczywistym za pomocą Raspberry Pi współpracującego z modułem GNSS (Global Navigation Satellite System). Projekt przeznaczony jest do systemów opartych na Linuxie (np. Raspberry Pi OS), co umożliwia monitorowanie lokalizacji w czasie rzeczywistym na podstawie współrzędnych.

2. Główne funkcje
1)Połączenie z modułem GNSS przez UART w celu odczytu wiadomości NMEA.
2)Zapis wszystkich wiadomości NMEA do pliku.
3)Filtrowanie i zapisywanie tylko wiadomości GGA do osobnego pliku, łącznie z linkami do Google Maps dla każdej pary współrzędnych.
4)Konfiguracja GPIO Raspberry Pi do kontrolowania zasilania modułu GNSS.

3. Struktura projektu
Projekt składa się z dwóch głównych plików:

-test2.py: Główny skrypt do odczytywania danych GNSS, zapisywania ich do plików i integracji z Google Maps w celu wizualizacji współrzędnych GGA.
-googl_maps_api.py: Moduł przetwarzający wiadomości GGA i tworzący linki do Google Maps dla statycznej reprezentacji lokalizacji na podstawie uzyskanych współrzędnych.

4. Przegląd funkcjonalności modułów

test2.py
1)Importowanie bibliotek: Importuje niezbędne biblioteki (serial, time, RPi.GPIO) do odczytu danych GNSS, obsługi czasu oraz pracy z GPIO na Raspberry Pi. Moduł googl_maps_api zajmuje się przetwarzaniem wiadomości GGA.

2)Funkcja log_gga_and_nmea: Funkcja implementuje odczyt danych GNSS, filtrowanie i zapisywanie do plików:

  -Konfiguracja GPIO: Ustawia GPIO na Raspberry Pi, aby aktywować moduł GNSS.
  -Podanie nazw plików: Pyta użytkownika o nazwy plików do zapisania danych GGA oraz wszystkich danych NMEA.
  -Inicjalizacja portu szeregowego: Łączy się z modułem GNSS z określonym portem szeregowym i szybkością transmisji.
  -Aktywacja GNSS: Wysyła polecenie do włączenia modułu GNSS.
  -Przetwarzanie danych: Odczytuje wszystkie dane NMEA w pętli, dzieląc je na wszystkie wiadomości NMEA oraz wiadomości GGA.
   -Wszystkie wiadomości NMEA są zapisywane w nmea_file.
   -Tylko wiadomości GGA są zapisywane w gga_file, a dla każdej wiadomości GGA dodawany jest link do Google Maps, aby ułatwić wizualizację.
  -Wyłączanie GNSS i czyszczenie GPIO: Po zakończeniu pracy skryptu funkcja wyłącza moduł GNSS i czyści ustawienia GPIO.

googl_maps_api.py
1)API_KEY: Klucz API Google Maps, wymagany do generowania linków do statycznej mapy.

2)Funkcja create_google_maps_link(lat, lon): Tworzy link do Google Maps Static API z podanymi współrzędnymi szerokości i długości geograficznej, wyświetlany dla każdej wiadomości GGA.

3)Funkcja process_gga_sentence(sentence):

 -Przyjmuje zdanie GGA, wyodrębnia szerokość i długość geograficzną.
 -Konwertuje współrzędne z formatu używanego w GGA na format dziesiętny.
 -Używa create_google_maps_link, aby utworzyć link do Google Maps i zwraca go do zapisu w pliku danych GGA.

5. Przykład użycia
Aby uruchomić program:


python3 test2.py

Program zapyta o nazwy plików:

Enter the file name for GGA data: gga_data.txt
Enter the file name for all NMEA data: nmea_data.txt

Po uruchomieniu dane z modułu GNSS zostaną zapisane w określonych plikach:

-gga_data.txt:

$GNGGA,092751.000,5321.6802,N,00630.3372,W,1,8,1.03,58.9,M,46.9,M,,*47
# Google Maps: https://maps.googleapis.com/maps/api/staticmap?center=53.36134,-6.50562&zoom=15&size=600x300&markers=color:red|53.36134,-6.50562&key=Twój_API_Key

-nmea_data.txt:

$GNGGA,092751.000,5321.6802,N,00630.3372,W,1,8,1.03,58.9,M,46.9,M,,*47
$GNGLL,5321.6802,N,00630.3372,W,092751.000,A,A*55

6. Konfiguracja

-Ustawienia portu szeregowego, takie jak port i szybkość transmisji, można skonfigurować w log_gga_and_nmea() w test2.py:

log_gga_and_nmea('/dev/ttyAMA0', 115200)

-Klucz API Google Maps jest ustawiany w googl_maps_api.py:

API_KEY = 'Twój_API_Key'

7. Wymagania

Wymagane biblioteki Python:

-serial do komunikacji przez port szeregowy.
-RPi.GPIO do pracy z GPIO na Raspberry Pi.
-re do wyrażeń regularnych używanych do parsowania wiadomości GGA.

Aby zainstalować zależności, uruchom:

pip install pyserial RPi.GPIO
