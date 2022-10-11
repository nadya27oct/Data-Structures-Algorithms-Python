"""
Given a string and a rotation factor, return an encrypted string.
String = "Zebra-493?". Rotation factor is 3. Resulting string is "Cheud-726?
Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A),
and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0).
Note that the non-alphanumeric characters remain unchanged.
"""
def rotationalCipher(input_str, rotation_factor):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ''

    for i in input_str:
        if i.isalnum():
            if i.isalpha():
                if i.isupper():
                    idx = alphabet.index(i.lower())
                    new_idx = (idx+rotation_factor)%26
                    encrypted += alphabet[new_idx].upper()
                else:
                    idx = alphabet.index(i)
                    new_idx = (idx+rotation_factor) % 26
                    encrypted += alphabet[new_idx]
            else:
                num = (int(i) + rotation_factor) % 10
                encrypted += str(num)

        else:
            encrypted += i

    return encrypted

str1 = rotationalCipher("Zebra-493?", 3) # Cheud-726?
str2 = rotationalCipher("abcdefghijklmNOPQRSTUVWXYZ0123456789",39) # nopqrstuvwxyzABCDEFGHIJKLM9012345678
str3 = rotationalCipher("All-convoYs-9-be:Alert1.",4) # Epp-gsrzsCw-3-fi:Epivx5.
str4 = rotationalCipher("abcdZXYzxy-999.@",200) #stuvRPQrpq-999.@
