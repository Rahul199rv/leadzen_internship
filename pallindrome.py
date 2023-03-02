def find_longest_palindrome(str_input):
    longest = ''
    n = len(str_input)
    for i in range(n):
        for j in range(i+1,n+1):
            word = str_input[i:j]
            if word == word[::-1]:
                if len(word)>len(longest):
                    longest = word          
    return longest

str_input = input("Enter the string:")
print(find_longest_palindrome(str_input))
