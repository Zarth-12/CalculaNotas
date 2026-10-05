from media_ponderada import calcular_media_ponderada

nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota3 = float(input("Digite a nota da terceira avaliação: "))

media = calcular_media_ponderada(nota1, nota2, nota3)

print(f"A média ponderada é: {media:.2f}")
