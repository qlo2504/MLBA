from numpy import nan as NA
import pandas as pd

data=pd.DataFrame([[1.,6.5,3.],
                   [1.,NA,NA],
                   [NA,NA,NA],
                   [NA,6.5,3.]])
print(data)
print("-"*50)
cleaned=data.dropna() #Có NA là bỏ
print(cleaned)
print("-"*50)
cleaned2=data.dropna(how='all') #Tất cả giá trị là NA mới bỏ
print(cleaned2)

