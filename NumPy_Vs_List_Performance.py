import numpy as np
import random
import time
import matplotlib.pyplot as plt

t_list =[]
t_array=[]
for j in range(10,101):
    list_a =[]
    list_b =[]
    list_c =[]
    for i in range(j):
        list_a.append(random.randint(1,100))
        list_b.append(random.randint(1,100))
    start1= time.time()
    for i in range(len(list_a)):
        list_c.append(list_a[i]+list_b[i])
    end1 = time.time()
    t_list.append(end1-start1)
    array_a = np.array(list_a)
    array_b = np.array(list_b)
    start2 = time.time() 
    array_c = np.add(array_a, array_b)
    end2 = time.time()
    t_array.append(end2-start2)
    
x = [i for i in range(10,101)]
plt.title('Performance',fontsize=20)
plt.plot(x,t_list, color = 'b', label='List')
plt.plot(x,t_array, color = 'orange', label='NumPy Array')
plt.xlabel('Number of Elements', fontsize=10)
plt.ylabel('Execution Time', fontsize=10)
plt.legend()
plt.show()
