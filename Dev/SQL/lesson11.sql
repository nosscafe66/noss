SELECT
    city,
    LENGTH(city)
FROM
    Station
WHERE
    LENGTH(city) =(
        SELECT
            MIN(LENGTH(city))
        FROM
            Station
    )
ORDER BY
    city ASC
LIMIT
    1;

SELECT
    city,
    LENGTH(city)
FROM
    Station
WHERE
    LENGTH(city) =(
        SELECT
            MAX(LENGTH(city))
        FROM
            Station
    );