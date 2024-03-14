-- Lists all the cities of California that can be found in the database hbtn_0d_us
SELECT cities.id, cities.name
FROM cities, states
ON cities.state_id = states.id
WHERE states.name = 'California';
