A = float(input('VALOR DE A:'))
B = float(input('VALOR DE B:'))

NOME = str(input('NOME:'))
TESTE = False
PROF = str(input('PROFISSÃO:'))

###REALIZANDO AS OPERAÇÕES###
a = (A + 1 >= (B ** (1/2))) or (NOME != 'ANA')
b = (A + 1 >= (B ** (1/2))) and (PROF == 'MEDICO')
c = (NOME != 'ANA') or (PROF == 'MEDICO') and (A + 1 >= (B ** (1/2)))
d = not TESTE and (( A + 1 ) >= (B ** (1/2))) or not (PROF == 'MEDICO')
e = not ((A + 1 >= (B ** (1/2))) and TESTE)

###IMPRIMINDO RESULTADOS###
print (a)
print (b)
print (c)
print (d)
print (e)
