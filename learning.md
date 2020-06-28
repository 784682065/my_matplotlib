
### 1. plot() 绘制折线图 
label 参数代表该线名称
plt.title() 方法代表该图名称
plt.show() 展示该图

### 2. bar() 绘制柱形图
color 参数代表 绘制颜色 g代表green (颜色英语单词首字母)

### 3. hist() 绘制直方图
rwidth 属性表示 宽度大小

### 4. scatter() 绘制散点图

### 5. stackplot 绘制堆叠图
堆叠图用于显示部分对整体随时间得到关系
plt.plot([], [], color='m', label='Sleeping', linewidth=5) 可用于标记堆叠部分的含义

### 6. pie() 绘制饼图

```
plt.pie(slices,
        labels=activities,
        colors=cols,
        shadow=True,
        explode=(0, 0.1, 0, 0),  # 哪个为0.1 就拉出哪个饼
        autopct='%1.1f%%')  # 出现百分比
```

### 7.使用csv 或者 numpy 读取本地数据

```python
with open('example.txt', 'r') as csvfile:
     polts = csv.reader(csvfile, delimiter=',')
     for row in polts:
         x.append(int(row[0]))
         y.append(int(row[1]))
```
```python
np.loadtxt('example.txt', delimiter=',', unpack=True)
```
