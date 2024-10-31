# modules/gga_processor.py
import re

API_KEY = 'AIzaSyBnOHckBAKk-81Ds4-fi-LFZ2FPv7Y2LRg'

def create_google_maps_link(lat, lon):
    """Generates a Google Maps static link for given coordinates."""
    return f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=15&size=600x300&markers=color:red|{lat},{lon}&key={API_KEY}"

def process_gga_sentence(sentence):
    """
    Processes a single GGA sentence, extracts coordinates,
    and generates a Google Maps link.
    """
    match = re.match(r"\$GNGGA,\d+\.\d+,(.*?),(N|S),(.*?),(E|W),.*", sentence)
    if match:
        lat_str, lat_dir, lon_str, lon_dir = match.groups()
        
        # Convert latitude and longitude to decimal format
        lat = float(lat_str[:2]) + float(lat_str[2:]) / 60.0
        lon = float(lon_str[:3]) + float(lon_str[3:]) / 60.0

        # Adjust for hemisphere
        if lat_dir == 'S':
            lat = -lat
        if lon_dir == 'W':
            lon = -lon

        # Generate Google Maps link
        maps_link = create_google_maps_link(lat, lon)
        return maps_link
    
    return None
