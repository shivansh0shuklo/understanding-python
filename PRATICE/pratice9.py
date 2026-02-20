# # The Goal: Write a function that takes a string (like a sentence) and returns a dictionary.

# The dictionary should contain every unique word in the sentence as a key.

# The value should be a boolean (True or False) indicating whether that word is a palindrome (reads the same forwards and backwards).

# Bonus: Ignore punctuation and capitalization!

# Example Input: "Wow, did you see that racecar?"
# Example Output: {'wow': True, 'did': True, 'you': False, 'see': False, 'that': False, 'racecar': True}
import string
def check(sentences):
    # parts = string.strip("?!,.").lower()#strip is used for the removing the special characters
    re = str.maketrans("","","?.,!")#
    clean_txt_list = sentences.translate(re).lower().split()
    dictionary = {}
    i = 0
    while (i<len(clean_txt_list)):
        word  = clean_txt_list[i]
        if (word == word[::-1]):
            dictionary[word] = True
        else:
            dictionary[word] = False
        i+=1
    return dictionary
text  = "hello, How are you wow omg?"
b  = check(text)
print(b)