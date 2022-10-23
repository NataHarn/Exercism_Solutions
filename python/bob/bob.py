def response(hey_bob):
    hey_bob = hey_bob.strip(" \t\r\n")
    if hey_bob == "":
            return "Fine. Be that way!"
    elif hey_bob[-1] == '?':
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    else:
        if hey_bob.isupper():
            return "Whoa, chill out!"
        return "Whatever."
