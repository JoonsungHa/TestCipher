#  File: TestCipher.py

#  Description:

#  Student's Name: Joonsung Ha

#  Student's UT EID: jh69256

#  Partner's Name: Laurence Wang

#  Partner's UT EID: lnw653

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(strng, key):
    lst = []
    for row in range(3):
        re = []
        for col in range(len(strng)):
            re.append("-")
        lst.append(re)

    row_index = 0
    col_index = 0
    length = len(strng)

    while strng != "":
        for i in range(key):
            if col_index < length:
                lst[row_index][col_index] = strng[0]
                strng = strng[1:]
                row_index += 1
                col_index += 1
            else:
                break

        if col_index < length:
            row_index -= 1
            col_index -= 1
        else:
            break

        for b in range(key - 2):
            if col_index < length:
                row_index -= 1
                col_index += 1
                lst[row_index][col_index] = strng[0]
                strng = strng[1:]
            else:
                break
        if col_index < length:
            row_index = 0
            col_index += 1
        else:
            break

    return lst


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng, key):
    # I have to recreate the list

    return ""


#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):

    strng = str(strng).lower()
    f = []
    g = ""
    for x in range(len(strng)):
        if 97 <= ord(strng[x]) <= 122:
            f.append(strng[x])
    for x in f:
        g += x
    strng = g
    return(strng)  # placeholder for the actual return statement


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p, s):
    q = ord(p)
    v = ord(s)-97
    q += v
    if q > 122:
        q -= 26
    return chr(q)  # placeholder for actual return statement


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p, s):
    q = ord(p)
    v = ord(s) - 97
    q -= v
    if q < 97:
        q += 26
    return chr(q)  # placeholder for actual return statement


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(strng, phrase):
    s = ""
    for x in range(len(strng)):
        s += encode_character(phrase[x % len(phrase)], strng[x])
    return s  # placeholder for the actual return statement


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(strng, phrase):
    s = ""
    for x in range(len(strng)):
        s += decode_character(strng[x], phrase[x % len(phrase)] )
    return s
def main():
    # prompt the user to enter plain text
    plain_text = input("Enter Plain Text to be Encoded: ")

    # prompt the user to enter the key
    key = input("Enter Key: ")

    # encrypt and print the plain text using rail fence cipher

    # prompt the user to enter encoded text

    # prompt the user to enter the key

    # decrypt and print the encoded text using rail fence cipher

    # prompt the user to enter plain text
    plain_text = input("Enter Plain Text to be Encoded: ")
    plain_text = filter_string(plain_text)

    # prompt the user to enter pass phrase
    key = input("Enter Pass Phrase (no spaces allowed): ")
    key = filter_string(key)

    # encrypt and print the plain text using Vigenere cipher
    s = vigenere_encode(plain_text, key)
    print(s)

    # prompt the user to enter encoded text
    plain_text = input("Enter Encoded Text to be Decoded: ")
    plain_text = filter_string(plain_text)

    # prompt the user to enter pass phrase
    key = input("Enter Pass Phrase (no spaces allowed): ")
    key = filter_string(key)

    # decrypt and print the encoded text using Vigenere cipher
    s = vigenere_decode(plain_text, key)
    print(s)


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
