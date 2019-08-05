
f=open('binary.txt','rb')
b=f.read()
f.close()
ba=bytearray(b)
ba[10:15]=[0x41,0x42,0x43,0x44]
print(ba)

f=open('binary.txt','wb')
f.write(ba)
f.close()

