from database.run_sql import run_sql
from models.artist import Artist


def save(artist):
    sql = " INSERT INTO artists (name) VALUES (%s) RETURNING id "
    values=[artist.name]
    results=run_sql(sql,values)
    artist.id=results[0]['id']
    
def delete_all():
    sql = "DELETE  FROM artists"
    run_sql(sql)
    
def find_by_id(id):
    sql="SELECT * FROM artists WHERE id= %s"
    values=[id]
    results=run_sql(sql,values)
    artist_found=Artist(results['name'])
    return artist_found

def list_all():
    sql="SELECT * FROM artists"
    results= run_sql(sql)
    return results
