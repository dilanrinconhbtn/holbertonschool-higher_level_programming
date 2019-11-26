-- Script that lists all the cities that have california
SELECT id, name -- List all citys
FROM cities
-- filter only citys of California
WHERE state_id = (
SELECT id FROM states WHERE name = "California");
