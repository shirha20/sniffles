//draw a piechart using matplotlib
import matplotlib.pyplot as plt
x = [10,20,30,40]
plt.pie(x)
plt.show()

//labling the piechart
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
plt.pie(x,labels = y)
plt.show()

//using explode with piechart
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
ex = [0.4,0.0,0.0,0.0]
plt.pie(x,labels = y,explode = ex)
plt.show()

//adding shadow to piechart
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
ex = [0.4,0.0,0.0,0.0]
plt.pie(x,labels = y,explode = ex,shadow = true)
plt.show()

//adjusting the radius
import matplotlib.pyplot as plt
x = [10,20,30,40]
y = ["c","c++","java","python"]
ex = [0.4,0.0,0.0,0.0]
plt.pie(x,labels = y,explode = ex,radius = 1.5)
plt.show()


