-- 8. Names of people who starred in Toy Story
SELECT name FROM people JOIN stars, movies ON people.id = stars.person_id AND movies.id = stars.movie_id WHERE title = "Toy Story"
