import duckdb
import pandas as pd
import numpy as np
import os
from datetime import datetime, date, timedelta
import time
con_memory = duckdb.connect(database=':memory:')


con_memory.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        department VARCHAR,
        salary DECIMAL(10, 2),
        hire_date DATE,
        is_active BOOLEAN
    )
""")
print("Đã tạo bảng employees")


con_memory.execute("""
    INSERT INTO employees VALUES 
    (1, 'John Doe', 'Engineering', 75000.50, '2020-01-15', TRUE)
""")


employees_data = [
    (2, 'Jane Smith', 'Marketing', 65000.00, '2019-05-20', True),
    (3, 'Bob Johnson', 'Engineering', 85000.00, '2018-03-10', True),
    (4, 'Alice Brown', 'HR', 60000.00, '2021-02-28', True),
    (5, 'Charlie Wilson', 'Engineering', 90000.00, '2017-08-05', False)
]
con_memory.executemany(
    "INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)",
    employees_data
)

result = con_memory.execute("SELECT * FROM employees").fetchall()
print("Tất cả nhân viên:")
for row in result:
    print(row)

result = con_memory.execute("""
    SELECT name, department, salary 
    FROM employees 
    WHERE department = 'Engineering' AND salary > 80000
""").fetchall()
print("\nKỹ sư có lương > 80000:")
for row in result:
    print(row)
result = con_memory.execute("""
    SELECT 
        department, 
        COUNT(*) as employee_count,
        AVG(salary) as avg_salary,
        MAX(salary) as max_salary
    FROM employees
    WHERE is_active = TRUE
    GROUP BY department
    ORDER BY avg_salary DESC
""").fetchall()
print("\nThống kê theo phòng ban:")
for row in result:
    print(row)
df = con_memory.execute("SELECT * FROM employees").df()
print("DataFrame từ truy vấn:")
print(df)
new_employees = pd.DataFrame({
    'id': [6, 7],
    'name': ['Eva Green', 'Frank White'],
    'department': ['Sales', 'Engineering'],
    'salary': [70000.00, 95000.00],
    'hire_date': [date(2022, 1, 10), date(2021, 9, 15)],
    'is_active': [True, True]
})
con_memory.register('new_employees_df', new_employees)
print("Đã đăng ký DataFrame làm bảng tạm")
result = con_memory.execute("SELECT * FROM new_employees_df").fetchall()
print("\nNhân viên mới từ DataFrame:")
for row in result:
    print(row)
con_memory.execute("INSERT INTO employees SELECT * FROM new_employees_df")
print("Đã chèn dữ liệu từ DataFrame vào bảng")
df = con_memory.execute("SELECT * FROM employees").df()
print("DataFrame từ truy vấn:")
print(df)
result = con_memory.execute("SELECT * FROM employees").fetchall()
print("Tất cả nhân viên:")
for row in result:
    print(row)
sample_data = pd.DataFrame({
    'product_id': [101, 102, 103, 104],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'price': [1200.00, 25.50, 45.00, 300.00],
    'stock': [15, 100, 75, 25]
})

sample_data.to_csv('products.csv', index=False)
print("Đã tạo file products.csv")

result = con_memory.execute("SELECT * FROM 'products.csv' WHERE price > 100").fetchall()
print("Sản phẩm có giá > 100 từ CSV:")
for row in result:
    print(row)
con_memory.execute("CREATE TABLE products AS SELECT * FROM 'products.csv'")
print("Đã import CSV vào bảng products")
con_memory.execute("COPY (SELECT * FROM products) TO 'products.parquet' (FORMAT PARQUET)")
print("Đã xuất dữ liệu sang Parquet")
print("\nTất cả nhân viên sau khi chèn:")
result = con_memory.execute("SELECT * FROM employees").fetchall()
for row in result:
    print(row)

# Phân tích dữ liệu nhân viên
print("Phân tích dữ liệu nhân viên:")

# Tuổi làm việc (thâm niên)
result = con_memory.execute("""
    SELECT 
        name,
        department,
        salary,
        DATE_PART('year', CURRENT_DATE) - DATE_PART('year', hire_date) as years_employed,
        CASE 
            WHEN DATE_PART('year', CURRENT_DATE) - DATE_PART('year', hire_date) > 3 
            THEN salary * 0.05 
            ELSE 0 
        END as bonus
    FROM employees
    WHERE is_active = TRUE
    ORDER BY years_employed DESC
""").df()

print(result)

# Phân tích tổng quan
summary = con_memory.execute("""
    SELECT 
        COUNT(*) as total_employees,
        COUNT(CASE WHEN is_active = TRUE THEN 1 END) as active_employees,
        AVG(salary) as average_salary,
        SUM(salary) as total_salary_expense,
        MIN(hire_date) as earliest_hire,
        MAX(hire_date) as latest_hire
    FROM employees
""").fetchone()

print(f"\nTổng quan nhân viên:")
print(f"Tổng số nhân viên: {summary[0]}")
print(f"Số nhân viên đang làm: {summary[1]}")
print(f"Lương trung bình: ${summary[2]:.2f}")
print(f"Tổng chi phí lương: ${summary[3]:.2f}")
print(f"Ngày thuê sớm nhất: {summary[4]}")
print(f"Ngày thuê gần nhất: {summary[5]}")
