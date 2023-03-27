from PIL import Image
import math

def compare_sum(a, b):
    if (a + b > 127):
        c = a - b
    else:
        c = a + b
    return c

def cyPixel(pixel, symbol):
    pixel_ar = ['', '', '']
    bit = ' '.join(format(ord(x), 'b') for x in symbol)
    bit = list(bit.strip())
    k=0
    for i in bit:
        if k<3: pixel_ar[0]=str(pixel_ar[0])+str(i)
        elif k<5: pixel_ar[1]=str(pixel_ar[1])+str(i)
        else: pixel_ar[2]=str(pixel_ar[2])+str(i)
        k+=1
    pixel_ar[0] = compare_sum(pixel[0], int(pixel_ar[0], 2))
    pixel_ar[1] = compare_sum(pixel[1], int(pixel_ar[1], 2))
    pixel_ar[2] = compare_sum(pixel[2], int(pixel_ar[2], 2))
    return [pixel_ar[0], pixel_ar[1], pixel_ar[2]]

def encode(adressLoad, adressSave,textValue,filename):
    img = Image.open(adressLoad)
    img = img.convert('RGB')
    siz = img.size
    if(len(adressLoad)<siz[0]):
        x=len(adressLoad)
        y=1
    else:
        x=siz[0]
        y=math.ceil(len(adressLoad)/siz[0])
    cnt=0
    for i in range(x):
        for j in range(y):
            if cnt < len(textValue):
                r=int(cyPixel(img.getpixel((i, j)),textValue[cnt])[0])
                g=int(cyPixel(img.getpixel((i, j)),textValue[cnt])[1])
                b=int(cyPixel(img.getpixel((i, j)),textValue[cnt])[2])
                cnt+=1
                img.putpixel((i, j), ((r, g, b)))
            else:
                adress=str(adressSave)+'/'+str(filename)

                img.save(adress)
                print(adress)
                return