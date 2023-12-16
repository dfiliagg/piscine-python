import sys

def ft_remove_spaces(word):
    new_word = ""
    for letter in word:
        if letter != " ":
            new_word += letter
    return new_word

def is_palindrome(word):
    word = ft_remove_spaces(word)
    begin, end = 0, len(word) - 1
    while begin < end:
        if word[begin] != word[end]:
            return False
        begin += 1
        end -=1
    return True

def main():
    if len(sys.argv) != 2:
        print("Error! Insert just 1 string!")
        exit()
    if is_palindrome(sys.argv[1]):
        print("The string "+sys.argv[1]+" is palindrome")
    else:
        print("The string "+sys.argv[1]+ " is not palindrome")

if __name__ == "__main__":
    main()
