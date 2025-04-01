# Write your MySQL query statement below
SELECT  T1.stock_name
    ,   SUM(
    CASE    WHEN T1.operation = 'Buy'   THEN -1
            WHEN T1.operation = 'Sell'  THEN +1
            ELSE 0
    END
    *
    T1.price
)   AS capital_gain_loss
FROM    Stocks T1
GROUP BY
        T1.stock_name
ORDER BY
        capital_gain_loss   DESC