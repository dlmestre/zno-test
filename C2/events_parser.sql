WITH ntable
     AS (SELECT customfield_publicationid    AS CustomField_PublicationId,
                customfield_pagenum          AS CustomField_PageNum,
                Min(timestamp)               AS dt,
                Row_number()
                  OVER (
                    ORDER BY Min(timestamp)) AS RowNum
         FROM   events
         GROUP  BY timestamp,
                   customfield_publicationid,
                   customfield_pagenum)
SELECT t1.customfield_publicationid        AS CustomField_PublicationId,
       t1.customfield_pagenum              AS CustomField_PageNum,
       Timestampdiff(second, t1.dt, t2.dt) AS Elapsed
FROM   ntable t1
       INNER JOIN ntable t2
               ON t2.rownum = t1.rownum + 1
