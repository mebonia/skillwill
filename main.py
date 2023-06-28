#N1
strings = []
for i in range(5):
    string = input('შეიყვანეთ სტრიქონი:')
    strings.append(string)

max_len = 0
for string in strings:
    if len(string) > max_len:
        max_len = len(string)

print("ყველაზე გრძელი სტრიქონის სიგრძეა: ", max_len)

# N2
def find_max(nums):
    max_value = nums[0]

    for number in nums:
        if number > max_value:
            max_value = number
    return max_value


list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
maximum = find_max(list)
print('მაქსიმალურია', maximum)

# N3
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
num= int(input('შეიყვანეთ რიცხვი:'))
result = factorial(num)
print(num, 'ის ფაქტორიალი არის:', result)
