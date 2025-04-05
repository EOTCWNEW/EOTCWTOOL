from PIL import Image
import exifread
import os
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Display banner
def banner():
    os.system("jp2a /data/data/com.termux/files/home/EOTCW/pics/EOTCWLOGO.jpeg --colors")
    print (Fore.WHITE + "CREATED BY NDE... WORKS SOMETIMES!")
    print (' ')

# Convert GPS coordinates from DMS to decimal
def convert_to_degrees(value):
    d = float(value.values[0])
    m = float(value.values[1])
    s = float(value.values[2])
    return d + (m / 60.0) + (s / 3600.0)


# Extract basic image metadata
def get_basic_metadata(image_path):
    with Image.open(image_path) as img:
        print(Fore.GREEN + f"Image Format: {img.format}")
        print(Fore.GREEN + f"Image Size: {img.size} pixels")
        print(Fore.GREEN + f"Image Mode: {img.mode}")


# Extract EXIF metadata
def get_exif_metadata(image_path):
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)

        exif_keys = [
            "Image Make", "Image Model", "Image DateTime",
            "EXIF FNumber", "EXIF ExposureTime", "EXIF ISOSpeedRatings",
            "EXIF FocalLength", "EXIF LensModel", "GPS GPSAltitude",
            "GPS GPSAltitudeRef", "GPS GPSSpeed", "GPS GPSSpeedRef",
            "GPS GPSTrack", "GPS GPSTrackRef", "GPS GPSDifferential"
        ]

        print(Fore.CYAN + "\n[+] GPS EXIF Metadata:")
        for tag in exif_keys:
            if tag in tags:
                print(Fore.GREEN + f"{tag}: {tags[tag]}")

        # Extract and convert GPS coordinates
        gps_latitude = tags.get("GPS GPSLatitude")
        gps_latitude_ref = tags.get("GPS GPSLatitudeRef")
        gps_longitude = tags.get("GPS GPSLongitude")
        gps_longitude_ref = tags.get("GPS GPSLongitudeRef")

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = convert_to_degrees(gps_latitude)
            lon = convert_to_degrees(gps_longitude)
            if gps_latitude_ref.values[0] != 'N':
                lat = -lat
            if gps_longitude_ref.values[0] != 'E':
                lon = -lon
            print(Fore.GREEN + f"Latitude: {lat:.6f}°")
            print(Fore.GREEN + f"Longitude: {lon:.6f}°")
        else:
            print(Fore.RED + "No GPS data available.")


# Extract all metadata tags
def get_all_tags(image_path):
    print(Fore.CYAN + "\n[+] All Metadata Tags:")
    with open(image_path, 'rb') as img_file:
        tags = exifread.process_file(img_file)
        for tag in tags:
            print(Fore.GREEN + f"{tag}: {tags[tag]}")


# Main execution block
if __name__ == "__main__":
    banner()

    image_path = input(Fore.YELLOW + "Enter the path to the image: ")

    try:
        print(Fore.CYAN + "\n[+] Extracting Basic Image Metadata...")
        get_basic_metadata(image_path)

        print(Fore.CYAN + "\n[+] Extracting EXIF Metadata...")
        get_exif_metadata(image_path)

        print(Fore.CYAN + "\n[+] Extracting Additional Tags...")
        get_all_tags(image_path)

    except FileNotFoundError:
        print(Fore.RED + "[-] Error: File not found.")
