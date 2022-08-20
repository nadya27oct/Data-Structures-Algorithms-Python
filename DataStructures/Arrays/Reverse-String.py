# Check Input. What if input is not a string?
# What if input is empty or 1 letter?

string = "Attributes may be data or method."

def reverse_string(string):

    reverse = string[::-1]
    return reverse


print(reverse_string(string))

def reverse_string_as_list(string):

    if type(string) != str or len(string) < 2:
        return "Not a valid input"

    else:

        total_items = len(string) - 1

        backwards = []
        while total_items >= 0:
            backwards.append(string[x])
            x -= 1

        return ''.join(backwards)

print(reverse_string_as_list(string))
# Time complexity O(n)
