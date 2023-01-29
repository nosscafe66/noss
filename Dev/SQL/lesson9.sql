select
  distinct CITY,
  (count(*) - count(CITY)) as cnt
from
  STATION