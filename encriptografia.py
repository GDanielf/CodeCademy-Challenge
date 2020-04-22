import string
import hashlib 


alphabet = list(string.ascii_lowercase)

def julio_decrypt(word,number):
    aux = ''
    for letter in word:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            aux += alphabet[letter_position - number]
        else:
            aux += letter    
    return aux.lower()

def hash_convertere(decifrado):
    resumo = hashlib.sha1(decifrado.encode('utf-8')).hexdigest().lower()
    return resumo
    
decifrado = julio_decrypt('qfpqmf uibu ibuf dbut xjmm dpnf cbdl bt njdf jo uifjs ofyu mjgf. gbjui sftojdl', 1)
hash_convertere(decifrado)

print(decifrado)
print(hash_convertere(decifrado))
