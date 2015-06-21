# MKDIR
# ================
# Google Code Jam
# Carlton Duffett

# Determines how many mkdir operations are needed to create
# a desired set of folders, given a set of folders that exist
# already.

sizes = ["small", "large"]

for size in sizes:

    f = open("A-" + size + "-practice.in")
    x = open("A-" + size + "-practice.out",'w')

    t = int(f.readline())
    fs = {} # master file system

    for test in range(0,t):

        dims = f.readline().split()
        n = int(dims[0]) # number of directories following that already exist
        m = int(dims[1]) # number of directories that need to be created
        fs.clear()
        num_mkdirs = 0

        # build know directory structure
        for i in range(0,n):

            path = f.readline()[:-1] # strip newline
            dirs = path.split('/')
            folder = fs

            for adir in dirs[1:]:

                if adir not in folder:
                    # mkdir
                    folder[adir] = {} # sub directories are also dicts

                # cd
                folder = folder[adir]

        # test directory structure for creation of new dirs
        for j in range(0,m):

            path = f.readline()[:-1] # strip newline
            dirs = path.split('/')
            folder = fs

            for adir in dirs[1:]:

                if adir not in folder:
                    # mkdir
                    folder[adir] = {}
                    num_mkdirs += 1

                #cd
                folder = folder[adir]

        x.write("Case #" + str(test + 1) + ": " + str(num_mkdirs) + "\n")

    f.close()
    x.close()

# for(size)



