def calcularMediaPonderada(nota1, peso1, nota2, peso2):
    media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
    return media

nota1 = float(input('Digite a primeira nota:'))
peso1 = int(input('Digite o peso da primeira nota:'))

nota2 = float(input('Digite a segunda nota:'))
peso2 = int(input('Digite o peso da segunda nota:'))

media = calcularMediaPonderada(nota1, peso1, nota2, peso2)
print(f'A média ponderada é:{media:.2f}')
