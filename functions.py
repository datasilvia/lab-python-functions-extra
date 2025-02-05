import string

def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
   
    lista = list(set(lst))
    print(lista)



def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """

    upper = 0
    lower = 0

    
    for letter in string:
        if letter.isupper():
                upper += 1
        elif letter.islower():
                lower += 1
    
    count = {"Uppercase letters": upper, "Lowercase letters": lower}
    print(count)



def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
  
    import string

    new_sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    print(new_sentence)
    return new_sentence



def word_count_f(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    sentence = remove_punctuation_f(sentence)
    count = (len(sentence.split()))
    return count