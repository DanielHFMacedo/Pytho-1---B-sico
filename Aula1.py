# Aula 1 Variáveis

# Tipos primitivos : int, bool, float, str
# Pode conter letras e números
# Não pode começar com número
# Não pode conter caracteres especiais ( | ! ´ ^ ~ ' ")
# Não pode ter nome igual a palavra reservada

# Declaração : nome_da_variavel=valor

altura=1.75
nome="Daniel Macêdo"
idade=25
permissao=True

# utilizamos comando print para imprimir os valores das variáveis

print("Altura=",altura)
print("Nome=",nome)
print("Idade",idade)
print("Permissão",permissao)

# tipos

print("Tipo da variável altura=",type(altura))
print("Tipo da variável nome=",type(nome))
print("Tipo da variável idade=",type(idade))
print("Tipo da variável permissão=",type(permissao),"\n")
# Usamos "texto" para escrever um texto no print
# Para imprimir uma variável entre 2 textos separamos por vírgula (,)
# Usamos "\n" para pular uma linha

# Em python não é necessário declarar o tipo da váriável antes do seu nome
# também não é necessário utilizar " ; " no final da linha de código como na linguagem C
# A identação não utiliza { } como na linguagem C mas o TAB é reconhecido como identação.

# Um algorítmo se trata de um procedimento ordenado para resolver um problema
# Envolve entrada, processamento e saída
# Exemplo:

#entrada
salario_base=2000
gratificacao=50

#processamento
salario_bruto= salario_base+gratificacao

#saida
print("Salário bruto=",salario_bruto)

#utilizamos o comando input para o usuário digitar um valor

#entrada
salario_base=float(input("Digite o valor do salário base "))
# Se você não definir o tipo primitivo no input ele vai dizer que é um dado string
# Por isso utilizamos float() para resolver o problema
gratificacao=float(input("Digite o valor da gratificação "))

#processamento
salario_bruto= salario_base+gratificacao

#saida
print("Salário bruto=",salario_bruto)

# Operadores Aritméticos (+, -, *, /, //, **, %)

print("2+2=",2+2)
print("3-2",3-2)
print("2*5",2*5)
print("2 elevado a 5 potência=",2**5)
print("16/3=",16/3) # Mostra a divisão real de 16 por 5
print("16//3=",16//3) # Mostro a divisão inteira de 16 por 5
print("16%3=",16%3) # Mostra o resto da divisão de 16 por 5
