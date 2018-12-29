from flask import Flask, render_template, url_for, flash, redirect, request
from forms import SearchForm
import pickle
from PyLyrics import *
import pandas as pd

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456'


with open("rap_lyrics.pkl", 'rb') as picklefile:
    rap_lyrics = pickle.load(picklefile)

with open("rap_tracks.pkl", 'rb') as picklefile1:
    rap_tracks = pickle.load(picklefile1)

with open("rap_list.pkl", 'rb') as picklefile2:
    rap_list = pickle.load(picklefile2)

with open("closest_rap.pkl", 'rb') as picklefile3:
    closest_rap = pickle.load(picklefile3)

with open("closest_rap_audio.pkl", 'rb') as picklefile3:
    closest_rap_audio= pickle.load(picklefile3)

with open("closest_rap_both.pkl", 'rb') as picklefile3:
    closest_rap_both= pickle.load(picklefile3)

with open("rb_lyrics.pkl", 'rb') as picklefile3:
    rb_lyrics= pickle.load(picklefile3)

with open("rb_tracks.pkl", 'rb') as picklefile3:
    rb_tracks= pickle.load(picklefile3)

with open("rb_list.pkl", 'rb') as picklefile3:
    rb_list= pickle.load(picklefile3)

with open("closest_rb_lyrics.pkl", 'rb') as picklefile3:
    closest_rb_lyrics= pickle.load(picklefile3)

with open("closest_rap_audio.pkl", 'rb') as picklefile3:
    closest_rb_audio= pickle.load(picklefile3)

with open("country_lyrics.pkl", 'rb') as picklefile3:
    country_lyrics= pickle.load(picklefile3)

with open("country_list.pkl", 'rb') as picklefile3:
    country_list= pickle.load(picklefile3)

with open("closest_country_audio.pkl", 'rb') as picklefile3:
    closest_country_audio= pickle.load(picklefile3)

with open("closest_country_lyrics.pkl", 'rb') as picklefile3:
    closest_country_lyrics= pickle.load(picklefile3)

with open("rock_list.pkl", 'rb') as picklefile3:
    rock_list= pickle.load(picklefile3)

with open("rock_lyrics.pkl", 'rb') as picklefile3:
    rock_lyrics= pickle.load(picklefile3)

with open("closest_rock_lyrics.pkl", 'rb') as picklefile3:
    closest_rock_lyrics= pickle.load(picklefile3)

with open("closest_rock_audio.pkl", 'rb') as picklefile3:
    closest_rock_audio= pickle.load(picklefile3)

with open("rock_tracks.pkl", 'rb') as picklefile3:
    rock_tracks= pickle.load(picklefile3)

with open("closest_both_rock.pkl", 'rb') as picklefile3:
    closest_both_rock= pickle.load(picklefile3)

with open("closest_both_rb.pkl", 'rb') as picklefile3:
    closest_both_rb= pickle.load(picklefile3)

with open("closest_both_country.pkl", 'rb') as picklefile3:
    closest_both_country= pickle.load(picklefile3)

with open("lyrics_dict.pkl", 'rb') as picklefile3:
    lyrics_dict= pickle.load(picklefile3)

with open("lyrics_list.pkl", 'rb') as picklefile3:
    lyrics_list= pickle.load(picklefile3)

with open("tracks.pkl", 'rb') as picklefile3:
    tracks= pickle.load(picklefile3)

with open("closest_both.pkl", 'rb') as picklefile3:
    closest_both= pickle.load(picklefile3)

with open("closest_lyrics.pkl", 'rb') as picklefile3:
    closest_lyrics= pickle.load(picklefile3)

with open("closest_audio.pkl", 'rb') as picklefile3:
    closest_audio= pickle.load(picklefile3)

def similar_rap_lyrics_audio(artist,song):
    neighbors_lyrics=[]
    neighbors = []
    neighbors_audio = []
    neighbors1 = []
    neighbors_both = []
    neighbors2= []

    lyrics = PyLyrics.getLyrics(artist,song)
    clean_lyrics = lyrics.replace('\n',' ')

    position = rap_list.index(clean_lyrics)

    for song in closest_rap[position]:
        for index in song:
            if index != position:
                neighbors_lyrics.append(rap_list[index])

    for song in closest_rap_audio[position]:
        for index in song:
            if index != position:
                neighbors_audio.append(rap_list[index])

    for song in closest_rap_both[position]:
        for index in song:
            if index != position:
                neighbors_both.append(rap_list[index])

    for dicts in rap_lyrics:
        for key,val in dicts.items():
            for i in neighbors_lyrics:
                if val == i:
                    neighbors.append(dicts['Artist'] + ' : ' + key)
                    neighbors = list(set(neighbors))

    for dicts in rap_lyrics:
        for key,val in dicts.items():
            for i in neighbors_audio:
                if val == i:
                    neighbors1.append(dicts['Artist'] + ' : ' + key)
                    neighbors1 = list(set(neighbors1))

    for dicts in rap_lyrics:
        for key,val in dicts.items():
            for i in neighbors_both:
                if val == i:
                    neighbors2.append(dicts['Artist'] + ' : ' + key)
                    neighbors2 = list(set(neighbors2))

    return neighbors,neighbors1,neighbors2

def similar_rb_lyrics_audio(artist,song):
    neighbors_lyrics=[]
    neighbors = []
    neighbors_audio = []
    neighbors1 = []
    neighbors_both = []
    neighbors2 = []

    lyrics = PyLyrics.getLyrics(artist,song)
    clean_lyrics = lyrics.replace('\n',' ')

    position = rb_list.index(clean_lyrics)

    for song in closest_rb_lyrics[position]:
        for index in song:
            if index != position:
                neighbors_lyrics.append(rb_list[index])

    for song in closest_rb_audio[position]:
        for index in song:
            if index != position:
                neighbors_audio.append(rb_list[index])

    for song in closest_both_rb[position]:
        for index in song:
            if index != position:
                neighbors_both.append(rb_list[index])


    for dicts in rb_lyrics:
        for key,val in dicts.items():
            for i in neighbors_lyrics:
                if val == i:
                    neighbors.append(dicts['Artist'] + ' : ' + key)
                    neighbors = list(set(neighbors))

    for dicts in rb_lyrics:
        for key,val in dicts.items():
            for i in neighbors_audio:
                if val == i:
                    neighbors1.append(dicts['Artist'] + ' : ' + key)
                    neighbors1 = list(set(neighbors1))

    for dicts in rb_lyrics:
        for key,val in dicts.items():
            for i in neighbors_both:
                if val == i:
                    neighbors2.append(dicts['Artist'] + ' : ' + key)
                    neighbors2 = list(set(neighbors2))

    return neighbors,neighbors1,neighbors2

def similar_country_lyrics_audio(artist,song):
    neighbors_lyrics=[]
    neighbors = []
    neighbors_audio = []
    neighbors1 = []
    neighbors_both = []
    neighbors2 = []

    lyrics = PyLyrics.getLyrics(artist,song)
    clean_lyrics = lyrics.replace('\n',' ')

    position = country_list.index(clean_lyrics)

    for song in closest_country_lyrics[position]:
        for index in song:
            if index != position:
                neighbors_lyrics.append(country_list[index])

    for song in closest_country_audio[position]:
        for index in song:
            if index != position:
                neighbors_audio.append(country_list[index])

    for song in closest_both_country[position]:
        for index in song:
            if index != position:
                neighbors_both.append(country_list[index])

    for dicts in country_lyrics:
        for key,val in dicts.items():
            for i in neighbors_lyrics:
                if val == i:
                    neighbors.append(dicts['Artist'] + ' : ' + key)
                    neighbors = list(set(neighbors))

    for dicts in country_lyrics:
        for key,val in dicts.items():
            for i in neighbors_audio:
                if val == i:
                    neighbors1.append(dicts['Artist'] + ' : ' + key)
                    neighbors1 = list(set(neighbors1))

    for dicts in country_lyrics:
        for key,val in dicts.items():
            for i in neighbors_both:
                if val == i:
                    neighbors2.append(dicts['Artist'] + ' : ' + key)
                    neighbors2 = list(set(neighbors2))

    return neighbors,neighbors1,neighbors2

def similar_rock_lyrics_audio(artist,song):
    neighbors_lyrics=[]
    neighbors = []
    neighbors_audio = []
    neighbors1 = []
    neighbors_both = []
    neighbors2 = []

    lyrics = PyLyrics.getLyrics(artist,song)
    clean_lyrics = lyrics.replace('\n',' ')

    position = rock_list.index(clean_lyrics)

    for song in closest_rock_lyrics[position]:
        for index in song:
            neighbors_lyrics.append(rock_list[index])

    for song in closest_rock_audio[position]:
        for index in song:
            neighbors_audio.append(rock_list[index])

    for song in closest_both_rock[position]:
        for index in song:
            neighbors_audio.append(rock_list[index])

    for dicts in rock_lyrics:
        for key,val in dicts.items():
            for i in neighbors_lyrics:
                if val == i:
                    neighbors.append(dicts['Artist'] + ' : ' + key)
                    neighbors = list(set(neighbors))

    for dicts in rock_lyrics:
        for key,val in dicts.items():
            for i in neighbors_audio:
                if val == i:
                    neighbors1.append(dicts['Artist'] + ' : ' + key)
                    neighbors1 = list(set(neighbors1))

    for dicts in rock_lyrics:
        for key,val in dicts.items():
            for i in neighbors_both:
                if val == i:
                    neighbors2.append(dicts['Artist'] + ' : ' + key)
                    neighbors2 = list(set(neighbors2))



    return neighbors,neighbors1,neighbors2


def similar_any_lyrics_audio(artist,song):
    neighbors_lyrics=[]
    neighbors = []
    neighbors_audio = []
    neighbors1 = []
    neighbors_both = []
    neighbors2 = []

    lyrics = PyLyrics.getLyrics(artist,song)
    clean_lyrics = lyrics.replace('\n',' ')

    position = lyrics_list.index(clean_lyrics)

    for song in closest_lyrics[position]:
        for index in song:
            neighbors_lyrics.append(lyrics_list[index])

    for song in closest_audio[position]:
        for index in song:
            neighbors_audio.append(lyrics_list[index])

    for song in closest_both[position]:
        for index in song:
            neighbors_both.append(lyrics_list[index])

    for dicts in lyrics_dict:
        for key,val in dicts.items():
            for i in neighbors_lyrics:
                if val == i:
                    neighbors.append(dicts['Artist'] + ' : ' + key)
                    neighbors = list(set(neighbors))

    for dicts in lyrics_dict:
        for key,val in dicts.items():
            for i in neighbors_audio:
                if val == i:
                    neighbors1.append(dicts['Artist'] + ' : ' + key)
                    neighbors1 = list(set(neighbors1))

    for dicts in lyrics_dict:
        for key,val in dicts.items():
            for i in neighbors_both:
                if val == i:
                    neighbors2.append(dicts['Artist'] + ' : ' + key)
                    neighbors2 = list(set(neighbors2))



    return neighbors,neighbors1,neighbors2



@app.route("/")

@app.route("/fill",methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        rb_artist = form.rb.data
        rb_song = form.rb_song.data
        rap_artist = form.rap.data
        rap_song = form.rap_song.data
        country_artist = form.country.data
        country_song = form.country_song.data
        rock_artist = form.rock.data
        rock_song = form.rock_song.data
        any_artist = form.any.data
        any_song = form.any_song.data

        if rap_artist:
            result,result1,result2 = similar_rap_lyrics_audio(rap_artist,rap_song)
            return render_template('home.html',result=result,result1 = result1,result2=result2)

        elif country_artist:
            result,result1,result2 = similar_country_lyrics_audio(country_artist,country_song)
            return render_template('home.html',result=result,result1 = result1,result2=result2)

        elif rb_artist:
            result,result1,result2 = similar_rb_lyrics_audio(rb_artist,rb_song)
            return render_template('home.html',result=result,result1 = result1,result2=result2)

        elif rock_artist:
            result,result1,result2 = similar_rock_lyrics_audio(rock_artist,rock_song)
            return render_template('home.html',result=result,result1 = result1,result2=result2)

        else:
            result,result1,result2 = similar_any_lyrics_audio(any_artist,any_song)
            return render_template('home.html',result=result,result1=result1,result2=result2)



    return render_template('fill.html',form=form)


@app.route("/about")
def about():
    return render_template('about.html',title='About')


@app.route("/home")
def home():
    return render_template('home.html',result=result,result1=result1,result2=result2)



if __name__ == '__main__':
    app.run(debug=True)
