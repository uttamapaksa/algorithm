WITH RECURSIVE Generations AS (
    -- 최초 세대 설정
    (SELECT 
        ID, 
        PARENT_ID, 
        1 AS GENERATION
    FROM 
        ECOLI_DATA
    WHERE 
        PARENT_ID IS NULL)
    UNION ALL
    -- 자식 세대 설정
    (SELECT 
        e.ID, 
        e.PARENT_ID, 
        g.GENERATION + 1 AS GENERATION
    FROM 
        ECOLI_DATA e
    INNER JOIN 
        Generations g
    ON 
        e.PARENT_ID = g.ID)
)


SELECT 
    COUNT(*) AS COUNT,
    g.GENERATION
FROM 
    Generations g
LEFT JOIN 
    ECOLI_DATA e
ON 
    g.ID = e.PARENT_ID
WHERE 
    e.ID IS NULL
GROUP BY 
    g.GENERATION
ORDER BY 
    g.GENERATION;