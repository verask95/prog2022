A = 3
B = 16

NOME = 'MIRIAM'

PROF = 'ADVOGADO'


a = (A + 1 >= (B ** (1/2))) or (NOME != 'ANA')
b = (A + 1 >= (B ** (1/2))) and (PROF == 'MEDICO')
c = (NOME != 'ANA') or (PROFISSAO == 'MEDICO') and (A + 1 >= (B ** (1/2)))
d = not 'TESTE' and (( A + 1 ) >= (B ** (1/2))) or not (PROF == 'MEDICO')
e = not ((A + 1 >= (B ** (1/2))) and 'TESTE')

print (a)
print (b)
print (c)
print (d)
