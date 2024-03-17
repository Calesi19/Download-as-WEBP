# Download-as-WEBP

![Banner](docs/banner.webp)

A simple script to download images from a URL and convert them to WebP format. You can run the script from the terminal no matter what directory you are in. The image will download as WEBP format on that current directory. 

Helpful if you are a frontend developer that often works with webp images.

# Setup

### 1. Create a virtual environment
```
python -m venv venv
```
### 2. Activate the virtual environment
On Windows
```
venv\Scripts\activate
```
On Mac/Linux
```
source venv/bin/activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```

# PyInstaller

### Create a standalone executable
```
pyinstaller --onefile src/download_image.py
```
### Move the executable to a directory in your PATH

On Windows
```
move dist\download_image C:\path\to\your\directory

```
On Mac/Linux
```
sudo mv dist/download_image /usr/local/bin
```

# Usage

Run the script
```
download_image "https://example.com/example-image.jpg"
```

You can run the script from the terminal no matter what directory you are in. The image will download as WEBP format on that current directory.