# Write your MySQL query statement below
SELECT  DATE_FORMAT(T1.trans_date, '%Y-%m')                             AS month
    ,   T1.country                                                      AS country
    ,   COUNT(*)                                                        AS trans_count
    ,   SUM(CASE WHEN T1.state = 'approved' THEN 1 ELSE 0 END)          AS approved_count
    ,   SUM(T1.amount)                                                  AS trans_total_amount
    ,   SUM(CASE WHEN T1.state = 'approved' THEN T1.amount ELSE 0 END)  AS approved_total_amount
FROM    Transactions T1
GROUP BY
        DATE_FORMAT(T1.trans_date, '%Y-%m')
    ,   T1.country