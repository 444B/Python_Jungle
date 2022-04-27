# Vowels -> G

user_string = input("Enter a string: ")
output_string = []

def translate(user_string):
    for letter in user_string:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            # if letter in "AEIOUaeiou"
            # 
            output_string.append("g")
        else:
            output_string.append(letter)

translate(user_string)

print("".join(output_string))

  

