import requests
import os


def parse_collection():
    url = "http://hubblesite.org/api/v3/images"
    params = {"collection_name": "spacecraft"}
    req = requests.get(url, params=params)
    for info in req.json():
        print(info['id'])
        hubble_parse(info['id'])


def hubble_parse(id):
    url = f"http://hubblesite.org/api/v3/image/{id}"
    req = requests.get(url)
    image_info = req.json()['image_files'][-2]
    image_url = image_info['file_url']
    image_type = image_url.split(".")[-1]
    download_picture(image_url, f"{id}.{image_type}")
    print(f"Сохранено. {id}.{image_type}")


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
    parse_collection()


if __name__ == "__main__":
    main()