def printFirstItemThenFirstHalfThenSayHi100Times(items):
    print(items[0])

    middleIndex = len(items) // 2
    index = 0

    while index < middleIndex:
        print(items[index])
        index += 1
    
    for _ in range(100):
        print('hi')
    

#  O(1 + n/2 + 100) or O(n)