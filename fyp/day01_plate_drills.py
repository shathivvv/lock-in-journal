import re

PLATE_PATTERN = re.compile(r"^[A-Z]{1,3}\d{1,4}[A-Z]?$")

def normalize(text):
    return re.sub(r"[^A-Z0-9]", "", text.upper())

def count_letters_digits(text):
    text = text.upper()
    letters = 0
    digits = 0
    for char in text :
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            letters +=1
        elif char in "0123456789":
            digits+=1
    return (letters,digits)
    
        
def normalize_loop(text):
    text = text.upper()
    result = ""

    for char in text:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or char in "0123456789":
            result += char

    return result

def is_valid_plate(text):
    plate = normalize(text)
    return PLATE_PATTERN.match(plate) is not None

#^ means is the start, A-Z 1,3 grabs 1 to 3 letters in this case WA, \d {1,4} grabs any 4 digit from 0-9 which is 1, [A-Z]? grabs only one letter if exists which is O and $ is the end of string but still remains 34

assert not is_valid_plate("WA1O34")
# Valid cases
assert is_valid_plate("WA1234B") 
assert is_valid_plate("BJT 8558") 
assert is_valid_plate("W 1234")

# Invalid cases
assert not is_valid_plate("HONDA")
assert not is_valid_plate("WXYZ123") 
assert not is_valid_plate("WA12345") 

print("Task 1 passed!")

# Task 6 tests
assert normalize_loop("wa 1234 b") == normalize("wa 1234 b")
assert normalize_loop("W-A1234") == normalize("W-A1234")
assert normalize_loop("bjt.8558") == normalize("bjt.8558")
assert normalize_loop("  ") == normalize("  ")
assert normalize_loop("ÄB12") == normalize("ÄB12")

print("Task 6 passed!")

# Task 7 tests
assert count_letters_digits("WA1234B") == (3, 4)
assert count_letters_digits("wa1234b") == (3, 4)  # Lowercase is converted to uppercase before counting.
assert count_letters_digits("") == (0, 0)

print("Task 7 passed!")