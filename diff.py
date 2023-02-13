import sys
import re

add = 0
sub = 0
ins = []
outs = []
index = 0

# asm = open('pass.asm')
asm = open(str(sys.argv[1]))
content = asm.readlines()

inAsm = set()

def handleResult():
    global add, sub, ins, outs
    if add != sub and ins and outs:
            temp = ins[0]
            temp = re.sub(r'0x.*\Z', "0xhex", temp);
            if temp not in inAsm and len(ins) == 1:
                # ignore ins with length more than 1
                # we can get full coverage without them
                # assert len(ins) == 1
                print("====>")
                print(ins)
                print("=====")
                print(outs)
                print("<====")
            inAsm.add(temp)
    add = 0
    sub = 0
    ins.clear()
    outs.clear()

with open(sys.argv[2], 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        if line[0].isdigit():
            if line.find(',') != -1:
                idx = int(line.split(',')[0])
                if idx - 1 == index:
                    ins.append(content[index - 1][:-1])
                    outs.append(content[index - 1][:-1])
                else:
                    index = idx
                    handleResult()
            else:
                handleResult()
        elif line[0] == '>':
            ins.append(line[2:])
            add += 1
            index += 1
        elif line[0] == '<':
            outs.append(line[2:])
            sub += 1
            index += 1
