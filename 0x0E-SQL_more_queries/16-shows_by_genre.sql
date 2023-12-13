-- lists all shows, and all genres linked to that show
select tv_shows.title,  tv_genres.name from tv_shows
LEFT join tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT join tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
