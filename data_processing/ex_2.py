import pandas as pd

def filter_orders(df: pd.DataFrame, minValue: float, maxValue: float, sortType: bool) -> pd.DataFrame:
    order_totals = (
        df.groupby("OrderID")
          .apply(lambda x: (x["UnitPrice"] * x["Quantity"] * (1 - x["Discount"])).sum())
          .reset_index(name="Sum")
    )


    order_filtered = order_totals[
        (order_totals["Sum"] >= minValue) & (order_totals["Sum"] <= maxValue)
    ]


    order_filtered = order_filtered.sort_values(by="Sum", ascending=sortType).reset_index(drop=True)

    return order_filtered

df = pd.read_csv("../dataset/SalesTransactions/SalesTransactions.csv")

minValue = float(input("Nhập giá trị Min: "))
maxValue = float(input("Nhập giá trị Max: "))
sortType = input("Sắp xếp tăng dần? (y/n): ").lower().startswith("y")

result = filter_orders(df, minValue, maxValue, sortType)
print(result)
