# Criação de uma lista de tarefas

tarefas = ['Tomar banho','Tomar café','Se exercitar','Passear com os pets','Ir para o trabalho']

# Transformar a lista em uma string separada por vírgulas

string_com_virgulas = ', '.join(tarefas)
print(string_com_virgulas)

# Transformar a lista em uma string com cada item em uma nova linha

string_com_novas_linhas = '\n'.join(tarefas)
print(string_com_novas_linhas)

# Adicionando hífen a cada item

nova_lista = []
for item in tarefas:
    nova_lista.append(f'- {item}')

print(nova_lista)

string_com_hifens = '\n'.join(nova_lista)
print(string_com_hifens)

# Nome do arquivo

nome_do_arquivo = 'tarefas.txt'

with open(nome_do_arquivo,'w',encoding="utf-8") as file:
    file.write(string_com_hifens)


with open(nome_do_arquivo,'r') as file:
    arquivo = file.read()

print(tarefas)

# Remoção da acentuação da palavra

