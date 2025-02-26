SELECT  name    AS 'Customers'
FROM    Customers T1
WHERE   T1.id   NOT IN  (
    SELECT  customerId
    FROM    Orders
)