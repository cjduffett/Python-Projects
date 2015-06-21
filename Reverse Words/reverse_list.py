# Practice: Reversing Lists
# =========================
# Carlton Duffett

# Reverses the order of words in a list. For example:

# original: ["this", "is", "a", "test"]
# new:      ["test", "a", "is", "this"]

def tokenizer(string):

    # splits a string at whitespace and returns a list
    strlist = list()

    # skip leading whitespace
    it = 0
    while string[it] == " ":
        it += 1

    last_token = it - 1
    
    for i in range(it,len(string)):

        if i == len(string) - 1:
            strlist.append(string[last_token + 1:i + 1])

        if string[i] == " ":
            strlist.append(string[last_token + 1:i])
            last_token = i

    return strlist
# tokenizer()

def swap(l, a, b):

    # swaps indeces a and b in list l
    tmp = l[a]
    l[a] = l[b]
    l[b] = tmp

# Main script:
# --------------------------------------------------------
string_tests = list()
string_tests.append("this is a test")
string_tests.append("a marvelous sentence")
string_tests.append("catch me if you can")
string_tests.append("there once was a man from nantucket")
string_tests.append("have you ever seen the rain")

for string in string_tests:

    l = tokenizer(string)
    L = len(l)

    for i in range(0, L/2): # integer division == floor

        swap(l, i, L - i - 1)

    print l
