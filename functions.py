def quick_string(my_word):
    """
    Sort a string from A-Z using recursive quick sort

    Parameters:
        my_word - string of maximum 10 uppercase letters and nothing else
    Returns:
        sorted_string - a new string after being sorted
    """

    # Checking the amount of unique letters instead of total in the base case
    # This prevents errors caused by duplicate letters
    unique_letters = ""
    for i in my_word:
        if i not in unique_letters:
            unique_letters += i

    if len(unique_letters) <= 1:
        return my_word
    else:
        pivot = my_word[(len(my_word)-1) // 2]
        less, equal, greater = "", "", ""
        for i in my_word:
            if i < pivot:
                less += i
            elif i > pivot:
                greater += i
            else:
                equal += i
        sorted_string = quick_string(less) + quick_string(equal) + quick_string (greater)
        return (sorted_string)


def string_permutations(my_word):
    """
    Recursively finds the permutations of a given string. Stores in a list of strings.

    Parameters:
        my_word - a sorted string of maximum 10 letters
    Returns:
        Permutations_list - a list of strings of all possible permutations
    """
    Permutations_list = []

    letters_to_permute = my_word
    if len(letters_to_permute) > 0:
        for i in letters_to_permute:
            Permutations_list.extend(construct_permutations(letters_to_permute.replace(i,''), i))
    
    return Permutations_list


# Recursive function called and set up by string_permutations
def construct_permutations(remaining_letters, cur):
    # List of permutations constructed
    permutations = []

    # If no letters remain, a permutation has been fully constructed
    if len(remaining_letters) < 1:
        permutations.append(cur)
    else:
        # Otherwise, constructs new permutations with remaining_letters
        for i in remaining_letters:
            # Recursive call, adds new letter to cur to continue construction of permutation
            # Also removes the added letter as it shouldn't appear again
            permutations.extend(construct_permutations (remaining_letters.replace(i,''), cur+i))

    return permutations