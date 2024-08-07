mensagem = input("Digite a mensagem: ")
chave = input("Digite a chave: ".lower())

chavecompr = 0
mensagem_cript = ""

for x in mensagem:
    if x.isalpha():                  
        ordem = ord(chave[chavecompr % len(chave)]) - ord('a')
        
        if x.islower():
            mensagem_cript+= chr((ord(x) - ord('a') + ordem) % 26 + ord('a'))                 
        elif x.isupper():
            mensagem_cript += chr((ord(x) - ord('A') + ordem) % 26 + ord('A'))          
        chavecompr+= 1
        
    else:
        mensagem_cript += x  

print("Mensagem criptografada:", mensagem_cript)

'''Descriptografando
a mensagem'''

mensagem_decript = ""
chavecompr = 0

for i in mensagem_cript:
    if i.isalpha():  
        ordem = ord(chave[chavecompr % len(chave)]) - ord('a')
        
        if i.islower():
            mensagem_decript += chr((ord(i) - ord('a') - ordem) % 26 + ord('a'))
        elif i.isupper():
            mensagem_decript += chr((ord(i) - ord('A') - ordem) % 26 + ord('A'))
        chavecompr += 1
        
    else:
        mensagem_decript += i  
print("Mensagem descriptografada:", mensagem_decript)