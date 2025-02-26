# Write your MySQL query statement below
SELECT  patient_id
    ,   patient_name
    ,   conditions
FROM    Patients T1
WHERE   T1.conditions LIKE 'DIAB1%'
    OR  T1.conditions LIKE '% DIAB1%'
    -- REGEXP '\\bDIAB1'