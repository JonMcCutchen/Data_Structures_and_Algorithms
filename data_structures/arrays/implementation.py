#Although arrays are pre-defined in Python in the form of lists, we can implement our own arrays.
#Here, we will implement our own array with some common methods such as access, push, pop, insert, delete

class MyArray():
    def __init__(self):
        self.length = 0 #Initial length of the array
        self.data = {} #We initialize an empty dictionary to store the elements of the array
    
    #The attributes of the array class are stored in a dictionary by default.
    #When the __dict__ method is called on an instance of the class it returns the attributes of the class along with their values in a dictionary format
    #Now, when the instance of the class is printed, it returns a class object with its location in memory.
    #But we know when we print the array we get the elements of the array as output
    #When we print the instance of the class, the built-in __str__ method is called. So we can modify the __str__ method inside the class
    #To suit our needs.
    def __str__(self):
        return str(self.__dict__) #This will return the attributes of the class in a dictionary format

    def get(self, index):
        return self.data[index] #Returns the element at the specified index
    
    def push(self, item):
        self.length += 1
        self.data[self.length-1] = item #Adds the element at the end of the array

    def pop(self):
        last_item = self.data[self.length-1] #Stores the last element of the array
        del self.data[self.length-1] #Deletes the last element of the array
        self.length -= 1 #Decreases the length of the array by 1
        return last_item #Returns the last element of the array. O(1) time complexity

    def insert(self, index, item):
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i-1] #Shifts all elements to the right of the specified index by one place
        self.data[index] = item #Inserts the element at the specified index. O(n) time complexity
        self.length += 1 #Increases the length of the array by 1
    
    def delete(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1] #Shifts all elements to the right of the specified index by one place to the left
        del self.data[self.length-1] #Deletes the last element of the array
        self.length -= 1 #Decreases the length of the array by 1. O(n) time complexity

    
arr = MyArray()
arr.push(5)
# {'length': 1, 'data': {0: 5}}

arr.push(10)
# {'length': 2, 'data': {0: 5, 1: 10}}

arr.push(15)
# {'length': 3, 'data': {0: 5, 1: 10, 2: 15}}

arr.pop()
# {'length': 2, 'data': {0: 5, 1: 10}}


arr.push(15)
arr.push(20)
arr.push(25)
# {'length': 5, 'data': {0: 5, 1: 10, 2: 15, 3: 20, 4: 25}}

arr.insert(2, 12)
# {'length': 6, 'data': {0: 5, 1: 10, 2: 12, 3: 15, 4: 20, 5: 25}}

arr.delete(2)
# {'length': 5, 'data': {0: 5, 1: 10, 2: 15, 3: 20, 4: 25}}

print(arr.get(2))
# 15

print(arr)
#The outputs given after each function call are the outputs obtained by calling print(arr) and not by the function calls themselves