import random

bandas_rock = {'queen': ['Radio Gaga', 'the show must go on', 'dust'], 'system of a down': ['byob', 'aerials'],
               'iron maiden': ['fear of the dark', 'the number of the beast', 'run to the hills',
                               'alexander the great']}

ativo = 0
while ativo == 0:
    print()
    print('Esse é um jogo de adivinhação, popularmente conhecido como FORCA, para começar, escolha um tema entre:')
    print('1 - Música')
    print('2 - Banda')
    print('3 - ')
    print('4 - Filme')
    print('5 - Série')
    print('6 - Anime')
    print()
    print('IMPORTANTE: Você terá 5 CHANCES para acertar!')
    print()
    tema = input('Digite o número correspondente ao Tema escolhido: ')

    if not tema.isnumeric():
        print('Erro! O valor digitado não é um número, vamos começar novamente.')
        continue
    tema = int(tema)

    if tema == 1:
        print()
        print('Agora escolha o número do seu subtema, entre:')
        print('1 - Queen')
        print('2 - System of a down')
        print('3 - Iron Maiden')
        print('4 - Rosa de Saron')
        subtema = input('Digite o número correspondente ao Sub-Tema escolhido: ')

        if not subtema.isnumeric():
            print('Erro! O valor digitado não é um número, vamos começar novamente.')
            continue
        subtema = int(subtema)

        if subtema == 1:
            print()
            lista1 = bandas_rock['queen']
            secreto = random.choice(lista1)
            secreto = secreto.upper()
            contagem = len(secreto)
            # print('Em processo de testes, estamos sem dicas, porém a banda é queen')
            # print('Dica: Essa música, foi uma das ultimas produzidas pela banda e o vocalista bebeu uma garrafa '
            #      'de VODKA inteira, para conseguir gravar ela.')
            # print('Banda Britânica')
            # print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 2:
            print()
            lista1 = bandas_rock['system of a down']
            secreto = random.choice(lista1)
            secreto = secreto.upper()
            contagem = len(secreto)
            # print('Dica: Essa música é da Rainha da Sofrência.')
            # print('Cantora Brasileira')
            # print()
            # print(f'Sua palavra tem {contagem} letras')
        elif subtema == 3:
            print()
            lista1 = bandas_rock['iron maiden']
            secreto = random.choice(lista1)
            secreto = secreto.upper()
            contagem = len(secreto)
            # print('Dica: Essa música tem uma história, onde a fã enviou uma carta falando .')
            # print('Cantor Americano')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 4:
            print()
            secreto = 'Noites traçoeiras'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Hino nacional do padre Marcelo')
            print('Cantor Brasileiro')
            print()
            print(f'Sua palavra tem {contagem} letras')
        else:
            print('Digite um número de 1 à 4, por favor.')
            continue

    elif tema == 2:
        print()
        print('Agora escolha o subtema, entre:')
        print('1 - Rock')
        print('2 - Sertanejo')
        print('3 - Pop')
        print('4 - Gospel')
        subtema = input('Digite o número correspondente ao Sub-Tema escolhido: ')

        if not subtema.isnumeric():
            print('Erro! O valor digitado não é um número, vamos começar novamente.')
            continue
        subtema = int(subtema)

        if subtema == 1:
            print()
            secreto = random.choice(list(bandas_rock))
            secreto = secreto.upper()
            contagem = len(secreto)
            print(f'sua banda tem {contagem} letras')

        elif subtema == 2:
            print()
            secreto = 'Inevitavel'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Esse album é sofrência raiz, e a clássica "DEIXA" faz parte dele.')
            print('Dupla Brasileira')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 3:
            print()
            secreto = 'Thriller'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Billie Jean faz parte desse albúm.')
            print('Cantor Americano')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 4:
            print()
            secreto = 'Horizonte Distante'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Depois do sucesso dos seus acústicos, a banda Rosa de Saron entrou com tudo com esse novo '
                  'albúm')
            print('Banda Brasileira')
            print()
            print(f'Sua palavra tem {contagem} letras')
        else:
            print('Digite um número de 1 à 4, por favor.')

    if tema == 3:
        print()
        print('Agora escolha o subtema, entre:')
        print('1 - Rock')
        print('2 - Sertanejo')
        print('3 - Pop')
        print('4 - Gospel')
        subtema = input('Digite o número correspondente ao Sub-Tema escolhido: ')

        if not subtema.isnumeric():
            print('Erro! O valor digitado não é um número, vamos começar novamente.')
            continue
        subtema = int(subtema)

        if subtema == 1:
            print()
            secreto = 'Iron Maiden'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Somewhere in time, um dos melhores albuns de heavy metal, lançando em 1986 por essa banda'
                  'clássica de METAL.')
            print('Banda Britânica')
            print()
            print(f'Sua palavra tem {contagem} letras')

        elif subtema == 2:
            print()
            secreto = 'Zeze di Camargo e Luciano'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Melhor música dessa dupla é Pra mudar minha vida')
            print('Dupla Brasileira')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 3:
            print()
            secreto = 'Beyonce'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Rainha do pop, sucesso absoluto com a música Halo!')
            print('Cantora Americana')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 4:
            print()
            secreto = 'Rosa de Saron'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Sem você, a música mais famosa da banda, antigindo as rádios NACIONAIS.')
            print('Banda Brasileira')
            print()
            print(f'Sua palavra tem {contagem} letras')
        else:
            print('Digite um número de 1 à 4, por favor.')

    if tema == 4:
        print()
        print('Agora escolha o subtema, entre:')
        print('1 - Suspence')
        print('2 - Ação')
        print('3 - Comédia')
        print('4 - Clássicos')
        subtema = input('Digite o número correspondente ao Sub-Tema escolhido: ')

        if not subtema.isnumeric():
            print('Erro! O valor digitado não é um número, vamos começar novamente.')
            continue
        subtema = int(subtema)

        if subtema == 1:
            print()
            secreto = 'Memento'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Nesse filme o ator principal perde a memória, e ele só tem lembraças através de suas '
                  'tatuagens')
            print('Nome do filme em Inglês')
            print()
            print(f'Sua palavra tem {contagem} letras')

        elif subtema == 2:
            print()
            secreto = 'Matrix'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Esse filme mudou os rumos de efeitos especias e as pessoas vivem em outra realidade.')
            print('Nome do filme em Inglês')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 3:
            print()
            secreto = 'Ace Ventura'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Filme de um veterinário muito louco.')
            print('Nome do filme em Inglês')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 4:
            print()
            secreto = 'The Shawshank Redemption'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Filme sobre liberdade e esperança, com partipação mais que especial de Morgan Freeman')
            print('Nome do filme em Inglês')
            print()
            print(f'Sua palavra tem {contagem} letras')
        else:
            print('Digite um número de 1 à 4, por favor.')

    if tema == 5:
        print()
        print('Agora escolha o subtema, entre:')
        print('1 - Suspence')
        print('2 - Ação')
        print('3 - Comédia')
        print('4 - Fantasia')
        subtema = input('Digite o número correspondente ao Sub-Tema escolhido: ')

        if not subtema.isnumeric():
            print('Erro! O valor digitado não é um número, vamos começar novamente.')
            continue
        subtema = int(subtema)

        if subtema == 1:
            print()
            secreto = 'Breaking Bad'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Professor de química, que entra no mudo do tráfico')
            print('Nome da série em Inglês')
            print()
            print(f'Sua palavra tem {contagem} letras')

        elif subtema == 2:
            print()
            secreto = 'Prision Break'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: A série com um dos melhores planos já elaborados e executados')
            print('Nome da série em Inglês')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 3:
            print()
            secreto = 'Friends'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Série que se passa em Manhattan nos anos 90.')
            print('Nome da série em Inglês')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 4:
            print()
            secreto = 'Game of Thrones'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Série sobre guerra e poder')
            print()
            print(f'Sua palavra tem {contagem} letras')
        else:
            print('Digite um número de 1 à 4, por favor.')

    if tema == 6:
        print()
        print('Agora escolha o subtema, entre:')
        print('1 - Cyberpunk')
        print('2 - Viagem no tempo')
        print('3 - Comédia')
        print('4 - Simbolismo e filosofia')
        subtema = input('Digite o número correspondente ao Sub-Tema escolhido: ')

        if not subtema.isnumeric():
            print('Erro! O valor digitado não é um número, vamos começar novamente.')
            continue
        subtema = int(subtema)

        if subtema == 1:
            print()
            secreto = 'Pyscho Pass'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Acontece num mundo futurístico, onde sua vida e escolhas são julgada pela tecnologia')
            print('Nome do anime Origial')
            print()
            print(f'Sua palavra tem {contagem} letras')

        elif subtema == 2:
            print()
            secreto = 'Steins Gate'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Um laboratório pequeno, desbore váris situações sobre laço no tempo')
            print('Nome do anime Origial')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 3:
            print()
            secreto = 'One Punch Man'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Ele treinou vários anos, até que ficou careca')
            print('Nome do anime Origial')
            print()
            print(f'Sua palavra tem {contagem} letras')
        elif subtema == 4:
            print()
            secreto = 'Evangelion'
            secreto = secreto.upper()
            contagem = len(secreto)
            print('Dica: Anime que trouxe a cultura de anime para o ociente, cheio de simbolismo Gnóstico')
            print('Nome do anime Origial')
            print()
            print(f'Sua palavra tem {contagem} letras')
        else:
            print('Digite um número de 1 à 4, por favor.')

    chances = 5
    digitadas = [' ']
    letras_armazenadas = []
    ativo1 = 0

    while ativo1 == 0:
        if chances <= 0:
            print('Você perdeu!!!')
            print()
            finalizar = input('Deseja tentar novamente? Sim ou Não: ')
            finalizar = finalizar.lower()
            if finalizar == 'sim' or finalizar == 's':
                print('Vou lhe dar mais uma chance')
                chances = 1
                continue
            else:
                print('): música triste')
                ativo = 1
                break
        print()
        letra = input('Digite uma letra: ')
        letra = letra.upper()

        if len(letra) > 1:
            print()
            print('Ahhh isso não vale, digite apenas uma letra.')
            continue

        digitadas.append(letra)

        if letra not in letras_armazenadas:
            letras_armazenadas.append(letra)

        if letra in secreto:
            print()
            print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
        else:
            print()
            print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
            digitadas.pop()

        if letra not in secreto:
            chances -= 1
            print()
            print(f'Você ainda tem {chances} chances.')

        secreto_temporario = ''

        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '*'

        secreto_temporario = secreto_temporario.upper()
        secreto = secreto.upper()

        print(f'Sua palavra está assim: {secreto_temporario}')
        if letra in secreto:
            chutar = input('Deseja chutar a palavra ? Sim ou não: ')
            if chutar == 's' or chutar == 'sim':
                chute = input('Digite seu chute aqui: ')
                chute = chute.upper()
                if chute == secreto:
                    print()
                    print(f'Que legal, VOCÊ GANHOU!!! A palavra é {secreto}.')
                    print()
                    finalizar2 = input('Deseja advinhar outra palavra? Sim ou não: ')
                    finalizar2 = finalizar2.lower()
                    if finalizar2 == 'sim' or finalizar2 == 's':
                        print()
                        ativo1 = 1
                    else:
                        print('Obrigado e volte sempre (:')
                        ativo1 = 1
                        break
                else:
                    print('ERROU!!!! Continue tentando!')
                    continue
        if secreto_temporario == secreto:
            print()
            print(f'Que legal, VOCÊ GANHOU!!! A palavra é {secreto_temporario}.')
            print()
            finalizar1 = input('Deseja advinhar outra palavra? Sim ou não: ')
            finalizar1 = finalizar1.lower()
            if finalizar1 == 'sim' or finalizar1 == 's':
                print()
                ativo1 = 1
            else:
                print('Obrigado e volte sempre (:')
                ativo1 = 1
                break
        else:
            print()
            print(f'A palavra secreta está assim: {secreto_temporario}')
            print(f'e você digitou essas letras até agora {letras_armazenadas}')
            print('')
