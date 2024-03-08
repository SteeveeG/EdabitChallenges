# Link to Challenge : https://edabit.com/challenge/hZ4HzhboCJ5dDiNve
def special_reverse_string(input):
    trim_input = input.replace(" ", "")
    reverse_i = 0
    reverse_trim = trim_input[::-1]
    reversed_result = ""
    for input_i in range(input.__len__()):
        if input[input_i].isspace():
            reversed_result += " "
            reverse_i -= 1
        else:
            if input[input_i].isupper():
                reversed_result += reverse_trim[reverse_i].upper()
            else:
                reversed_result += reverse_trim[reverse_i].lower()
        reverse_i += 1
    print(reversed_result)


special_reverse_string('Edabit')  # 'Tibade'
special_reverse_string('UPPER lower')  # 'REBOL reppu'
special_reverse_string('1 23 456')  # '6 54 321'
special_reverse_string('Hello World!')  # '!dlro Wolleh'
special_reverse_string("Where's your dog Daisy?")  # "?ysiadg odru oys 'erehw"
special_reverse_string('addition(3, 2) = 5')  # '5=)2,3(noit id d a'
special_reverse_string(
    "It's known that CSS means Cascading Style Sheets")  # "Stee hsely tsgn IDA csacs Naemsscta Htnwo Nks'ti"
