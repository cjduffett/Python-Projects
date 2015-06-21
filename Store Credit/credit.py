# STORE CREDIT
# ===============
# Google Code Jam
# Carlton Duffett

# Searches through each list of prices for two prices that add up to the "credit".
# There may be duplicate prices. For example, if the credit is 8 and there are two
# items of price 4. Uses hashing for constant-time lookup.

sizes = ["small","large"]

for size in sizes:

    f = open("A-" + size + "-practice.in")
    x = open("A-" + size + "-practice.out",'w')
    n = int(f.readline())
    d = dict()

    for i in range(0,n):

        try:

            credit = int(f.readline()) # credit
            no_items = int(f.readline()) # num items
            prices = f.readline().split()
            d.clear()

            for j in range(0,no_items):

                if prices[j] not in d:
                    d[prices[j]] = list()

                d[prices[j]].append(j + 1) # 1-based index, hold in list frr duplicates

            # for (prices)

            for price in prices:

                key = str(credit - int(price)) # new key to search

                if key in d:

                    if price == key:
                        # possibly duplicate values
                        if len(d[price]) > 1:
                            # there were duplicates
                            a = d[price][0]
                            b = d[price][1]
                            break

                        else:
                            # no duplicate values
                            continue

                    a = d[price][0]
                    b = d[key][0]
                    break

                # if (key)
            # for (price)

            x.write("Case #" + str(i + 1) + ": " + str(a) + " " + str(b) + "\n")

        except IndexError:

            print "------------------------------"
            print "Failed on Case #" + str(i + 1)
            print "credit: " + str(credit)
            print "a key: " + price
            print "a = " + str(d[price][0])
            print "b key: " + key
            print "b = " + str(d[key][0])
            print "d[price]: " + str(d[price])
            print "d[key]: " + str(d[key])
        # try

    f.close()
    x.close()

# for (size)
