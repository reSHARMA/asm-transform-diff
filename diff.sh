objd () {
 objdump  -drwC -Mintel --no-show-raw-insn $1 &> $1.asm
}

clean () {
 sed -i '/:$/d' $1
 sed -i 's/#.*$//' $1
 sed -i '/^$/d' $1
 sed  -i '/^[a-z,A-Z]/d' $1
 sed -i 's/.*\t//' $1
 sed -i '/nop/d' $1
 sed -i '/lea/d' $1
 sed -i '/je/d' $1
 sed -i '/jne/d' $1
 sed -i '/jmp/d' $1
 sed -i '/jae/d' $1
 sed -i '/jbe/d' $1
}

objd $1
objd $2
clean $1.asm
clean $2.asm
diff --strip-trailing-cr -B -Z -I "(0x|0X)?[a-fA-F0-9]+" $1.asm $2.asm > diff.txt
python3 ~/diff.py $1.asm diff.txt
