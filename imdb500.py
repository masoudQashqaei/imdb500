import requests
from bs4 import BeautifulSoup
import pandas as pd

movies =[]

def remove_space(sentence):
    sentence = ''.join(sentence.split())
    return sentence


def get_movie(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for item in soup.find_all('div', class_= 'lister-item-content'):
        name = (item.find('a').get_text())
        year = (item.find('span', class_='lister-item-year').get_text())
        rate = (item.find('span', class_='ipl-rating-star__rating').get_text())
        try:
            metascore = (item.find('span', class_='metascore').get_text())
        except:
            metascore = "none"

        #somehow cant get the certificate span tag when requesting page !!!
        #cert = (item.find('span', class_='certificate').get_text())
        runtime = (item.find('span', class_='runtime').get_text())
        genre = (item.find('span', class_='genre').get_text())
        genre = genre.split(", ")

        genre1 = remove_space(genre[0])

        try:
            genre2 = remove_space(genre[1])
        except:
            genre2="none"
        try:
            genre3 = remove_space(genre[2])
        except:
            genre3="none"


        for i in item.find_all('p', class_='text-muted'):
            if(i.find_all('a') != []):
                director = i.find_all('a')[0].get_text()
                star1 = i.find_all('a')[1].get_text()
                star2 = i.find_all('a')[2].get_text()
                star3 = i.find_all('a')[3].get_text()



        movies.append([name, year, rate, metascore, director, star1, star2, star3, runtime, genre1, genre2, genre3])

urls = [
    "https://www.imdb.com/list/ls050782187/",
    "https://www.imdb.com/list/ls050782187/?sort=list_order,asc&st_dt=&mode=detail&page=2",
    "https://www.imdb.com/list/ls050782187/?sort=list_order,asc&st_dt=&mode=detail&page=3",
    "https://www.imdb.com/list/ls050782187/?sort=list_order,asc&st_dt=&mode=detail&page=4",
    "https://www.imdb.com/list/ls050782187/?sort=list_order,asc&st_dt=&mode=detail&page=5",
]
for url in urls:
    get_movie(url)

#print(movies)
pd.DataFrame(movies).to_excel('output.xlsx', header=False, index=False)