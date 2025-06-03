# Write your MySQL query statement below
SELECT  T1.book_id
    ,   T1.title
    ,   T1.author
    ,   T1.genre
    ,   T1.publication_year
    ,   COUNT(*)  AS current_borrowers
FROM    library_books AS T1
JOIN    borrowing_records AS T2
    ON  T2.book_id  =   T1.book_id
    AND T2.return_date  IS NULL
GROUP BY
        T1.book_id
    ,   T1.total_copies
HAVING   T1.total_copies - COUNT(*) = 0
ORDER BY
        current_borrowers   DESC
    ,   T1.title            ASC