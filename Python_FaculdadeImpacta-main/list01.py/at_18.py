# Programa que lê o tamanho do download em MegaBytes e a velocidade da internet em MegaBits por segundo, e mostre o tempo estimado para o download em minutos. A fórmula para calcular o tempo de download é: Tempo (em minutos) = (Tamanho do Download (em MB) * 8) / Velocidade da Internet (em Mbps) / 60, onde MB é o tamanho do download em MegaBytes, Mbps é a velocidade da internet em MegaBits por segundo, e 60 é o número de segundos em um minuto.

MB = float(input('Digite o tamanho do seu Download em MegaBytes: '))
mbps = float(input('Digite a velocidade da sua internet em MegaBits por segundo: '))

tempo_download = (MB * 8) / mbps / 60

print(f'O tempo estimado para o download é de {tempo_download:.2f} minutos.')
