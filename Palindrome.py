def palindrome(string):
    """ Checks whether given "string" is a palindrome or not."""
    for index in range(int(len(string)/2)):
        if string[index] != string[-index - 1]:
            return False
    return True
