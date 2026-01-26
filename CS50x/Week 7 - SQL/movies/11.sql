-- 11. Titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated
SELECT title FROM movies m
    JOIN stars s ON s.movie_id = m.id
    JOIN people p ON s.person_id =  p.id
    JOIN ratings r ON r.movie_id = m.id
WHERE name = "Chadwick Boseman"
ORDER BY rating DESC
LIMIT 5;
