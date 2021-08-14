# reading opening writing in the file and  filtering string the way I want


import os

p = []
with open("s.txt", "r+") as file:
    for line in file:
        done = os.path.basename("r" + line)
        a = done.replace('.', '')[:-5]
        # format in the template I need
        print("""{{title:"{}",description: "ინფორმაცია",output: "ფასი"}},""".format(a))
        splitted = a.split("№")

        p.append(splitted[0])

    # remove dublicates
    res = []
    for i in p:
        if i not in res:
            res.append(i)
    #
    # second part:button making

    for g in res:
        # for j in range(len(res)):
        print("""{{id : 1, name :"{}"}},""".format(g))

