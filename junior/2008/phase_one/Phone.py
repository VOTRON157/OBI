phone_number = input()
converted_phone_number = ""
if phone_number.isalpha:
    for char in phone_number:
        if char == '-':
            converted_phone_number += '-'
        elif char == 'A' or char == 'B' or char == 'C':
            converted_phone_number += '2'
        elif char == 'D' or char == 'E' or char == 'F':
            converted_phone_number += '3'
        elif char == 'G' or char == 'H' or char == 'I':
            converted_phone_number += '4'
        elif char == 'J' or char == 'K' or char == 'L':
            converted_phone_number += '5'
        elif char == 'M' or char == 'N' or char == 'O':
            converted_phone_number += '6'
        elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
            converted_phone_number += '7'
        elif char == 'T' or char == 'U' or char == 'V':
            converted_phone_number += '8'
        else:
            converted_phone_number += '9'
    print(converted_phone_number)