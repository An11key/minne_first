import os.path


def bp():
    file = "lox.txt"
    name = "Non-overlapping Intervals"
    link = "https://leetcode.com/problems/non-overlapping-intervals/"
    code = "dfsdf"
    if not os.path.exists(file):
        f = open(file, 'w')
        f.close()
    f = open(file, 'r')
    if os.stat(file).st_size == 0:
        f.close()
        f = open(file, 'w')
        f.write("#{}\n\n+[{}](#{})\n\n##{}\n\n{}\n\n```python\n{}\n```".format(file.split('.')[0].capitalize(), name,
                                                                               name.lower().split(' ')[0] + '-' +
                                                                               name.lower().split(' ')[1], name, link,
                                                                               code))
    else:
        all_elem = f.read().split("\n\n")
        all_names = all_elem[0].split('\n')
        all_names2 = all_elem[1].split('\n')
        all_names3 = all_elem[2].split('\n')
        all_links = all_elem[3].split('\n')
        all_code = all_elem[4].split('```')
        all_links.append(link)
        all_code.append(code)
        print(all_links)

        f.close()
bp()