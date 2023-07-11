
# This simulates dividing students evenly into two classes

students = int(input("How many students are there?"))

a = [0.5, 0.5]

numberItem = students
remainder = numberItem

b = [0,0]

for i in range(0,2):
    b[i] = round(a[i]*numberItem)
    if (b[i] > remainder) or (b[i] == 0):
        b[i] = remainder
        remainder = 0
    else:
            remainder = remainder - b[i]
    print(b[i])
print("The above figures show how many students will be in each class")