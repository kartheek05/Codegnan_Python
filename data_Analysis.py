'''
Data Analysis:
Why this is need 
---> This is crutial because it converts raw dat aintoo actionable insights, enabling information to making decisions easy. 
It also improve operational efficiency 

1.Decision Making 
2.Improved Operational Efficiency
3.Customer Understanding
4.Market Insights
5.Risk Management
6.Data-Driven Strategies


Line Plot:
import matplotlib.pyplot as pit
x = [1,2,3,4]
y = [10,85,50,90]
pit.plot(x,y)
pit.show()

Bar Graph:
import matplotlib.pyplot as pit
pit.bar(["A","B","C"],[9,7,5])
pit.show()

Pie Graph:
import matplotlib.pyplot as pit
pit.pie([30,40,20,23],labels=["Surya","Kartheek","Roy","Raju"])
pit.show()

Histogram:
import matplotlib.pyplot as pit
pit.hist([23,4,78,9])
pit.show()
'''
'''
Numpy(Numerical Pyhton) 
---->is the foundational open-source library for scientific computing in pyhton, providing high-performance, N-dimensional array objects(ndarray).
---->This enables efficient numerical computation linear algebra, and data manipulation, serving as the basis for tools like Tensorflow and scipy
import numpy as kk
arr = kk.array([1,2,3])
print(arr-1)

Pandas
-->This is used for handling structured data in table format
'''
import pandas as kk
data = {"naem":["Kartheek","Teja"],"Marks":[89,90]}
any = kk.DataFrame(data)
print(any)