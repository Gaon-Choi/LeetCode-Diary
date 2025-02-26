SELECT  T1.firstName    AS 'firstName'
    ,   T1.lastName     AS 'lastName'
    ,   T2.city         AS 'city'
    ,   T2.state        AS 'state'
FROM    Person T1
LEFT JOIN    Address T2
    ON  T2.personId    = T1.personId