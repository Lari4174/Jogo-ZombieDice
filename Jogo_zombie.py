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
#e aqui a quantidade de dados verdes, amarelos e vermelhos do jogo
print("INICIANDO O JOGO...");
scoreJogador = [];
jogadorAtual = 0;
dadosSorteados = [];
tiros = 0;
cerebros = 0;
passos = 0;

#aqui é setado as variáveis de pontuação de jogador
while True: #vai se repetir até ser forçadamente parado
  print("TURNO DO JOGADOR ", listaJogadores[jogadorAtual]);
  for i in range(0,3,1): #vai setar uma variável i, que começa em 1 e vai até 3 com o passo de 1 em 1, serve para sortear os dados do jogo
    numSorteado = random.randint(0, 12); #irá randomizar um dado a ser jogado e armazenará o valor no numdado
    dadoSorteado = listaDados[numSorteado]; # irá pegar da lista de dados e atriburi a vairável dadoSorteado
    if dadoSorteado == "CPCTPC":
      corDado = "VERDE";
    elif dadoSorteado == "TPCTPC":
      corDado = "AMARELO";
    else:
      corDado = "VERMELHO";
    #teste condicional para verificar qual cor do dado
    print("Dado sorteado: ", corDado);
    dadosSorteados.append(dadoSorteado);
    #irá adicionar o dado sorteado à lista de dadosSorteados
  print("As faces sorteadas foram: ")
  for dadoSorteado in dadosSorteados: #fará uma lista dos dados 
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
    #teste condicional para verificar em qual caractere caiu
  print("SCORE ATUAL: ");
  print("CEREBROS: ", cerebros);
  print("TIROS: ", tiros);
  if tiros >= 3:
    print("AVISO: você perdeu seu score");
    if jogadorAtual == len(listaJogadores):
      jogadorAtual = 0;
    jogadorAtual = jogadorAtual + 1;
    #e se for o último jogador ein ein ein ein?
    dadosSorteados = [];
    tiros = 0;
    cerebros = 0;
    passos = 0;
    continue;
    #####Precisa de um verificador para passar, talvez um if len para pular essa parte da repetição e ir para o próximo código####
  continuarTurno = input("AVISO: Voce deseja continuar jogando dados? (s=sim / n=nao)");
  if continuarTurno == 'n':
    pontua = cerebros;
    Tpontua = score[jogadorAtual] + pontua;
    score[jogadorAtual] = Tpontua;
    jogadorAtual = jogadorAtual + 1;
    dadosSorteados = [];
    tiros = 0;
    cerebros = 0;
    passos = 0;
    print(score);
    if jogadorAtual == len(listaJogadores):
      continuarJogando = input("AVISO: todos os jogadores querem jogar mais uma rodada? (s=sim / n=nao)");
      #colocar um for para a lista de jogadores imprimindo o score de cada um
      if (continuarJogando == 's'):
        print("Iniciando mais um turno");
        print(jogadorAtual);
        jogadorAtual = 0;
        continue;
      else:
        print("Finalizando prototipo do jogo...");
        break;
	#a partir do momento que todos os jogadores encerrarem o seu turno, o jogo encerra
  else:
    print("Iniciando mais uma rodada do turno atual...");
    dadosSorteados = [];
    #última condicional para verificar caso haja mais um turno a ocorrer
print(score);
##  O QUE FAZER?  ##
# criar o placar com tupla no final
#verificador de pontuação, quando atingir uma certa quantidade, criar um alerta sobre e que o jogo irá encerrar
# criar uma opção para ver os dados que estão no copo
# criar uma forma de que os dados não jogados sejam re-rolados
# utilizar a tupla para mostrar o resultado final, fazendo a junção de nome de jogador e o score.
#retirar da lista com o numerador do jogador, depois adicionar 
