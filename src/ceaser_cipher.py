def encrypt(text, key):
    result = ""
    for count in range(0, len(text)):
        each_char = text[count]
        if each_char >= 'a' and each_char <= 'z':
            letter = chr(ord(each_char) + key)
            if each_char > 'z':
                letter = chr(ord(each_char) - 26)

        if each_char >= 'A' and each_char <= 'Z':
            letter = chr(ord(each_char) + key)
            if each_char > 'Z':
                letter = chr(ord(each_char) + 26)
        result += letter

    return result


def decrypt(word, key):
    result = ""
    for count in range(0, len(word)):
        each_char = word[count]
        if each_char >= 'a' and each_char <= 'z':
            letter = chr(ord(each_char) - key)
            if each_char > 'z':
                letter = chr(ord(each_char) + 26)

        if each_char >= 'A' and each_char <= 'Z':
            letter = chr(ord(each_char) - key)
            if each_char > 'Z':
                letter = chr(ord(each_char) + 26)
        result += letter

    return result





