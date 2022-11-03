##calculo de média ponderada

n1 = int(input ('Informe a sua primeira nota:'))

n2 = int(input('Informe a sua segunda nota:'))

media = (n1 *2 + n2 *3) /5

if media >= 60:
    print('Você esta aprovado!')
elif media < 20:
    print('Você esta reprovado!')
else:
    print('Você fará a prova final!')