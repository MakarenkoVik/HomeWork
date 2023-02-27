from peewee import *

db = SqliteDatabase('chinook.db')


class DatabaseModel(Model):

    class Meta:
        database = db
    

class Albums(DatabaseModel):
    title = CharField(column_name = "Title")
    album_id = AutoField(column_name = "AlbumId")

    class Meta:
        table_name = 'albums'


class Tracks(DatabaseModel):
    name = CharField(column_name = "Name")
    album_id = AutoField(column_name = "AlbumId")

    class Meta:
        table_name = 'tracks'


def get_tracks_by_album(album):
    with db:
        tracks = Tracks.select().where(Tracks.album_id == Albums.select().where(Albums.title == album))
        print(tracks)
    return tracks

for track in list(get_tracks_by_album("Load")):
    print(track.name)
