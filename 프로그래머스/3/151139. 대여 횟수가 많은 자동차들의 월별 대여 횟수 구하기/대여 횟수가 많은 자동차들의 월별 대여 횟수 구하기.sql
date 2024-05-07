WITH a AS (
    SELECT car_id, MONTH(START_DATE) AS MONTH
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE YEAR(START_DATE) = 2022 AND (MONTH(START_DATE) BETWEEN 8 AND 10)
), b as (
    select car_id
    from a
    group by car_id
    having count(*) >= 5
)

SELECT a.MONTH, a.car_id, count(*) as RECORDS
FROM a join b on a.car_id = b.car_id
group by concat(a.car_id, '-', a.MONTH)
order by a.month asc, a.car_id desc