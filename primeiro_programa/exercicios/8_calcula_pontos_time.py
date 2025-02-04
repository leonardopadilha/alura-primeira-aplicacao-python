# Calcule a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos
# em cada jogo. Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de
# números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato.
# A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração
# que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcula_pontos(gols_marcados, gols_sofridos):
  pontos = 0
  for i in range(len(gols_marcados)):
    if gols_marcados[i] > gols_sofridos[i]:
      pontos += 3
    elif gols_marcados[i] == gols_sofridos[i]:
      pontos += 1
  aprov = 100 * pontos / (len(gols_marcados) * 3)
  return (pontos, aprov)

pontos, aprov = calcula_pontos(gols_marcados, gols_sofridos)
print(f"A pontuação do time foi de {pontos} e seu aproveitamento foi de {aprov}%")