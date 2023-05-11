def elements_parells(llista):
    result = []
    for i in range(len(llista)):
        if i % 2 == 0:
            result.append(llista[i])
    return result

l=[1,2,3,4,5,6,67,7,8,9,7,7,3]

print(elements_parells(l))