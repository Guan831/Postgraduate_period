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
    return response.content


def get_url(number=0):
    s = str(number).zfill(7)
    print("http://cinematicroom.com/soundtrack/"+s+"/")
    return "http://cinematicroom.com/soundtrack/"+s+"/"


def get_movie_name(string):
    s = "≪"
    n = string.index(s)
    return string[0:n]


def get_movie_music_name(string):
    s = "」"
    if(string.find(s) < 0):
        return ""
    n = string.index(s)
    return string[1:n]


def get_artist_name(string):
    s = "」"
    if(string.find(s) < 0):
        return ""
    n = string.index(s)
    end = len(string)
    if(n == end):
        return ""
    return string[n+1:end]


def get_music_name_tostring(string):
    s = "："
    end1 = len(string)
    begin = string.index(s)+1
    s = "<"
    end2 = string.index(s)
    end = min(end1, end2)
    return string[begin:end]


def getmain_music_string(string):
    s = "："
    begin = string.index(s)+1
    s = "<"
    end = string.index(s)
    return string[begin:end]


def get_moviename_and_musicname(number):
    try:
        html = get_http_response(get_url(number))
        soup = BeautifulSoup(html, 'lxml')
        html_movie_name = soup.title.string
        movie_name = get_movie_name(html_movie_name)
        try:
            music_name_string = ""
            music_name_regexp = re.compile("主題歌.*?：.*?<br ?/?>")
            music_name_regexp1 = re.compile("メインテーマ.*?<?>")
            music_name_regexp2 = re.compile("インスパイアソング.*?<?/?li>")
            music_name_regexp3 = re.compile("エンディング曲.*?：.*?<br ?/?>")
            music_name_regexp4 = re.compile("イメージソング.*?：.*?<br ?/?>")
            music_name = music_name_regexp.findall(str(soup))
            music_name = "".join(music_name)
            music_name1 = music_name_regexp1.findall(str(soup))
            music_name1 = "".join(music_name1)
            music_name2 = music_name_regexp2.findall(str(soup))
            music_name2 = "".join(music_name2)
            music_name3 = music_name_regexp3.findall(str(soup))
            music_name_3 = "".join(music_name3)
            music_name4 = music_name_regexp4.findall(str(soup))
            music_name_4 = "".join(music_name4)
            if(music_name != ""):
                music_name_string0 = get_music_name_tostring(music_name)
                music_name_string = music_name_string0
            elif(music_name1 != ""):
                music_name_string1 = get_music_name_tostring(music_name1)
                music_name_string = music_name_string1
            elif(music_name2 != ""):
                music_name_string2 = get_music_name_tostring(music_name2)
                music_name_string = music_name_string2
            elif(music_name_3 != ""):
                music_name_string3 = get_music_name_tostring(music_name3)
                music_name_string = music_name_string3
            elif(music_name_4 != ""):
                music_name_string4 = get_music_name_tostring(music_name)
                music_name_string = music_name_string4
        except ValueError:
            return movie_name, music_name_string
        return movie_name, music_name_string
    except ValueError:
        return "", ""


if __name__ == '__main__':
    # get_moviename_and_musicname(12)
    '''
    for n in range(0, 50):
        file = open("movie_music.csv")
        movie_list = list(csv.reader(file))
        file.close()
        x = 30600

        for i in range(x+n*200, x+200+n*200):
            movie_name, music_name_string = get_moviename_and_musicname(i)
            movie = [movie_name, music_name_string]
            movie_list.append(movie)
            time.sleep(2)

        with open("movie_music.csv", "w", encoding='utf-8', newline="") as file:
       x     writer = csv.writer(file)
            for movie in movie_list:
                csvRow = []

                csvRow.append(movie[0])
                csvRow.append(movie[1])
                writer.writerow(csvRow)
            file.close()
        time.sleep(5)
    '''
    '''
    #first_music_id = soup.find(text=music_name_regexp)
    '''
    '''
        if(soup.td.div.ol.children != None):

        for i, child in enumerate(soup.td.div.ol.children):
            print(child.string)
    '''
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
