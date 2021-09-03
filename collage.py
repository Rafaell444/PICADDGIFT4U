import os

p = []
with open("s.txt", "r+") as file:
    for line in file:
        done = os.path.basename("r" + line)
        a = done[:-6]
        # format in the template I need
        print("""{{title:"{}",description: "ზომა≈ A3+",output: "ფასი: 6.50"}},""".format(a))
        splitted = a.split("№")

        p.append(splitted[0])

    # remove dublicates
    res = []
    for i in p:
        if i not in res:
            res.append(i)
    #
    # second part:button making

    counter = 1
    for g in res:
        withoutposter = g[:-9]
        print("""{{id : "{}", name :"{}"}},""".format(counter, withoutposter))
        counter += 1
