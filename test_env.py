import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 打印版本号
print(f"pandas版本: {pd.__version__}")
print(f"numpy版本: {np.__version__}")

# 创建一个简单的数据
data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)

# 保存为CSV
df.to_csv('test_data.csv', index=False)
print("数据已保存为 test_data.csv")

# 画图（不显示，只保存）
plt.figure()
plt.plot(df['x'], df['y'])
plt.savefig('test_plot.png')
print("图已保存为 test_plot.png")