WITH rows_table
     AS (SELECT customfield_publicationid,
                customfield_pagenum,
                timestamp,
                Row_number()
                  OVER (
                    ORDER BY timestamp) AS row_id
         FROM   events)
SELECT t1.customfield_publicationid,
       t1.customfield_pagenum,
       Timestampdiff(second, t1.timestamp, t2.timestamp) AS ReadTime_sec
FROM   rows_table t1
       INNER JOIN rows_table t2
               ON t2.row_id = t1.row_id + 1
