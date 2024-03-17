import requests
import os
import sys
from PIL import Image

def download_image(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        # Convert the image to WebP format
        with Image.open(file_name) as img:
            webp_file_name = os.path.splitext(file_name)[0] + '.webp'
            img.save(webp_file_name, 'WEBP')
            print(f"Image converted and saved as: {webp_file_name}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: download_image.py <image_url>")
        sys.exit(1)

    image_url = sys.argv[1]
    file_name = os.path.basename(image_url)
    download_image(image_url, file_name)
