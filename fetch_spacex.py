import requests
import os


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/latest"
    response = requests.get(url)
    info = response.json()
    urls = info['links']['flickr_images']
    for url_number, url in enumerate(urls):
        download_picture(url, f"spacex{url_number}.jpg")


def download_picture(url, filename):
    response = requests.get(url)
    path = ".//images"
    if not os.path.exists(path):
        os.makedirs(path)
    with open(f"{path}//{filename}", 'wb') as f:
        f.write(response.content)


def main():
    fetch_spacex_last_launch()


if __name__== "__main__":
    main()