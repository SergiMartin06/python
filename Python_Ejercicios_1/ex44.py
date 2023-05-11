def esta_ordenada(nums):
    if nums == sorted(nums):
        print ("està ordenada de forma ascendent")
    elif nums == sorted(nums, reverse=True):
        print ("està ordenada de forma descendent")
    else:
        print ("no està ordenada")


l=[1,2,3,4,5,6]

esta_ordenada(l)