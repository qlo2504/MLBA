import pandas as pd

def top3_highest_value_products(df: pd.DataFrame) -> pd.DataFrame:
    product_value = (
        df.groupby("ProductID")
          .apply(lambda x: (x["UnitPrice"] * x["Quantity"] * (1 - x["Discount"])).sum())
          .reset_index(name="TotalValue")
    )
    top3 = (
        product_value.sort_values(by="TotalValue", ascending=False)
                     .head(3)
                     .reset_index(drop=True)
    )
    return top3
df = pd.read_csv("../dataset/SalesTransactions/SalesTransactions.csv")
result = top3_highest_value_products(df)
print(result)
