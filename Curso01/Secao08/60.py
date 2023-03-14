from random import randint

texto = """Lorem ipsum dolor sit amet consectetur adipiscing elit Sed consequat tincidunt erat nec cursus metus feugiat non Suspendisse a nulla efficitur felis mattis accumsan Nunc id facilisis eros ac pellentesque ipsum In hac habitasse platea dictumst""".lower().split()

def sub_string(txt:str):
    
    if txt in texto:
        for i in range(len(texto)):
            if txt in texto[i]:
                return i
    else:
        return -1


txt = input('Digite a palavra que deseja procurar: ')
print(sub_string(txt))