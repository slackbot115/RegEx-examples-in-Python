import re

op = int(input("Digite a opcao que deseja realizar:\n1 - Verificar IPs\n2 - Verificar DDD\n3 - Verificar CPF\n"))

if op == 1:
    regex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

    insertBy = int(input("Deseja inserir de que forma?:\n1 - Unico valor\n2 - Insercao de arquivo\n"))

    if insertBy == 1:
        check_str = str(input("Digite o endereco IP: "))

        matches = re.finditer(regex, check_str, re.MULTILINE)
        
        for matchNum, match in enumerate(matches, start=1):
            print ("IP valido: {match}".format(match = match.group()))
            exit()
        print("IP invalido...")

    if insertBy == 2:
        for i, line in enumerate(open("ips.txt")):
            for match in re.finditer(regex, line):
                print("IP identificado: {match}".format(match = match.group()))
if op == 2:
    regex = r"^(\([0-9]{2}\)|[0-9]{2})$"

    insertBy = int(input("Deseja inserir de que forma?:\n1 - Unico valor\n2 - Insercao de arquivo\n"))

    if insertBy == 1:
        check_str = str(input("Digite o DDD: "))

        matches = re.finditer(regex, check_str, re.MULTILINE)
        
        for matchNum, match in enumerate(matches, start=1):
            print ("DDD valido: {match}".format(match = match.group()))
            exit()
        print("DDD invalido...")

    if insertBy == 2:
        for i, line in enumerate(open("ddd.txt")):
            for match in re.finditer(regex, line):
                print("DDD identificado: {match}".format(match = match.group()))
if op == 3:
    regex = r"^[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}"

    insertBy = int(input("Deseja inserir de que forma?:\n1 - Unico valor\n2 - Insercao de arquivo\n"))

    if insertBy == 1:
        check_str = str(input("Digite o CPF: "))

        matches = re.finditer(regex, check_str, re.MULTILINE)
        
        for matchNum, match in enumerate(matches, start=1):
            print ("CPF valido: {match}".format(match = match.group()))
            exit()
        print("CPF invalido...")

    if insertBy == 2:
        for i, line in enumerate(open("cpf.txt")):
            for match in re.finditer(regex, line):
                print("CPF identificado: {match}".format(match = match.group()))
