

num = int(input("Enter the No Of T: "))
result = int(input("Please Input Your initial amount: "))
# result = 100
counter = 0

while(counter < num):
    result = result + result * 0.1
    counter = counter + 1
print(result)