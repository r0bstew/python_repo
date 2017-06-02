# python_repo


<p align="center">
test. <br/>



Testing how SQL statements look:
```sql
SELECT * FROM ids_client_property_map;
```

```sql
SELECT * 
  FROM ids_client_property_map icpm 
  INNER JOIN property_client pc ON (icpm.oid_property_client = pc.oid_property_client)
  WHERE pc.oid_property_client > 0
  GROUP BY pc.oid_property_client
  ORDER BY icpm.property_name ASC
  LIMIT 10;
```
