from PIL import Image
import math

def compare_sum(a, b):
    if (a + b > 127):
        c = a - b
    else:
        c = a + b
    return c

def txt2bit(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def cyPixel(pixel, symbol):
    pixel_ar = ['', '', '']
    bit = txt2bit(symbol)
    bit = list(bit.strip())
    k=0
    for i in bit:
        if k<3: pixel_ar[0]=str(pixel_ar[0])+str(i)
        elif k<6: pixel_ar[1]=str(pixel_ar[1])+str(i)
        else: pixel_ar[2]=str(pixel_ar[2])+str(i)
        k+=1
    pixel_ar[0] = compare_sum(pixel[0], int(pixel_ar[0], 2))
    pixel_ar[1] = compare_sum(pixel[1], int(pixel_ar[1], 2))
    pixel_ar[2] = compare_sum(pixel[2], int(pixel_ar[2], 2))
    return [pixel_ar[0], pixel_ar[1], pixel_ar[2]]

def bin_px(pixel):
    string=''
    for i in range(3):
        px=str(bin(pixel[i])[2:])
        if len(px)<8:
            px='0'*(8-len(px))+px

        string+=px
    return string
def get_key(adressLoad,textValue,x,y):
    img=Image.open(adressLoad)
    img = img.convert('RGB')
    string=''
    cnt=0
    for i in range(x):
        for j in range(y):
            if cnt < len(textValue):
                string=string + bin_px(img.getpixel((i,j)))
                cnt+=1
                print(bin_px(img.getpixel((i,j))))
    print(hex(int(string,2))[2:])
    print(int(string, 2))
    print(string)
    return(hex(int(string,2))[2:])
def encode(adressLoad, adressSave,textValue,filename):
    img = Image.open(adressLoad)
    img = img.convert('RGB')

    siz = img.size
    if(len(textValue)<siz[0]):
        x=len(textValue)
        y=1
    else:
        x=siz[0]
        y=math.ceil(len(textValue)/siz[0])
    global getKey
    getKey = get_key(adressLoad, textValue,x,y)
    cnt=0
    for i in range(x):
        for j in range(y):
            if cnt < len(textValue):
                r=int(cyPixel(img.getpixel((i, j)),textValue[cnt])[0])
                g=int(cyPixel(img.getpixel((i, j)),textValue[cnt])[1])
                b=int(cyPixel(img.getpixel((i, j)),textValue[cnt])[2])
                cnt+=1
                print('orig= ',img.getpixel((i, j)))
                print('rgb = ',((r,g,b)),'\n')
                img.putpixel((i, j), ((r, g, b)))
    adress=str(adressSave)+'/'+str(filename)
    print(adress)
    img.save(adress)
    img.close()
    return