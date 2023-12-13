-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_shows
JOIN tv_genre ON tv_shows_genre.genre_id = tv_genres.id
JOIN tv_shows_genre ON tv_shows_genre.show_id =  tv_shows.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title asc;
