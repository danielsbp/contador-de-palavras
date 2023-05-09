#from pprint import pprint as print
from unidecode import unidecode
import re
import os

while True:

    # Limpa o terminal
    os.system("cls")


    with open("texto.txt", "r", encoding="utf8") as file:
        
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
        