import os
import urllib.request

def download_file(url, filename):
    # Check if the file already exists
    if os.path.exists(filename):
        print(f"File '{filename}' already exists. Removing it...")
        os.remove(filename)
        print("File removed.")

    # Download the file
    print(f"Downloading '{filename}' from '{url}'...")
    urllib.request.urlretrieve(url, filename)
    print("Download completed.")

# Provide the URL of the file and the desired filename
url = "https://www.example.com/file.txt"
filename = "file.txt"

# Call the download_file function
download_file(url, filename)
