import matplotlib.pyplot as plt
import csv
import numpy as np

# 折线图
# plt.plot([1, 2, 3], [5, 7, 4])
# plt.plot([1, 2, 3], [10, 14, 12])
# plt.legend()
# plt.show()

# 条形图
# plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2],
#         label="Example one", color='y')
#
# plt.bar([2, 4, 6, 8, 10], [8, 6, 7, 8, 2],
#         label="Example two")
# plt.show()

# 直方图
# population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65,
#                    54, 44, 43, 42, 48]
# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
# plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()

# 堆叠图
# days = [1, 2, 3, 4, 5]
# sleeping = [7, 8, 6, 11, 7]
# eating = [2, 3, 4, 3, 2]
# working = [7, 8, 7, 2, 2]
# playing = [8, 5, 7, 8, 13]
#
# """用于标记堆叠部分的含义"""
# plt.plot([], [], color='m', label='Sleeping', linewidth=5)
# plt.plot([], [], color='c', label='Eating', linewidth=5)
# plt.plot([], [], color='r', label='Working', linewidth=5)
# plt.plot([], [], color='k', label='Playing', linewidth=5)
#
# # plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\n Check it out')
# plt.legend()  # 不加legend 则标签无法显示
# plt.show()

# 饼图
# slices = [7, 2, 2, 13]
# activities = ['Sleeping', 'eating', 'working', 'playing']
# cols = ['c', 'm', 'r', 'b']
#
# plt.pie(slices,
#         labels=activities,
#         colors=cols,
#         shadow=True,
#         explode=(0, 0.1, 0, 0),  # 哪个为0.1 就拉出哪个饼
#         autopct='%1.1f%%')  # 出现百分比
# plt.title('Interesting Graph \nCheck it out')
# plt.show()


# 从文件中读取数据 绘制折线图
#
# x = []
# y = []
#
# with open('example.txt', 'r') as csvfile:
#     polts = csv.reader(csvfile, delimiter=',')
#     for row in polts:
#         x.append(int(row[0]))
#         y.append(int(row[1]))
#
# plt.plot(x, y, label='Loaded from file!')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()

# 使用numpy 读取数据

# x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
# plt.plot(x, y, label='Loaded from file!')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Interesting Graph\nCheck it out')
# plt.legend()
# plt.show()
