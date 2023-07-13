#python list
                #0      #1        #2        #3
fruitbasket = ['apple','banana','cherry','mango']
print(fruitbasket[0]) #indice
print(fruitbasket[3])
print(fruitbasket[2])  

print(len(fruitbasket))

fruitbasket.append("watermelon")
fruitbasket.remove("cherry")
for fruit in fruitbasket:
    print (fruit)

for i in range(len(fruitbasket)):
    print(i)
    print(fruitbasket[i])

# python dictionary practice
fruitdict= {'apple':10, 'banana':3, 'watermelon':1}
#keys       #values
print (fruitdict['apple'])
print(fruitdict['banana'])
print (fruitdict.keys()) #returned a list of keys

fruitdict['coconut'] = 100

for item in fruitdict:
    
    print(str(fruitdict[item]))

for value in fruitdict.values():
    print(value)

del fruitdict['apple']

fruitlist =['apple','orange','tomato']

