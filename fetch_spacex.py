import requests
import os


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/latest"
    req = requests.get(url)
    info = req.json()
    urls = info['links']['flickr_images']
    for url_number, url in enumerate(urls):
        download_picture(url, f"spacex{url_number}.jpg")


def download_picture(url, filename):
    req = requests.get(url)
    path = ".//images"
    if os.path.exists(path):
        with open(f"{path}//{filename}", 'wb') as f:
            f.write(req.content)
    else:
        os.makedirs(path)
        with open(f"{path}//{filename}", 'wb') as f:
            f.write(req.content)


def main():
    fetch_spacex_last_launch()


if __name__== "__main__":
    main()