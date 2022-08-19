string = ['a','b','c','d']

#Insert
string.append('e')
# O(1)
# We are not looping through array - just adding an element at the end.
print(string)

# O(n) complexity as we have to shift array indices.
string.insert(3,'z') #Reassigned index by looping through array after 3rd element
print(string)

#Delete
string.pop() # remove last item. O(1). Not looping through.
print(string)

string.pop(2) # O(n): Elements to right of 3rd element needs to be removed.
# Need to loop over array to reassign index.

#Lookup
print(string[2]) #O(1) operation as we are performing look up.
#Regardless of the size of array, we only access element at 3rd position.
