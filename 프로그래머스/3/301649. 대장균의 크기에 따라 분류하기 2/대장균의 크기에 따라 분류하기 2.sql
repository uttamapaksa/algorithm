WITH rankings AS (
  SELECT
    id,
    PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) * 100 AS ranking
  FROM ecoli_data
)

SELECT
  id,
  CASE
    WHEN ranking <= 25 THEN 'CRITICAL'
    WHEN ranking <= 50 THEN 'HIGH'
    WHEN ranking <= 75 THEN 'MEDIUM'
    ELSE 'LOW'
  END AS colony_name
FROM rankings
ORDER BY id ASC;