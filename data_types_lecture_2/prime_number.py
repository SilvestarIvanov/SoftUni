number_input=int(input())
prime=True
for i in range(2,number_input):
    if number_input % i==0:
        prime=False
        break
print(prime)