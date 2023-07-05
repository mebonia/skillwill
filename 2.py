
#N1
def min_value(dict):
    values = dict.values()
    return min(values)

dict1 = {'1' : 10, '2' : 20, '3' : 30, '4' : 40}
minimum_value = min_value(dict1)
print(minimum_value)

#N2
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
num= int(input('შეიყვანეთ რიცხვი:'))
result = factorial(num)
print(num, 'ის ფაქტორიალი არის:', result)