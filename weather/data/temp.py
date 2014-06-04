fout = open('result.txt', 'w+')
with open("city_code.txt") as fin:
    for line in fin:
        line = line.strip()
        if line == "":
            continue
        else:
            line = line.decode('utf-8')
            words = line.split('=')
            line = "%s %s\n" % (words[1], words[0])
            fout.write(line.encode('utf-8'))
fout.close()
