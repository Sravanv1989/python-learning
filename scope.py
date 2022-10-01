sum=10
def calculate():
    global sum
    sum=sum+20
    currentsum = 200
    totalSum = (sum+currentsum)
    print(totalSum)

calculate();
print(sum)