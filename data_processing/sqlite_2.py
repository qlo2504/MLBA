import sqlite3
import pandas as pd


n = int(input("Nhập số lượng invoice tối thiểu: "))


conn = sqlite3.connect("../databases/Chinook_Sqlite.sqlite")

query = """
SELECT 
    c.CustomerId,
    c.FirstName,
    c.LastName,
    COUNT(i.InvoiceId) AS InvoiceCount,
    SUM(i.Total) AS TotalAmount
FROM Customer c
JOIN Invoice i
    ON c.CustomerId = i.CustomerId
GROUP BY 
    c.CustomerId,
    c.FirstName,
    c.LastName
HAVING 
    COUNT(i.InvoiceId) >= ?
ORDER BY 
    TotalAmount DESC;
"""


df = pd.read_sql_query(query, conn, params=(n,))
print(df)

conn.close()
