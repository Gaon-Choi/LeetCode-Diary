/* Write your T-SQL query statement below */
SELECT  name        = T1.name
    ,   balance     = T2.balance
FROM    Users T1
JOIN    (
    SELECT  account
        ,   balance =   SUM(ISNULL(TT1.amount, 0))
    FROM    Transactions TT1
    GROUP BY
            TT1.account
) T2
    ON  T2.account  =   T1.account
WHERE   T2.balance  > 10000