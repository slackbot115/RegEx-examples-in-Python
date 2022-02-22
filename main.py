import re
import os
import time

leave = True
while(leave is not True):
    op = int(input("Digite a opcao que deseja realizar:\n1 - Verificar IPs\n2 - Verificar DDD\n3 - Verificar CPF\n0 - Fechar\n"))

    if op == 1:
        regex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

        a = True
        while(a):
            insertBy = int(input(
                "Deseja inserir de que forma?:\n1 - Unico valor\n2 - Insercao de arquivo\n0 - Para voltar\n"))
            if insertBy == 1:
                check_str = str(input("Digite o endereco IP: "))

                if re.search(regex, check_str) is not None:
                    for thing in re.finditer(regex, check_str):
                        print('IP valido: ' + thing[0])
                else:
                    print('IP invalido...')
                time.sleep(1)
            if insertBy == 2:
                print("Exibindo arquivos...")
                for file in os.listdir():
                    if file.endswith(".txt"):
                        print(file)
                filename = str(
                    input("Digite o nome do arquivo desejado(sem a extensao): "))
                try:
                    for i, line in enumerate(open("{}.txt".format(filename))):
                        for match in re.finditer(regex, line):
                            print("IP identificado: {match}".format(
                                match=match.group()))
                    time.sleep(1)
                except Exception as e:
                    print("Erro: " + e)
            if insertBy == 0:
                break
    if op == 2:
        regex = r"^(\([0-9]{2}\)|[0-9]{2})$"

        a = True
        while(a):
            insertBy = int(input(
                "Deseja inserir de que forma?:\n1 - Unico valor\n2 - Insercao de arquivo\n0 - Para voltar\n"))

            if insertBy == 1:
                check_str = str(input("Digite o DDD: "))

                if re.search(regex, check_str) is not None:
                    for thing in re.finditer(regex, check_str):
                        print('DDD valido: ' + thing[0])
                else:
                    print('DDD invalido...')
                time.sleep(1)
            if insertBy == 2:
                print("Exibindo arquivos...")
                for file in os.listdir():
                    if file.endswith(".txt"):
                        print(file)
                filename = str(
                    input("Digite o nome do arquivo desejado(sem a extensao): "))
                try:
                    for i, line in enumerate(open("{}.txt".format(filename))):
                        for match in re.finditer(regex, line):
                            print("DDD identificado: {match}".format(
                                match=match.group()))
                    time.sleep(1)
                except Exception as e:
                    print("Erro: " + e)
            if insertBy == 0:
                break
    if op == 3:
        regex = r"^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}"

        a = True
        while(a):
            insertBy = int(input(
                "Deseja inserir de que forma?:\n1 - Unico valor\n2 - Insercao de arquivo\n0 - Para voltar\n"))

            if insertBy == 1:
                check_str = str(input("Digite o CPF: "))

                if re.search(regex, check_str) is not None:
                    for thing in re.finditer(regex, check_str):
                        print('CPF valido: ' + thing[0])
                else:
                    print('CPF invalido...')
                time.sleep(1)
            if insertBy == 2:
                print("Exibindo arquivos...")
                for file in os.listdir():
                    if file.endswith(".txt"):
                        print(file)
                filename = str(
                    input("Digite o nome do arquivo desejado(sem a extensao): "))
                try:
                    for i, line in enumerate(open("{}.txt".format(filename))):
                        for match in re.finditer(regex, line):
                            print("CPF identificado: {match}".format(
                                match=match.group()))
                    time.sleep(1)
                except Exception as e:
                    print("Erro: " + e)
            if insertBy == 0:
                break
    if op == 0:
        exit()
