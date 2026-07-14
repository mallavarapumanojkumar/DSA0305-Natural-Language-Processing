def pluralize(noun):

    if noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        plural = noun + "es"

    elif noun.endswith('y') and noun[-2] not in "aeiou":
        plural = noun[:-1] + "ies"

    else:
        plural = noun + "s"

    return plural


word = input("Enter a noun: ")
print("Plural form:", pluralize(word))
