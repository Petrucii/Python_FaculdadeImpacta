# Programa que lê um valor em GigaBytes e mostre o valor convertido em MegaBytes. A fórmula para converter de GigaBytes para MegaBytes é: MB = GB * 1024, onde MB é o valor em MegaBytes e GB é o valor em GigaBytes.

GB = float(input('Digite um valor qualquer em GigaBytes: '))
MB = GB * 1024
KB = GB * 1_000_000

print(f'O valor de {GB} GigaBytes, convertido para MegaBytes, é de: {MB} MegaBytes.')

print(f'E o valor de {GB} GigaBytes, convertido para KiloBytes, é de: {KB} KiloBytes!')