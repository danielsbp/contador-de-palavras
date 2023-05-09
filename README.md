# Contador de Palavras
Simples contador de palavras em Python para a matéria de Arquiteturas Cloud de BDAg


## Explicação do código:

### 1 - 

- Com o texto em mãos, faço o processo de retirar acentos especiais com regex e deixo ele todo em minúsculo para não dar conflito entre "teste" e "Teste" por exemplo.
- Depois disso, separo as palavras com o .split(" ") e crio um objeto do tipo set() para gravar as palavras exatamente uma vez numa lista com elemento únicos
- Logo após, defino a frequência das palavras na linha 34 e ordeno com uma função anônima e o sorted na linha 38.
- Deixo tudo preparado somente para printar depois quando o usuário escolher.
 ```
texto = file.read()

texto_sem_acentuacao = unidecode(texto)
texto_sem_acentuacao_ou_especiais = re.sub('[^a-zA-Z0-9 \\\]', '', texto_sem_acentuacao).lower()

palavras = texto_sem_acentuacao_ou_especiais.split(" ")

quantidade_de_palavras = len(palavras)

frequencias = dict()

palavra_array_uniq = set()

# Monto uma lista com as palavras onde uma palavra só pode ser colocada uma vez nela.
for palavra in palavras:
    palavra_array_uniq.add(palavra)

# Monto o dicionário que terá as frequências de cada palavra
for palavra in list(palavra_array_uniq):
    frequencias[palavra] = 0

# Alimento o dicionário de frequências
for palavra in palavras:
    frequencias[palavra] += 1

palavras_ordenado = sorted(frequencias.items(), key=lambda x: x[1], reverse=True)


```
## 2 -
- Crio uma interface simples CLI para que o usuário escolha a função.
- Printo os elementos pedidos pelo usuário e depois limpo a tela
- Pergunto se ele deseja entrar em outro item do menu ou se quer fechar o script
```
print("-="*10)
        print("CONTADOR DE PALAVRAS")
        print("-="*10)

        print("")
        print(" 1 - Ver o texto escrito sem caracteres especiais ou acentos;")
        print(" 2 - Realizar a contagem de maneira decrescente;")
        print(" 3 - Selecionar as palavras para ver a frequência;")
        print(" 4 - Exibir a palavra mais usada e a menos usada.")


        acao = int(input("O que você deseja fazer?"))

        if acao == 1:
            os.system("cls")    
            print(texto_sem_acentuacao_ou_especiais)   
        elif acao == 2:

            os.system("cls")
            print(palavras_ordenado)

            

            

        elif acao == 3:
            palavras_input = input("Digite as palavras que você quer ver a frequência: (Separe por \",\")")

            palavras_escolhidas = palavras_input.lower().strip().replace(" ", "").split(",")

            for palavra_escolhida in palavras_escolhidas:
                if(palavra_escolhida in frequencias.keys()):
                    print("\"{}\" aparece {}x no texto ".format(palavra_escolhida, frequencias[palavra_escolhida]))
                else:
                    print("A palavra \"{}\" não existe no texto.".format(palavra_escolhida))



        elif acao == 4:
            
            palavra_mais_usada = palavras_ordenado[0]
            palavra_menos_usada = palavras_ordenado[-1]

            print("Palavra mais usada: {}".format(palavra_mais_usada))
            print("Palavra menos usada: {}".format(palavra_menos_usada))
        
        print("")
        print("-="*10)
        print("")
        
        print("1 - Voltar para o menu;")
        print("2 - Parar o script.")
        acao2 = int(input("O que deseja fazer? "))

        if acao2 == 1:
            continue
        elif acao2 == 2:
            quit()
```
