"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """ Playlist """

    __tablename__ = "playlists"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False
                     )
    description = db.Column(db.String,
                        nullable=False,
                        default=""
                        )

    songs = db.relationship('Song',
                               secondary='playlists_songs',
                               backref='playlists')


    def __repr__(self):
        """Return playlist data"""

        pl = self

        return f"<Id {pl.id} Name {pl.name} Description {pl.description}>"




class Song(db.Model):
    """ Song """

    __tablename__ = "songs"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(50),
                     nullable=False
                     )
    artist = db.Column(db.String(50),
                        nullable=False
                        )


    def __repr__(self):
        """ Return song data """

        s = self

        return f"<Id {s.id} Title {s.title} Artist {s.artist}>"



class PlaylistSong(db.Model):
    """ Mapping of a playlist to a song """

    __tablename__ = "playlists_songs"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    playlist_id = db.Column(db.Integer,
                    db.ForeignKey("playlists.id"),
                    nullable=False
                    )
    song_id = db.Column(db.Integer,
                    db.ForeignKey("songs.id"),
                    nullable=False
                    )

    def __repr__(self):
        """ Return playlists_songs """

        ps = self

        return f"<Id {ps.id} playlist_id {ps.playlist_id} song_id {ps.song_id}>"


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
