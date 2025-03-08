import requests
import folium
import webbrowser

def get_ip_location():
    try:
        # Fetch public IP address
        ip_address = requests.get("https://api64.ipify.org?format=json").json()["ip"]
        
        # Get location details using ip-api
        response = requests.get(f"http://ip-api.com/json/{ip_address}").json()
        
        if response["status"] == "success":
            lat, lon = response["lat"], response["lon"]
            city, country = response["city"], response["country"]
            return lat, lon, city, country
        else:
            print("Error: Unable to fetch location.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_map(lat, lon, city, country):
    # Create a folium map centered at the user's location
    location_map = folium.Map(location=[lat, lon], zoom_start=12)
    
    # Add a marker
    folium.Marker([lat, lon], popup=f"Location: {city}, {country}", tooltip="You are here").add_to(location_map)
    
    # Save the map to an HTML file
    map_file = "geolocation_map.html"
    location_map.save(map_file)
    
    # Open the map in a web browser
    webbrowser.open(map_file)

if __name__ == "__main__":
    location = get_ip_location()
    
    if location:
        lat, lon, city, country = location
        print(f"Your Location: {city}, {country} (Lat: {lat}, Lon: {lon})")
        create_map(lat, lon, city, country)
