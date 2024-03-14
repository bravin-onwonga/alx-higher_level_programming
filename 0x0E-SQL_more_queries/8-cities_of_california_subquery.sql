-- Lists all the cities of California that can be found in the database hbtn_0d_us
SELECT id, name
FROM cities, state
ON cities.state_id = state.id
WHERE state.name = 'California';
