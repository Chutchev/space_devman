import os
import instabot
import dotenv


def upload_photo(filename, bot):
    bot.upload_photo(filename)
    print(f"Загружено. {filename}")


def main():
    dotenv.load_dotenv()
    login = os.getenv("LOGIN")
    password = os.getenv("PASS")
    directory = os.path.abspath(".//images")
    bot = instabot.Bot()
    bot.login(username=login, password=password)
    for file in os.listdir(directory):
        filename = f"{os.path.join(directory,file)}"
        print(filename)
        upload_photo(filename, bot)


if __name__ == "__main__":
    main()