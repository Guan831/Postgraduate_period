# coding:utf-8
import http.cookiejar
import re
import urllib.request
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time


def get_http_response(url):
    response = requests.get(
        url, headers={'User-Agent': 'testbot'})
    return response


def get_url(number=0):
    s = str(number).zfill(6)
    print("https://www.uta-net.com/song/"+s+"/")
    return "https://www.uta-net.com/song/"+s+"/"


# def get_music_name(string):
#     s = ">"
#     n = string.index(s)
#     d = "<"
#     m = string.index(d)
#     return string[n+1:m]


# def get_movie_name_tostring(string):
#     movie_name = string.lstrip()
#     movie_name = movie_name.rstrip()
#     return movie_name


# def getmain_music_string(string):
#     s = "："
#     begin = string.index(s)+1
#     s = "<"
#     end = string.index(s)
#     return string[begin:end]


def get_moviename_and_musicname(number):
    url = get_url(number)
    res = get_http_response(url)
    if res.status_code != 200:
        return ["", "", "", url]
    soup = BeautifulSoup(res.content, 'lxml')
    headline = soup.select(".row.h-100")[0]
    music_name = headline.select("h2.ms-2.ms-md-3")[0].text
    artist_name = headline.select("h3.ms-2.ms-md-3")[0].text.strip()
    is_movie_name = headline.select("p.ms-2.ms-md-3.mb-0")
    if len(is_movie_name) > 1:
        movie_name = is_movie_name[0].text.strip()
    else:
        movie_name = ""
    return [movie_name, music_name, artist_name, url]


if __name__ == '__main__':
    # get_moviename_and_musicname(12)

    x = 266590
    while True:
        movie = get_moviename_and_musicname(x)
        # print(movie)
        with open("movie_music2.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow(movie)
        x += 1
        time.sleep(2)

'''
    #first_music_id = soup.find(text=music_name_regexp)

        if(soup.td.div.ol.children != None):

        for i, child in enumerate(soup.td.div.ol.children):
            print(child.string)
  
    file = open("movie_music.csv")
    movie_list = list(csv.reader(file))
    movie_list2 = []
    file.close()
    for movie in movie_list:

        if movie[1] != "":
            movie_name = movie[0]
            movie_music_name = get_movie_music_name(movie[1])
            movie_music_artist_name = get_artist_name(movie[1])
            print(movie_name, movie_music_name, movie_music_artist_name)
            movie2 = [movie_name, movie_music_name, movie_music_artist_name]
            movie_list2.append(movie2)
        with open("movie_music_list.csv", "w", encoding='utf-8', newline="") as file:
            writer = csv.writer(file)
            for movie in movie_list2:
                csvRow = []

                csvRow.append(movie[0])
                csvRow.append(movie[1])
                csvRow.append(movie[2])
                writer.writerow(csvRow)
            file.close()
'''
