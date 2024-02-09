from configparser import ConfigParser
# Берём данные из закрытого файла

file_read: ConfigParser = ConfigParser()
file_read.read("../secret.ini")

API_KEY = file_read.get("Bot", "API_KEY")