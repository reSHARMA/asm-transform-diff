import sys

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
            assert len(ins) == 1
            if ins[0] not in inAsm:
                print("====>")
                print(ins)
                print("=====")
                print(outs)
                print("<====")
            inAsm.add(ins[0])
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
