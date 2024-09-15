def longest_substring_with_list(s):
    char_list = []  # List to store current substring without repeating characters
    max_len = 0  # Maximum length of the substring

    for char in s:
        # If the character is already in the list, remove characters from the left until it's gone
        while char in char_list:
            char_list.pop(0)  # Remove the first character (from the left)

        char_list.append(char)  # Add the current character to the list

        # Update max_len if the current substring is longer
        max_len = max(max_len, len(char_list))

    return max_len


print(longest_substring_with_list(""))