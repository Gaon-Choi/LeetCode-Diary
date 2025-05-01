/* Write your T-SQL query statement below */
SELECT  buyer_id        =   T1.user_id
    ,   join_date       =   T1.join_date
    ,   orders_in_2019  =   COUNT(CASE WHEN YEAR(T2.order_date) = 2019 THEN 1 END)
FROM    Users T1
LEFT JOIN    Orders T2
    ON  T2.buyer_id =   T1.user_id
GROUP BY
        T1.user_id
    ,   T1.join_date