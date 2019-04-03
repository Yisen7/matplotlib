import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,edgecolors='none',s=40,c=y_values,cmap=plt.cm.Reds)
# 设置图表标题并给坐标轴加上标签
# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

# plt.show()
# 将所生成的图表自动保存
plt.savefig('suqares_plot.png',bbox_inchces='tight')