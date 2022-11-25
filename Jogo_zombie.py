from cgi import print_arguments
import random	
print("ZOMBIE DICE (Prototipo Semana 4) ");
print("Seja bem-vindo ao jogo Zombie Dice!");
numJogadores = 0;
score = [];
while numJogadores < 2:	
	numJogadores = int(input("Informe a quantidade de jogadores: "));
	if numJogadores < 2:
		print("AVISO: Voce precisa de pelo menos 2 jogadores!");
#aqui vai ser definido quantos jogadores serão na partida

listaJogadores = []; #aqui é a lista da quantidade dos jogadores
for i in range(numJogadores): #Aqui é a nomeclatura dos jogadores, onde começará do 1, nomeando-os com o "for" até atribuir os nomes a todos os jogadores da variável numJogadores
  print("Informe o nome do jogador ",(i+1) ,": ");
  nome = input();
  score.append(0);
  listaJogadores.append(nome);
  #para ir adicionando a lista o nome dos jogadores
  listaJogadores[i] = nome; 

dadoVerde = "CPCTPC";
dadoAmarelo = "TPCTPC";
dadoVermelho = "TPTCPT";

#Definido as variáveis que cada face do dado terá
listaDados = [
					dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,dadoVerde,
					dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo,
					dadoVermelho,dadoVermelho,dadoVermelho
	];

print("INICIANDO O JOGO...");
scoreJogador = [];
jogadorAtual = 0;
dadosSorteados = [];
tiros = 0;
cerebros = 0;
passos = 0;
pontua = 0;
listaGa = [];
for i in range(numJogadores):
  listaGa.append(0);
print(listaGa)
while True: 
  print("TURNO DO JOGADOR ", listaJogadores[jogadorAtual]);
  for i in range(0,3,1):
    numSorteado = random.randint(0, 12); 
    dadoSorteado = listaDados[numSorteado]; 
    if dadoSorteado == "CPCTPC":
      corDado = "VERDE";
    elif dadoSorteado == "TPCTPC":
      corDado = "AMARELO";
    else:
      corDado = "VERMELHO";
    print("Dado sorteado: ", corDado);
    dadosSorteados.append(dadoSorteado);
  print("As faces sorteadas foram: ")
  for dadoSorteado in dadosSorteados: 
    numFaceDado = random.randint(0, 5);
    if dadoSorteado[numFaceDado] == "C":
      print("- CEREBRO (voce comeu um cerebro)");
      cerebros = cerebros + 1;
    elif dadoSorteado[numFaceDado] == "T":
      print("- TIRO (voce levou um tiro)");
      tiros = tiros + 1;
    else:
      print("- PASSOS (uma vitima escapou)");
      passos = passos + 1;
  print("SCORE ATUAL: ");
  print("CEREBROS: ", cerebros);
  print("TIROS: ", tiros);
  VerificadorT = True;
  if tiros >= 3:
    print("AVISO: você perdeu seu score");
    dadosSorteados = [];
    tiros = 0;
    cerebros = 0;
    passos = 0;
    if jogadorAtual == len(listaJogadores) - 1:
      jogadorAtual = 0; 
      continuarJogando = input("AVISO: todos os jogadores querem jogar mais uma rodada? (s=sim / n=nao)");
      if continuarJogando == 's':
        continue;
      else:
        VerificadorT = False;
    else:
      jogadorAtual = jogadorAtual + 1;
    #####Precisa de um verificador para passar, talvez um if len para pular essa parte da repetição e ir para o próximo código####
  else:
    VerificadorV = cerebros + score[jogadorAtual];
    if VerificadorV >= 5:
      print("Você atingiu o placar para ganhar, com: " + str(VerificadorV)); 
      listaGa[jogadorAtual] = VerificadorV;
      pontua = cerebros;
      Tpontua = score[jogadorAtual] + pontua;
      score[jogadorAtual] = Tpontua;
      print("sua pontuação atual é: " + str(score[jogadorAtual]));
      jogadorAtual = jogadorAtual + 1;
      dadosSorteados = [];
      tiros = 0;
      cerebros = 0;
      passos = 0;
      pontua = 0;
    else:
      continuarTurno = input("AVISO: Voce deseja continuar jogando dados? (s=sim / n=nao)");
      if continuarTurno == 'n':
        pontua = cerebros;
        Tpontua = score[jogadorAtual] + pontua;
        score[jogadorAtual] = Tpontua;
        print("sua pontuação atual é: " + str(score[jogadorAtual]));
        jogadorAtual = jogadorAtual + 1;
        dadosSorteados = [];
        tiros = 0;
        cerebros = 0;
        passos = 0;
        pontua = 0;
  if VerificadorT == False:
    print("Finalizando prototipo do jogo...");
    break; 
  else:  
    
    
##acho que preciso mudar essa parte para uma separada onde as variáveis se encaixam de uma forma mais decente
    #colocar um if com o VerificadorV para poder ver se alguém passou da pontuação de marco, se mais de uma pessoa passar, será feito o algorítimo para um comparativo talvez?
      if jogadorAtual == len(listaJogadores):
        continuarJogando = input("AVISO: todos os jogadores querem jogar mais uma rodada? (s=sim / n=nao)");
        if (continuarJogando == 's'):
          print("Iniciando mais um turno");
          print(jogadorAtual);
          jogadorAtual = 0;
          continue;
        else:
          print("Finalizando prototipo do jogo...");
          break;        
      else:
        print("Iniciando mais uma rodada do turno atual...");
      dadosSorteados = [];


jogadorAtual = 0;
for i in range (numJogadores):
  print("o jogador: " + str(listaJogadores[jogadorAtual]) + " fez esta pontuação: " +  str(score[jogadorAtual]));  
  jogadorAtual = jogadorAtual + 1;
##  O QUE FAZER?  ##
# criar uma opção para ver os dados que estão no copo
# criar uma forma de que os dados que cairam passos sejam re-rolados
# utilizar a tupla para mostrar o resultado final, fazendo a junção de nome de jogador e o score.
print(listaGa);


