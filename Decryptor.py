from PIL import Image
import math
import binascii
def keyUnpacking(key):
    codeArray=[]
    codeArrayNested=[]
    code = bin(int(str(key),16))[2:]
    if(len(code)%8!=0):
        code='0'*((math.ceil(len(code)/24))*24-len(code))+code
    code_copy=code
    for i in range (len(code)//24):
        for j in range(3):
            cnt=0
            currentStr = ''
            for k in code_copy:
                if cnt==8: break
                currentStr += k
                cnt+=1
            code_copy=code_copy[8:]
            codeArrayNested.append(int(currentStr,2))
        codeArray.append(codeArrayNested)
        codeArrayNested=[]
    print(codeArray)
    return codeArray

def pxDiff(pixel,a,fix,j):
    string = bin(int(abs(int(pixel) - int(a))))[2:]
    string = '0'*((2+fix)-len(string))+string
    print('[',j,']',pixel,'-',a,'=',string)
    return string

def bit2txt(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def decrypt(adress,key):
    text=''
    string=''

    img = Image.open(adress)
    img = img.convert('RGB')
    pxArray=keyUnpacking(key)
    length=len(pxArray)
    print(length)


    siz = img.size
    if ((length) < siz[0]):
        x = length
        y = 1
    else:
        x = siz[0]
        y = math.ceil(length / siz[0])
    cnt=0
    for i in range(x):
        for j in range(y):
            if cnt < length:
                r=pxDiff(int(img.getpixel((i, j))[0]),pxArray[cnt][0],1,j)
                g=pxDiff(int(img.getpixel((i, j))[1]),pxArray[cnt][1],1,j)
                b=pxDiff(int(img.getpixel((i, j))[2]),pxArray[cnt][2],0,j)
                text=text+str(bit2txt(r+g+b))
                cnt+=1
                print('bin = ', r+g+b,'symb = ', bit2txt(r+g+b),'\n')
            else:
                break
    print('txt = ',text)
    return text