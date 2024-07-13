#  Leitura e escrita de arquivos

with open('arquivo.txt','w') as file:
    file.write('Olá, mundo!')

with open('arquivo.txt','r') as file:
    conteudo = file.read()
print(conteudo)

# primeira parte eu coloco uma escrita ena segunda faço a leitura pedindo o conteúdo.