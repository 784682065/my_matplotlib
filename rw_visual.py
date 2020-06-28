import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues,
                edgecolor='none', s=1)
    # plt.plot(rw.x_values, rw.y_values,linewidth =5)

    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    #             s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make anther walk ?(y/n): ")
    if keep_running == 'n':
        break