from base64 import b64decode, b64encode
from random import randint

def adFly_decoder(sc):
    return b64decode(b64decode(sc[::2] + sc[::-2])[26:]) or "Invalid"
    
def adFly_encoder(url):
    temp = b64encode("{:02d}https://adf.ly/go.php?u={}".format(randint(0, 99), b64encode(url)))
    return ''.join(x+y for x,y in zip(temp[:len(temp)//2+1], temp[:len(temp)//2-1:-1]))