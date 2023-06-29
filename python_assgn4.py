#Python program to create a function

def most_frequent(string):
    # Create an empty dictionary to store the letter frequencies
    freq_dict = {}

    # Count the frequency of each letter in the string
    for letter in string:
        freq_dict[letter] = freq_dict.get(letter, 0) + 1

    # Sort the dictionary by values in descending order
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))

    # Print the letters in decreasing order of frequency
    for letter, frequency in sorted_dict.items():
        print(letter, frequency)


# Getting string value from the user
input_string = input("Enter a string: ")
most_frequent(input_string)
