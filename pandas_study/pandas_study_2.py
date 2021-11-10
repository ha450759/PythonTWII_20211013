import pandas as pd
import matplotlib.pyplot as plt
# Series 是一個類似陣列的物件(一維陣列)
# 建立 Series 物件: 使用 list
#s = pd.Series([4, 7, -5, 3]) # 預設的 index = 0, 1, 2, 3
#s = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
date = pd.date_range('20211101', periods=4)
s = pd.Series([4, 7, -5, 3], index=date)
print(s)
plt.plot(s.index, s.values, '-')
plt.title('my series chart')
plt.xlabel('date')
plt.grid(True) # 格狀
plt.show()