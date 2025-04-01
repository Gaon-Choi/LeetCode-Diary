# Write your MySQL query statement below
SELECT  T1.sample_id
    ,   T1.dna_sequence
    ,   T1.species
    ,   CASE    WHEN T1.dna_sequence LIKE 'ATG%' THEN 1
                ELSE 0
        END     AS has_start
    ,   CASE    WHEN T1.dna_sequence LIKE '%TAA' THEN 1
                WHEN T1.dna_sequence LIKE '%TAG' THEN 1
                WHEN T1.dna_sequence LIKE '%TGA' THEN 1
                ELSE 0
        END     AS has_stop
    ,   CASE    WHEN T1.dna_sequence LIKE '%ATAT%' THEN 1
                ELSE 0
        END     AS has_atat
    ,   CASE    WHEN T1.dna_sequence LIKE '%GGG%' THEN 1
                ELSE 0
        END     AS has_ggg
FROM    Samples T1
ORDER BY
        T1.sample_id    ASC