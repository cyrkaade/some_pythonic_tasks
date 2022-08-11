def max_letter(string):
    number = 1
    highest_letter = None
    for letter in string:
        sum_letter = string.count(letter)
        if sum_letter > number:
            number = sum_letter
            highest_letter = letter
    return highest_letter, number
print(max_letter('aaabbbb'))
