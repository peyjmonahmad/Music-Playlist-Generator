# Music-Playlist-Generator

This repository entails generating music playlists based off lyrical and audio similarities between songs.  Playlists were created among the genres of hip hop/rap, country, R&B/soul, and rock music.  The main process of this project can be followed throughout the jupyter notebook (.ipynb) file of this repository.  

It took a few simple steps to register for a Spotify API developer's account and reap the benefits of all artist information, album information, and track information.  For major artists across these genres, I retrieved track infromation from their three latest albums, as well as key audio features of those respective songs.  To get full lyrics of all these songs, I utilized the PyLyrics library in python. 

Once all the song lyrics undergoed pre-processing and lemmatization, it was ready for topic modeling.  The lyrics were transformed into a feature vector space, and fitted into a Latent Dirichlet Allocation (LDA) model.  The model was able to learn major topics that were consistent throughout songs, which gave a general view about lyrical details.  To really understand the meaning behind lyrics, I performed Word2Vec context modeling on all words in the corpus, and ended up with average feature vectors for each song.

With all the data transformed into Word2Vec feature vectors, I performed Nearest Neighbors to calculate the shortest cosine distances between every song.  I found the 10 closest lyrical neighbors for each song, and considered that a playlist.  This technique was also performed on audio features, which was much simpler to numerical nature of the data.  Lastly, I combined both lyrical and audio arrays to construct a combined playlist.  Ultimately, if you type in an artist and song into my generator, it will give you three unique playlists to listen too!

To try this out on your own, you can check out my Flask web application that encapsulates all of this work into a responsive web page.  This public page should be up and running shortly.

Note: Only songs that were in an artist's last three albums were retrieved.  Also, songs that were not available in the python PyLyrics library were excluded from the project, but thousands of well known songs per genre are present in the dataset.
