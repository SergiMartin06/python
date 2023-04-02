count = 0  
for num in range(2, 101):
    is_prime = True 
    for i in range(2, num):
        if num % i == 0:
            is_prime = False 
            break
    if is_prime:
        print(num, end=' ')
        count += 1
print("\nTotal de nombres primers: ", count)


