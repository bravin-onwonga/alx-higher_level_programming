-- Lists all the cities of California that can be found in the database hbtn_0d_us
SELECT DISTINCT cities.state_id, cities.name
FROM cities, states
WHERE cities.state_id = (
	SELECT states.id
	FROM states
	WHERE states.name = 'California'
);
