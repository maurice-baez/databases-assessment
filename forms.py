"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms.validators import Optional, URL, InputRequired
from wtforms import SelectField, StringField, TextAreaField

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Name:",
                validators=[InputRequired()]
                )
    description = TextAreaField("Description:")


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Title:",
                validators=[InputRequired()]
                )
    artist = StringField("Artist:",
                validators=[InputRequired()]
                )


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)


class DeleteSongFromPlaylistForm(FlaskForm):
    """ Delete song from playlist form """

    song = SelectField("Song to delete", coerce=int)


class PlaylistEditForm(FlaskForm):
    """ Form for editing playlist detail """

    name = StringField("Name:",
                validators=[InputRequired()]
                )
    description = TextAreaField("Description:")
