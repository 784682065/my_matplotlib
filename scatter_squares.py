import matplotlib.pyplot as plt

# x_values = [1,1.1, 2, 3, 4, 5]
# y_values = [1,1.41, 4, 9, 16, 25]
x_values = list(range(1001))
y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values,
#             edgecolors='none',
#             s=4)

plt.scatter(x_values, y_values,
            cmap=plt.cm.Blues,
            edgecolor='none', s=40)
# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()
