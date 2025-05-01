/* Write your T-SQL query statement below */
SELECT  transaction_date
    ,   odd_sum =   SUM(
            CASE    WHEN T1.amount % 2 = 1  THEN T1.amount
                    ELSE 0
            END
        )
    ,   even_sum =   SUM(
            CASE    WHEN T1.amount % 2 = 0  THEN T1.amount
                    ELSE 0
            END
        )
FROM    transactions T1
GROUP BY
        T1.transaction_date
ORDER BY
        T1.transaction_date ASC