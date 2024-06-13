-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT `city`, AVG(`value`) AS `avgtemp` FROM `temperatures` GROUP BY `city` ORDER BY `avgtemp` DESC;
