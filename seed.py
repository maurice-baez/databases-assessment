from models import Playlist, Song, PlaylistSong, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Playlist.query.delete()
Song.query.delete()
PlaylistSong.query.delete()

# Add playlists
playlist_1 = Playlist(name='Jamz!', description="This playlist has all the hot jamzzzz!")
playlist_2 = Playlist(name='Hit List')
playlist_3 = Playlist(name='Summer Soundz', description='Songs to set your summer off right')

# Add songs

song_1 = Song(title="Here Comes The Sun", artist="The Beatles")
song_2 = Song(title="Valerie", artist="Amy Winehouse")
song_3 = Song(title="Whip It", artist="Devo")
song_4 = Song(title="Ice Ice Baby", artist="Vanilla Ice")
song_5 = Song(title="Purple Haze", artist="Jimi Hendrix")
song_6 = Song(title="Everlong", artist="Foo Fighters")
song_7 = Song(title="Angie", artist="The Rolling Stones")
song_8 = Song(title="Even Flow", artist="Pearl Jam")
song_9 = Song(title="High and Dry", artist="Radiohead")
song_10 = Song(title="All Along the Watchtower", artist="Bob Dylan")
song_11 = Song(title="Uprising", artist="Muse")
song_12 = Song(title="Blank Space", artist="Taylor Swift")
song_13 = Song(title="Tom Sawyer", artist="Rush")
song_14 = Song(title="Faithfully", artist="Journey")
song_15 = Song(title="Rich Girl", artist="Hall and Oates")


# Add new objects to session, so they'll persist
db.session.add_all([playlist_1, playlist_2, playlist_3])
db.session.add_all([song_1, song_2, song_3, song_4, song_5,
                    song_6, song_7, song_8, song_9, song_10,
                    song_11, song_12, song_13, song_14, song_15
                    ])

db.session.commit()


#Populate plasylists_songs table

playlists_songs_1 = PlaylistSong(playlist_id = playlist_1.id, song_id = song_1.id)
playlists_songs_2 = PlaylistSong(playlist_id = playlist_1.id, song_id = song_2.id)
playlists_songs_3 = PlaylistSong(playlist_id = playlist_1.id, song_id = song_3.id)
playlists_songs_4 = PlaylistSong(playlist_id = playlist_1.id, song_id = song_4.id)
playlists_songs_5 = PlaylistSong(playlist_id = playlist_1.id, song_id = song_5.id)
playlists_songs_6 = PlaylistSong(playlist_id = playlist_2.id, song_id = song_6.id)
playlists_songs_7 = PlaylistSong(playlist_id = playlist_2.id, song_id = song_7.id)
playlists_songs_8 = PlaylistSong(playlist_id = playlist_2.id, song_id = song_8.id)
playlists_songs_9 = PlaylistSong(playlist_id = playlist_2.id, song_id = song_9.id)
playlists_songs_10 = PlaylistSong(playlist_id = playlist_2.id, song_id = song_10.id)
playlists_songs_11 = PlaylistSong(playlist_id = playlist_3.id, song_id = song_11.id)
playlists_songs_12 = PlaylistSong(playlist_id = playlist_3.id, song_id = song_12.id)
playlists_songs_13 = PlaylistSong(playlist_id = playlist_3.id, song_id = song_13.id)
playlists_songs_14 = PlaylistSong(playlist_id = playlist_3.id, song_id = song_14.id)
playlists_songs_15 = PlaylistSong(playlist_id = playlist_3.id, song_id = song_15.id)
playlists_songs_16 = PlaylistSong(playlist_id = playlist_1.id, song_id = song_15.id)
playlists_songs_17 = PlaylistSong(playlist_id = playlist_1.id, song_id = song_14.id)
playlists_songs_18 = PlaylistSong(playlist_id = playlist_1.id, song_id = song_13.id)
playlists_songs_19 = PlaylistSong(playlist_id = playlist_2.id, song_id = song_1.id)
playlists_songs_20 = PlaylistSong(playlist_id = playlist_2.id, song_id = song_2.id)
playlists_songs_21 = PlaylistSong(playlist_id = playlist_2.id, song_id = song_3.id)
playlists_songs_22 = PlaylistSong(playlist_id = playlist_3.id, song_id = song_4.id)
playlists_songs_23 = PlaylistSong(playlist_id = playlist_3.id, song_id = song_5.id)
playlists_songs_24 = PlaylistSong(playlist_id = playlist_3.id, song_id = song_6.id)

db.session.add_all([playlists_songs_1, playlists_songs_2, playlists_songs_3,
                    playlists_songs_4, playlists_songs_5, playlists_songs_6, playlists_songs_7, playlists_songs_8, playlists_songs_9, playlists_songs_10, playlists_songs_11, playlists_songs_12, playlists_songs_13, playlists_songs_14, playlists_songs_15, playlists_songs_16, playlists_songs_17, playlists_songs_18, playlists_songs_19, playlists_songs_20, playlists_songs_21, playlists_songs_22, playlists_songs_23, playlists_songs_24
                    ])

# Commit--otherwise, this never gets saved!

db.session.commit()

