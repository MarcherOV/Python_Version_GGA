# main.py
import time
import serial
import RPi.GPIO as GPIO
from googl_maps_api import process_gga_sentence

def log_gga_and_nmea(port, baudrate):
    # GPIO setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    
    # Enable GPIO pin 26 at the start
    GPIO.output(26, GPIO.HIGH)
    print("GPIO 26 enabled.")
    
    try:
        # User input for file names
        gga_file = input("Enter the file name for GGA data: ").strip()
        nmea_file = input("Enter the file name for all NMEA data: ").strip()

        # Clear and open the files
        with open(gga_file, 'w') as file:
            file.write("### GGA Data Log ###\n")
        with open(nmea_file, 'w') as file:
            file.write("### NMEA Data Log ###\n")
        
        # Connect to the port
        ser = serial.Serial(port, baudrate)

        # Enable GNSS
        ser.write(b'AT+QGNSSC=1\r')
        time.sleep(10)  # Delay to allow GNSS module to activate

        print("GPS started. Collecting data... Press Ctrl+C to stop.")
        
        # Start logging NMEA sentences into both files
        with open(gga_file, 'a') as gga_log, open(nmea_file, 'a') as nmea_log:
            try:
                while True:
                    # Request all NMEA sentences
                    ser.write(b'AT+QGNSSRD?\r')
                    time.sleep(1)  # Wait time for complete response

                    # Read all available responses
                    while ser.in_waiting:
                        response = ser.readline().decode('ascii', errors='ignore').strip()

                        # Log all NMEA data to nmea_file
                        if response:
                            nmea_log.write(response + '\n')
                            print(f"NMEA: {response}")

                            # Filter and log only GGA sentences to gga_file
                            if "$GNGGA" in response:
                                # Write the original GGA line
                                gga_log.write(response + '\n')
                                print(f"GGA: {response}")

                                # Process the GGA sentence to add Google Maps link
                                maps_link = process_gga_sentence(response)
                                if maps_link:
                                    gga_log.write(f"# Google Maps: {maps_link}\n")

            except KeyboardInterrupt:
                print("Stopped by user.")

    finally:
        # Disable GNSS and close the port
        ser.write(b'AT+QGNSSC=0\r')
        time.sleep(1)
        ser.close()
        print("GNSS disabled.")

        # Disable GPIO pin 26
        GPIO.output(26, GPIO.LOW)
        GPIO.cleanup()
        print("GPIO 26 disabled.")

# Call the function
log_gga_and_nmea('/dev/ttyAMA0', 115200)
