-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tg.name AS genre, COUNT(tsg.genre_id) AS number_of_shows
FROM tv_genres AS tg
LEFT JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
GROUP BY genre
HAVING COUNT(tsg.genre_id) <> 0
ORDER BY number_of_shows DESC;
