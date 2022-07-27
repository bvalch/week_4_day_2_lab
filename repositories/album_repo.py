from database.run_sql import run_sql
from models.album import Album


def save(album):
    sql = " INSERT INTO albums (title,genre,artist_id) VALUES (%s,%s,%s) RETURNING 'id' "
    values=[album.title, album.genre, album.artist.id]
    run_sql(sql,values)

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)
    
def find_by_id(id):
    sql = "SELECT * FROM albums WHERE id=%s"
    values=[id]
    results=run_sql(sql,values)
    album_found=Album(results['title'], results['genre'], results['artist'])
    return album_found

def list_all():
    sql="SELECT * FROM albums"
    result=run_sql(sql)
    return result