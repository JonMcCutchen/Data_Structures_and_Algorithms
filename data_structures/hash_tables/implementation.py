#Although hash tables come built-in in the form of dictionaries in Python,
#here we'll try to implement our own hash table

class hash_table():
    def __init__(self, size): #Constructor to initialize the size of the hash table
        self.size = size #Size of the hash table
        self.data = [None]*size #Creating an array of size 'size' with all elements as None 
    
    def __str__(self): #This function will be called when we print the object of this class
        return str(self.__dict__) #This will print the dictionary of the object
    
    def _hash(self, key): #This function will return the hash value of the key
        hash = 0
        for i in range(len(key)): #Loop through the characters of the key
            hash = (hash + ord(key[i])*i) % self.size #ord() returns the Unicode code of a character
        return hash #Return the hash value
    
    def get(self, key): #This function will return the value of the key
        hash = self._hash(key) #Get the hash value of the key
        if self.data[hash]: #If the hash value is not empty
            for i in range(len(self.data[hash])): #Loop through the list at the hash value
                if self.data[hash][i][0] == key: #If the key is found
                    return self.data[hash][i][1] #Return the value of the key
        return None #If the key is not found, return None
    
    def set(self, key, value): #This function will set the value of the key
        hash = self._hash(key) #Get the hash value of the key
        if not self.data[hash]:
            self.data[hash] = [[key, value]] #If the hash value is empty, we'll add the key-value pair as a list
        else:
            self.data[hash].append([key, value]) #If the hash value is not empty, we'll append the key-value pair to the list
        return self.data #Return the updated hash table

def keys(self): #Function to return all the keys
        keys_array = [] #Array to hold the keys
        for i in range(self.size): #We loop over the entire table
            if self.data[i]: #If we find a non-empty bucket, we go in and loop over all the key,value pairs that might be in it
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])): #Looping over all the lists(key,value pairs) in the current bucket
                        keys_array.append(self.data[i][j][0]) #Adding the key of each list to the keys_array
                else:
                    keys_array.append(self.data[i][0][0])
        return keys_array

def values(self): #Function to return all the values, with exactly the same logic as the keys function
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])  #Only difference from the keys function is instead of appending the first element, we are appending the last element of each list
        return values_array

new_hash = hash_table(2)
print(new_hash)
#{'size': 2, 'data': [None, None]}

new_hash.set('one',1)
new_hash.set('two',2)
new_hash.set('three',3)
new_hash.set('four',4)
new_hash.set('five',5)
print(new_hash)
#{'size': 2, 'data': [[['one', 1], ['five', 5]], [['two', 2], ['three', 3], ['four', 4]]]}

print(new_hash.get('one'))
#1

print(new_hash.keys())
#['one', 'five', 'two', 'three', 'four']
print(new_hash.values())
#[1, 5, 2, 3, 4]


#Now although there are some for loops running in the class hash,
#the time complexity is not O(n).
#This is because n stands for the size of the input, which corresponds to number of key,value pairs in the table
#But the for loop in the _hash function runs only for the length of the key, which would be insignificantly small in comparison to the number of entries in general.
#Also, the for loop in the get function runs for the length of the collisioned array, which in most cases, won't be too long
#Atleast nowhere near to the number of total entries, hence the time complexity remains way less than O(n), even less than O(log n) in most cases
#The keys and values methods are slightly worse than O(n) though, as we have to loop over the entire size of the table once,
#And loop over all the lists in the buckets which have collision