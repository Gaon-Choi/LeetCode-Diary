/* Write your T-SQL query statement below */
SELECT  id
    ,   Jan_Revenue =   SUM(CASE WHEN T1.month = 'Jan' THEN T1.revenue END)
    ,   Feb_Revenue =   SUM(CASE WHEN T1.month = 'Feb' THEN T1.revenue END)
    ,   Mar_Revenue =   SUM(CASE WHEN T1.month = 'Mar' THEN T1.revenue END)
    ,   Apr_Revenue =   SUM(CASE WHEN T1.month = 'Apr' THEN T1.revenue END)
    ,   May_Revenue =   SUM(CASE WHEN T1.month = 'May' THEN T1.revenue END)
    ,   Jun_Revenue =   SUM(CASE WHEN T1.month = 'JUn' THEN T1.revenue END)
    ,   Jul_Revenue =   SUM(CASE WHEN T1.month = 'Jul' THEN T1.revenue END)
    ,   Aug_Revenue =   SUM(CASE WHEN T1.month = 'Aug' THEN T1.revenue END)
    ,   Sep_Revenue =   SUM(CASE WHEN T1.month = 'Sep' THEN T1.revenue END)
    ,   Oct_Revenue =   SUM(CASE WHEN T1.month = 'Oct' THEN T1.revenue END)
    ,   Nov_Revenue =   SUM(CASE WHEN T1.month = 'Nov' THEN T1.revenue END)
    ,   Dec_Revenue =   SUM(CASE WHEN T1.month = 'Dec' THEN T1.revenue END)
FROM    Department T1
GROUP BY
        T1.id