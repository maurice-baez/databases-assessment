from pydoc import HTMLRepr
from unittest import TestCase

from app import app, db
from models import Playlist, Song, PlaylistSong

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///playlists_test"

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

app.config['WTF_CSRF_ENABLED'] = False

db.drop_all()
db.create_all()


##############################################################################
# Playlist tests

class PlaylistViewTestCase(TestCase):
    """Test views for playlists """

    def setUp(self):
        """Create test client, add sample data."""

        PlaylistSong.query.delete()
        Playlist.query.delete()
        Song.query.delete()


        self.client = app.test_client()

        test_playlist_1 = Playlist(name="test_playlist_1",
                        description="this is just the first test playlist"
                        )
        test_playlist_2 = Playlist(name="test_playlist_2",
                        description="this is just a second test playlist"
                        )

        test_song_1 = Song(title="test_song_1", artist="test_artist_1")
        test_song_2 = Song(title="test_song_2", artist="test_artist_2")

        db.session.add_all([test_playlist_1, test_playlist_2])
        db.session.add_all([test_song_1, test_song_2])
        db.session.commit()


        ############### Add test_song_1 & 2 to test_playlist_1 #####################

        test_playlists_songs_1 = PlaylistSong(playlist_id=test_playlist_1.id, song_id=test_song_1.id)

        test_playlists_songs_2 = PlaylistSong(playlist_id=test_playlist_1.id, song_id=test_song_2.id)


        db.session.add_all([test_playlists_songs_1, test_playlists_songs_2])
        db.session.commit()

        self.playlist_id = test_playlist_1.id
        self.song_id = test_song_1.id


    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_list_playlists(self):
        """Test that playlist list displays with playlists from database"""

        with self.client as c:
            resp = c.get("/playlists")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("test_playlist_1", html)
            self.assertIn("test_playlist_2", html)
            self.assertIn("Your Playlists", html)


    def test_playlist_detail_page(self):
        """ Test that the playlist detail page for corresponding playlist and songs load correctly """

        with self.client as c:
            resp = c.get(f"/playlists/{self.playlist_id}")
            html = resp.get_data(as_text=True)

            ### check that playlist name and description populate
            self.assertEqual(resp.status_code, 200)
            self.assertIn("test_playlist_1", html)
            self.assertIn("this is just the first", html)

            ### check that songs populate for a given playlist
            self.assertIn("TRACKS", html)
            self.assertIn("test_song_1", html)
            self.assertIn("test_artist_1", html)



    def test_display_add_new_playlist_form(self):
        """Test that new playlist form is displayed"""

        with self.client as c:
            resp = c.get("/playlists/add")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form id="playslist-add-form', html)



    def test_add_new_playlist(self):
        """Test that new playlist is added to db and page redirects"""

        with self.client as c:
            resp = c.post("/playlists/add", data = {"name": "another_test_playlist",
                                             "description": "Here is the description" },
                                            follow_redirects = True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("another_test_playlist", html)
            self.assertIn("Your Playlists", html)



    def test_display_edit_playlist_form(self):
        """ Test that edit playlist form is displayed and data from db is populated in input fields """

        with self.client as c:
            resp = c.get(f"/playlists/{self.playlist_id}/edit")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form id="playslist-edit-form', html)
            self.assertIn("test_playlist_1", html)
            self.assertIn("this is just the first test playlist", html)



    def test_edit_playlist(self):
        """ Test edit playlist functionality and redirect """

        with self.client as c:
            resp = c.post(f"/playlists/{self.playlist_id}/edit",
                                data = {"name": "updated_playlist_name",
                                        "description": "updated the description"},
                                follow_redirects = True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("updated_playlist_name", html)
            self.assertIn("updated the description", html)

            ### check that old content is no lionger there
            self.assertNotIn("test_playlist_1", html)
            self.assertNotIn("just the first test playlist", html)



    def test_delete_playlist(self):
        """ Test delete playlist functiontionality and redirect """

        with self.client as c:
            resp = c.post(f"/playlists/{self.playlist_id}/delete",
                                        follow_redirects = True
                                        )
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Your Playlists", html)

            ###check that playlist is no longer there
            self.assertNotIn("test_playlist_1", html)


##############################################################################
# Song tests

class SongViewTestCase(TestCase):
    """Test views for playlists """

    def setUp(self):
        """Create test client, add sample data."""

        PlaylistSong.query.delete()
        Playlist.query.delete()
        Song.query.delete()


        self.client = app.test_client()

        test_playlist_1 = Playlist(name="test_playlist_1",
                        description="this is just the first test playlist"
                        )
        test_playlist_2 = Playlist(name="test_playlist_2",
                        description="this is just a second test playlist"
                        )

        test_song_1 = Song(title="test_song_1", artist="test_artist_1")
        test_song_2 = Song(title="test_song_2", artist="test_artist_2")
        test_song_3 = Song(title="test_song_3", artist="test_artist_3")

        db.session.add_all([test_playlist_1, test_playlist_2])
        db.session.add_all([test_song_1, test_song_2, test_song_3])
        db.session.commit()


        ############### Add test_song_1 & 2 to test_playlist_1 #####################

        test_playlists_songs_1 = PlaylistSong(playlist_id=test_playlist_1.id, song_id=test_song_1.id)

        test_playlists_songs_2 = PlaylistSong(playlist_id=test_playlist_1.id, song_id=test_song_2.id)


        db.session.add_all([test_playlists_songs_1, test_playlists_songs_2])
        db.session.commit()

        self.playlist_id = test_playlist_1.id
        self.song_id = test_song_1.id
        self.song_3_id = test_song_3.id


    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()



    def test_list_songs(self):
        """Test that songs list displays with songs from db """

        with self.client as c:
            resp = c.get("/songs")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)

            self.assertIn("The Song List", html)
            self.assertIn("test_song_1", html)
            self.assertIn("test_song_2", html)


    def test_song_detail_page(self):
        """ Test that the song detail page and "appears on playlist" section loads correctly """

        with self.client as c:
            resp = c.get(f"/songs/{self.song_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)

            ### check that song name and artist display
            self.assertIn("test_song_1", html)
            self.assertIn("test_artist_1", html)

            ### check that playlists populate for a given song
            self.assertIn("appears on:", html)
            self.assertIn("test_playlist_1", html)


    def test_display_add_new_song_form(self):
        """Test that new song form is displayed"""

        with self.client as c:
            resp = c.get("/songs/add")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form id="song-add-form', html)



    def test_add_new_song(self):
        """Test that new song is added to db and page redirects"""

        with self.client as c:
            resp = c.post("/songs/add", data = {"title": "another_test_song",
                                             "artist": "another_test_artist"},
                                            follow_redirects = True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)

            self.assertIn("The Song List", html)
            self.assertIn("another_test_song", html)
            self.assertIn("another_test_artist", html)



    def test_add_new_song_to_playlist_form(self):
        """ Test the add new song to playlist form displays with test_song_3 as an option (song not currently on  playlist) """

        with self.client as c:
            resp = c.get(f"/playlists/{self.playlist_id}/add-song")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form id="add-song-to-playlist-form', html)
            self.assertIn("test_song_3", html)



    def test_add_new_song_to_playlist(self):
        """ Test adding new song to playlist and redirect """

        with self.client as c:
            resp = c.post(f"/playlists/{self.playlist_id}/add-song",
                                            data =
                                            {"playlist_id": f"{self.playlist_id}" , "song": f"{self.song_3_id}"
                                            },
                                            follow_redirects = True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)

            self.assertIn("TRACKS", html)
            self.assertIn("test_song_3", html)
            self.assertIn("test_artist_3", html)



##############################################################################
# Error handling tests

    def test_error_handling_from_unknown_playlist(self):
        """ Test 404 error handling """

        with self.client as c:
            resp = c.get("/playlilsts/dsknfdgkldsmkdmk")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 404)
            self.assertIn('<div class="fof', html)
            self.assertIn("Page not found...", html)


    def test_error_handling_from_unknown_song(self):
        """ Test 404 error handling """

        with self.client as c:
            resp = c.get("/songs/dsknfdgkldsmkdmk")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 404)
            self.assertIn('<div class="fof', html)
            self.assertIn("Page not found...", html)