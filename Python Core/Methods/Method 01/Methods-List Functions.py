l1=[1,2,3,4,5]
l2=[7,8,9,10]
l1.append(6)
l1.extend(l2)
print(l1)
print(l2)

l3=["Surya","Lokesh","Shiva"]
def fun(x):
    return len(x)
l3.sort(key=fun,reverse=True)
print(l3)