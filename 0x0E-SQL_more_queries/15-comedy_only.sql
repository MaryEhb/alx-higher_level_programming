-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres ON tv_shows_genre.show_id =  tv_shows.id
JOIN tv_genres ON tv_shows_genre.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title asc;
