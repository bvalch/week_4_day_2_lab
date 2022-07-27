from black import Report
from models.album import Album
from models.artist import Artist
import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo

artist_repo.delete_all()
artist1=Artist('Michael Jackson')
artist_repo.save(artist1)

album1=Album('Thriller','Pop',artist1)

album_repo.save(album1)


results=album_repo.list_all()
print(results)
