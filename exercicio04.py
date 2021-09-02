premio = float(input("Digite aqui o premio do bolão total: "))
descontobanco = (premio/100)*7
premiototal = premio - descontobanco
premio1 = premiototal*0.46
premio2 = premiototal*0.32
premio3 = premiototal*0.22
print("O valor total do premio é de {}, com o desconto de {} do banco ficará um total de {}, com isso o primeiro ganhador vai ganhar {}, o segundo {} e o terceiro {} ".format(premio,descontobanco,premiototal,premio1,premio2,premio3))
