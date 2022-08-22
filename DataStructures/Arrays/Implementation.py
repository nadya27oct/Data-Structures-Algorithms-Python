class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def access(self,index):
        return self.data[index]

    def push(self,element):
        self.data[self.length] = element
        self.length += 1

        return self.length

    def __str__(self):
        array = str(self.__dict__)
        return array

    def list(self):
        return self.data.values()

    def pop(self):
        last_item = self.length-1
        del self.data[last_item]
        self.length -= 1

        return self.data

    def delete(self,index):
        if index >= self.length:
            return 'Not a valid input'

        self.length -=1
        for i in range(index,self.length):
            self.data[i] = self.data[i+1]

        del self.data[self.length]

        return self.data

# a=['hi', 5, 'nemo', 70, 12,'code']. if we delete 2nd element, a = ['hi', 5, 'nemo', 12,code]
# a[2] = a[3] after deletion. a[0]='hi',a[1]=5, a[2]=12, a[3]='code'
# range(2,5) --> {2-->70, 3--> 12, 4-->'code'...5 remains at 'code'}

    def insert(self,index,value):
        if index >= self.length:
            return 'Not a valid input'

        else:

            self.data[index] = value

            i = self.length
            while i > index:
                self.data[i] = self.data[i-1]
                i -= 1

            self.length += 1

# a =['a','b','c','d']. insert(2,'x') # a=['a','b','x','c','d']. a[2] = 'x'
#after insertion, a[3] = a[2], a[4] = a[3]
# a[3] = 'c',a[4]='d'
# range(2,5), 2-->new,3-->c, 4--> d

new_array = MyArray()
new_array.push('hi')
new_array.push(5)
new_array.push('nemo')
new_array.push(70)

print(new_array.access(2))
new_array.push(12)
new_array.push('code')

print(new_array)
print(new_array.delete(2))
print(new_array.insert(3,'new'))
print(new_array)
