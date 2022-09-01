#Question - Given a string input, return the reversed string.

# Check Input. What if input is not a string?
# What if input is empty or 1 letter?

string = "Attributes may be data or method."

def reverse_string(string):

    reverse = string[::-1]
    return reverse


reverse_string(string)

def reverse_string_as_list(string):

    if type(string) != str or len(string) < 2:
        return "Not a valid input"

    else:

        x = len(string) - 1

        backwards = []
        while x >= 0:
            backwards.append(string[x])
            x -= 1

        return ''.join(backwards)

reverse_string_as_list(string)
# Time complexity O(n)
