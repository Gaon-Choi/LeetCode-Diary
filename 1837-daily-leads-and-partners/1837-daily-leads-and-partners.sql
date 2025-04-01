SELECT  date_id
    ,   make_name
    ,   COUNT(DISTINCT T1.lead_id)      AS unique_leads
    ,   COUNT(DISTINCT T1.partner_id)   AS unique_partners
FROM    DailySales T1
GROUP BY
        T1.date_id
    ,   T1.make_name