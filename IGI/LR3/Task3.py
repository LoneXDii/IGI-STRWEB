def check_string(string):
    lower_consonant = "бвгджзйклмнпрстфхйчшщbcdfghjklmnpqrstvwxyz"
    words = string.split()
    lower_started_words = 0
    a = len(words)
    for i in range(0, len(words)):
        if words[i][0] in lower_consonant:
            lower_started_words += 1
    return lower_started_words

def task3():
    string = input("Enter your string:\n")
    print("In your string ", check_string(string), " words started with lowercase consonant letter")
    return
