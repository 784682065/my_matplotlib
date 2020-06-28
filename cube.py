import matplotlib.pyplot as plt



def method1():
    x_values = [1,2,3,4,5]
    y_values = [1,8,27,64,125]

    plt.title('method1',fontsize=24)
    plt.ylabel('y_values',fontsize=14)
    plt.xlabel('x_values',fontsize=14)

    plt.scatter(x_values,y_values,s=100)
    plt.show()

def method2():
    x_values = list(range(1001))
    y_values = [x**3 for x in x_values]


    plt.title('method2',fontsize=24)
    plt.ylabel('y_values',fontsize=14)
    plt.xlabel('x_values',fontsize=14)

    plt.scatter(x_values, y_values, s=100)
    plt.show()

method1()