import sympy 
import random


class RSA :
    def __init__(self,length):
        self.length = length
        self.KPb,self.KPr = self.generate_keys()
    
    def generate_prime_pairs(self):
        lower_limit = 2**((self.length//2)-1)
        upper_limit = 2**(self.length//2) -1 
        p = sympy.randprime(lower_limit,upper_limit)
        q = sympy.randprime(lower_limit,upper_limit)

        while p==q:
            q = sympy.randprime(lower_limit,upper_limit)
        return (p,q)
    
    def generate_keys(self):
        p,q = self.generate_prime_pairs()
        n = p*q
        phi = (p-1)*(q-1)
        while True:
            e = random.randint(1,phi-1)
            if sympy.gcd(e,phi) == 1:
                break
        d = sympy.mod_inverse(e,phi)

        return ((e,n),(d,n))
    
    def segment_text(self,text):
        bytes = text.encode('utf-8')
        segment_size = self.length // 8
        segments = []
        for i in range(0,len(bytes),segment_size):
            segment = bytes[i:i+segment_size]
            if len(segment) < segment_size:
                segment += b'\0' * (segment_size - len(segment))
            hex_segment = segment.hex()
            decimal_segment = int(hex_segment, 16)
            segments.append(decimal_segment)
        return segments
    

    def encrytpt(self,message):
        data = self.segment_text(message)
        cipher = []
        for x in data:
            c = pow(x,self.KPr[0],self.KPr[1])
            cipher.append(c)
        return cipher
    
    def decrypt(self,cipher):
        message = []
        text = []
        for c in cipher:
            x = pow(c,self.KPb[0],self.KPb[1]) 
            message.append(x)
        
        for x in message:
            hex_string = hex(x)[2:]
            if len(hex_string) % 2 != 0:
                hex_string = '0' + hex_string
            byte_data = bytes.fromhex(hex_string)
            utf8_string = byte_data.decode('utf-8', errors='ignore')
            text.append(utf8_string)
        return ''.join(text)
    

if __name__=='__main__':
    pass
            








