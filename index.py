def capitalize_words_with_spaces(s):
    words = s.split(' ')
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

input_string =input()

capitalized_output = capitalize_words_with_spaces(input_string)
print("Capitalized Output:", capitalized_output)


#132 456 Wq  m e
#hello   world  lol