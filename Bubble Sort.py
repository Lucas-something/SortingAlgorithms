#!/usr/bin/env python
# coding: utf-8

# In[6]:


def listMakerFunction(listLenght):
    list = []
    for i in range (0, listLenght):
        list.append(int(input("Enter your number: ")))
    return list
    
def bubbleSort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

listLenght = int(input("How many numbers do you want to add to the list? "))

print(bubbleSort(listMakerFunction(listLenght)))




# In[ ]:





# In[ ]:




