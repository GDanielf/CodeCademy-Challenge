import string
import requests
import json
import hashlib 

def julio_encrypt(word, number):
    aux = ''
    alphabet = list(string.ascii_lowercase)
    
    for letter in word:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            aux += alphabet[letter_position + number]
        else:
            aux += letter    
    return aux.lower()
    
def julio_decrypt(word,number):
    aux = ''
    alphabet = list(string.ascii_lowercase)
    for letter in word:
        if letter in alphabet:
            letter_position = alphabet.index(letter)
            aux += alphabet[letter_position - number]
        else:
            aux += letter    
    return aux.lower()
   
def EnviarResposta():
    answer_file = open("answer.json", "rb")
    url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=9d406396d926875dfc15f383655e3f33d9a90577'
    headers = { 'Content-Type': 'multipart/form-data' }
    result = requests.post(
        url, files={"answer": answer_file},headers = headers)
    print(result)
    
    
response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=9d406396d926875dfc15f383655e3f33d9a90577')
content_text = response.text
content_dict = json.loads(content_text)
content_dict['decifrado'] = julio_decrypt(content_dict['cifrado'],content_dict['numero_casas'])
resumo = hashlib.sha1(content_dict['decifrado'].encode('utf-8')).hexdigest().lower()
content_dict['resumo_criptografico'] = resumo


myfile = open('teste.txt','w+')
myfile.write(str(content_dict))
myfile.seek(0)
myfile.close()

out_file = open("answer.json", "w") 
json.dump(content_dict, out_file, indent = 4, sort_keys = False) 
out_file.close() 

EnviarResposta()

