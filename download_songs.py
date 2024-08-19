import requests
from bs4 import BeautifulSoup
import os
import sys

def download_songs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    audio_tags = soup.find_all('audio')
    if not audio_tags:
        print("No audio tags found on the page.")
        return

    os.makedirs('downloads', exist_ok=True)

    for i, audio_tag in enumerate(audio_tags):
        audio_url = audio_tag['src']
        try:
            r = requests.get(audio_url, allow_redirects=True)
            filename = os.path.join('downloads', f'song_{i}.mp3')
            with open(filename, 'wb') as f:
                f.write(r.content)
            print(f'Downloaded {filename}')
        except Exception as e:
            print(f"Failed to download {audio_url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        download_songs(url)
    else:
        print("Please provide a URL as a command-line argument.")
