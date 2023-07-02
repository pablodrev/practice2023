import requests
from bs4 import BeautifulSoup


while True:
    try:
        url = input("Ссылка на исполнителя на Яндекс Музыке: ")
        response = requests.get(url + "/tracks")
        break
    except (requests.exceptions.MissingSchema,
            requests.exceptions.InvalidURL,
            requests.exceptions.InvalidSchema):
        print("Неверная ссылка! Попробуйте еще раз.")

soup = BeautifulSoup(response.text, "lxml")
artist_name = soup.find("h1", class_="page-artist__title").text
songs = soup.find_all("div", class_="d-track__name")

print(f"10 самых популярных треков исполнителя {artist_name}: ")
for i in range(10):
    print(f"{i+1}. - {songs[i].text}")
