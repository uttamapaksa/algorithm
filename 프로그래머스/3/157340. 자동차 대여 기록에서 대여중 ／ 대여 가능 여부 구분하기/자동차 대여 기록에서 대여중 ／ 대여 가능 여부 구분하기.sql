WITH B AS (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE <= DATE('2022-10-16') AND END_DATE >= DATE('2022-10-16')
)

SELECT
    A.CAR_ID,
    CASE
        WHEN A.CAR_ID IN (SELECT CAR_ID FROM B) THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY A
GROUP BY A.CAR_ID
ORDER BY A.CAR_ID DESC;