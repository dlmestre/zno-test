SELECT Sum(t1.readtime_sec) AS ReadingTime_sec,
       t1.publicationid,
       t3.articlename
FROM   table1 t1
       INNER JOIN table2 t2
               ON t1.pageid = t2.pageid
                  AND t1.publicationid = t2.publicationid
       INNER JOIN table3 t3
               ON t2.articleid = t3.articleid
GROUP  BY t1.publicationid,
          t3.articlename
