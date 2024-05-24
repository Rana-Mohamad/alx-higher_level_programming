-- Uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.name
	FROM tv_genres AS g
		INNER JOIN tv_show_genres AS tv
		ON g.id = tv.genre_id

		INNER JOIN tv_shows AS s
		ON s.id = tv.show_id
		WHERE s.title = 'Dexter'
	ORDER BY g.name;
