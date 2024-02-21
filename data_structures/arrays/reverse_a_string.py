# Create a function that reverses a string
# Example: "Hi my name is Jon" -> "noJ si eman ym iH"

def simple_reverse_string(string):
    new_string = []
    for i in range(len(string)-1, -1, -1): #Iterating through the string in reverse order
        new_string.append(string[i]) #Appending the characters to a new list
    return ''.join(new_string) #Joining the list to form a string

string = "Hi my name is Jon"
print(simple_reverse_string(string)) #noJ si eman ym iH. Time complexity: O(n)

#Since we only have to traverse the string once, the time complexity is O(n)
#But since we are also creating a new array of the same size , the space complexity is also O(n)


#A smarter way to do this , can be taking a pair of elements from either end of the string and swapping them
#We have start at both the ends and continue swapping pairs till the middle of the string
#Because we are creating a list in the swap function, space complexity is O(4*n) and time complexity is still at O(n)
def swap(string, a, b):
    string = list(string)
    temp = string[a]
    string[a] = string[b]
    string[b] = temp
    return ''.join(string)

# Optimized approach
def optimized_reverse_string(string):
    for i in range(len(string)//2):
        string = swap(string, i, len(string)-i-1)
    return string

print (optimized_reverse_string(string)) #noJ si eman ym iH

#Apart from these, some built-in functions that can be used to reverse a string are as follows:

string1 = 'abcde'
string2 = reversed(string1)
print(''.join(string2))

list1 = list(string1)
list1.reverse()
print(''.join(list1))

#Both these methods are of O(n) time complexity