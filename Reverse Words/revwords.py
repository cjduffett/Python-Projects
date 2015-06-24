# REVERSE WORDS
# ===============
# Google Code Jam
# Carlton Duffett

# SMALL FILE SIZE
f = open("B-small-practice.in")
n = int(f.readline())
lists = list()

for i in range(0, n):
    lists.append(f.readline().split())

f.close()
f = open("B-small-practice.out",'w')

for i in range(0, n):
    f.write("Case #" + str(i + 1) + ":")
    lists[i].reverse()

    for j in range(0,len(lists[i])):
        f.write(" " + lists[i][j])

    f.write("\n")

f.close()

# LARGE FILE SIZE
f = open("B-large-practice.in")
n = int(f.readline())
lists = list()

for i in range(0,n):
    lists.append(f.readline().split())

f.close()
f = open("B-large-practice.out",'w')

for i in range(0,n):
    f.write("Case #" + str(i + 1) + ":")
    lists[i].reverse()

    for j in range(0,len(lists[i])):
        f.write(" " + lists[i][j])

    f.write("\n")

f.close()