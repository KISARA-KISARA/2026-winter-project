import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 打印Hello Python
print("Hello Python from KISARA")

# 2. 创建简单数据
data = {'x': np.arange(1, 6), 'y': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)

# 3. 打印数据
print(df)

# 4. 画折线图
plt.figure()
plt.plot(df['x'], df['y'], marker='o')
plt.title("Hello Python Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("kaggle_t1_plot.png")
print("图已保存为 kaggle_t1_plot.png")