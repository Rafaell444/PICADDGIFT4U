import os

p = []
with open("s.txt", "r+") as file:
    for line in file:
        done = os.path.basename("r" + line)
        a = done[:-6]
        # format in the template I need
        if a[0:5] == "30X42":
            print("""{{title:"{}",description: "ზომა≈ A3+",output: "ფასი: 35"}},""".format(a))
        elif a[0:5] == "40X50":
            print("""{{title:"{}",description: "ზომა≈ A3+",output: "ფასი: 45"}},""".format(a))
        elif a[0:5] == "50X70":
            print("""{{title:"{}",description: "ზომა≈ A3+",output: "ფასი: 65"}},""".format(a))
        elif a[0:5] == "60X80":
            print("""{{title:"{}",description: "ზომა≈ A3+",output: "ფასი: 75"}},""".format(a))
        elif a[0:5] == "70X90":
            print("""{{title:"{}",description: "ზომა≈ A3+",output: "ფასი: 95"}},""".format(a))
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
