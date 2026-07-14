def fsa_ends_with_ab(string):
    state = "q0"

    for ch in string:
        if state == "q0":
            if ch == 'a':
                state = "q1"
            else:
                state = "q0"

        elif state == "q1":
            if ch == 'a':
                state = "q1"
            else:
                state = "q2"

        elif state == "q2":
            if ch == 'a':
                state = "q1"
            else:
                state = "q0"

    if state == "q2":
        return "Accepted"
    else:
        return "Rejected"


s = input("Enter a string: ")
print(fsa_ends_with_ab(s))
