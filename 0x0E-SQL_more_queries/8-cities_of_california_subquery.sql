-- Lists all the cities of California that can be found in the database hbtn_0d_us
SELECT id, name
FROM cities, state
WHERE state.name = 'Carlifonia'
AND cities.state_id = state.id;
