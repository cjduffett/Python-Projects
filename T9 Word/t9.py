# T9 WORD GENERATOR
# =================
# Google Code Jam
# Carlton Duffett

# Generates the needed key presses on a cellphone numpad
# to type out a desired message. For example:

# message:      hi
# keypresses:   44 444

# The keypad is modeled as:

#   1       2       3
#          ABC     DEF
#   4       5       6
#  GHI     JKL     MNO
#   7       8       9
#  PQRS    TUV     WXYZ

# Enumerate letters in the alphabet:
t9 = dict()
t9["a"] = "2"
t9["b"] = "22"
t9["c"] = "222"
t9["d"] = "3"
t9["e"] = "33"
t9["f"] = "333"
t9["g"] = "4"
t9["h"] = "44"
t9["i"] = "444"
t9["j"] = "5"
t9["k"] = "55"
t9["l"] = "555"
t9["m"] = "6"
t9["n"] = "66"
t9["o"] = "666"
t9["p"] = "7"
t9["q"] = "77"
t9["r"] = "777"
t9["s"] = "7777"
t9["t"] = "8"
t9["u"] = "88"
t9["v"] = "888"
t9["w"] = "9"
t9["x"] = "99"
t9["y"] = "999"
t9["z"] = "9999"
t9[" "] = "0"

# Main script:
# -----------------------------------------------
sizes = ["small", "large"]

for size in sizes:

    f = open("C-" + size + "-practice.in")
    x = open("C-" + size + "-practice.out",'w')

    n = int(f.readline())

    for i in range(0,n):

        x.write("Case #" + str(i + 1) + ": ")
        phrase = f.readline()[:-1] # strip newline

        for j in range(0,len(phrase)):

            x.write(t9[phrase[j]])

            if j < len(phrase) - 1:

                if t9[phrase[j]][0] == t9[phrase[j + 1]][0]: # letter on same key
                    # print pause
                    x.write(" ")

        x.write("\n")

    # for(phrase)

    f.close()
    x.close()

# for(size)



