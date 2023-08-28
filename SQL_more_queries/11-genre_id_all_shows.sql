-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id.
-- Script that lists all cities contained in the database
SELECT tv_shows.title, tv_show_genres.genre_id -- Query to join cities and states
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
