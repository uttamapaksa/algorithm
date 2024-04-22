SELECT COUNT(*) AS COUNT
FROM ecoli_data
WHERE NOT genotype & 2 AND (genotype & 1 || genotype & 4);