from unidecode import unidecode
import operator


def encriptaFrase(frase, chave):
    frase = unidecode(frase)  # Retira caracteres especiais
    frase = frase.lower()  # Deixa tudo minusculo

    for i in range(len(frase)):  # Percorre toda a frase
        frase = list(frase)  # Transforma a frase em lista

        if(ord(frase[i]) >= 97 and ord(frase[i]) <= 122-chave):  # Verifica o valor ASCII do caractere da lista
            frase[i] = chr(ord(frase[i]) + chave)  # Adiciona a chave para criptografar

        elif(ord(frase[i]) > 122-chave and ord(frase[i]) <= 122):
            frase[i] = chr(ord(frase[i]) - (26-chave))

    frase = "".join(frase)  # Torna a lista em string novamente
    return frase


def encriptaTexto(texto, chave):
    f = open(texto, "r", encoding="utf-8")  # Lê o arquivo texto
    frases = f.readlines()  # Divide as linhas do arquivo em uma lista
    for i in range(len(frases)):
        frases[i] = frases[i][:-1]  # Remove o \n do final de cada string
        print(encriptaFrase(frases[i], chave))  # Manda para a função para codificar


def decriptaFrase(frase, chave):
    frase = unidecode(frase)  # Retira caracteres especiais
    frase = frase.lower()  # Deixa tudo minusculo

    for i in range(len(frase)):  # Percorre toda a frase
        frase = list(frase)  # Transforma a frase em lista

        if (ord(frase[i]) >= 97+chave and ord(frase[i]) <= 122):  # Verifica o valor ASCII do caractere da lista
            frase[i] = chr(ord(frase[i]) - chave)  # Remove a chave para descriptografar

        elif (ord(frase[i]) >= 97 and ord(frase[i]) < 97+chave):
            frase[i] = chr((122 - chave) + (ord(frase[i]) - 96))

    frase = "".join(frase)  # Torna a lista em string novamente
    return frase


def decriptaTexto(texto, chave):
    f = open(texto, "r", encoding="utf-8")  # Lê o arquivo texto
    frases = f.readlines()  # Divide as linhas do arquivo em uma lista
    for i in range(len(frases)):
        frases[i] = frases[i][:-1]  # Remove o \n do final de cada string
        print(decriptaFrase(frases[i], chave))  # Manda para a função para decriptar


def frequencia(texto):
    f = open(texto, "r", encoding="utf-8")  # Lê o arquivo texto
    frases = f.readlines()

    # Cria um dicionario para armazenar as frequências de letras
    dicionario = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    # A cada ocorrência da letra, adiciona no dicionário
    for i in range(len(frases)):
        dicionario["a"] += frases[i].count("a")
        dicionario["b"] += frases[i].count("b")
        dicionario["c"] += frases[i].count("c")
        dicionario["d"] += frases[i].count("d")
        dicionario["e"] += frases[i].count("e")
        dicionario["f"] += frases[i].count("f")
        dicionario["g"] += frases[i].count("g")
        dicionario["h"] += frases[i].count("h")
        dicionario["i"] += frases[i].count("i")
        dicionario["j"] += frases[i].count("j")
        dicionario["k"] += frases[i].count("k")
        dicionario["l"] += frases[i].count("l")
        dicionario["m"] += frases[i].count("m")
        dicionario["n"] += frases[i].count("n")
        dicionario["o"] += frases[i].count("o")
        dicionario["p"] += frases[i].count("p")
        dicionario["q"] += frases[i].count("q")
        dicionario["r"] += frases[i].count("r")
        dicionario["s"] += frases[i].count("s")
        dicionario["t"] += frases[i].count("t")
        dicionario["u"] += frases[i].count("u")
        dicionario["v"] += frases[i].count("v")
        dicionario["w"] += frases[i].count("w")
        dicionario["x"] += frases[i].count("x")
        dicionario["y"] += frases[i].count("y")
        dicionario["z"] += frases[i].count("z")

    soma = sum(dicionario.values())  # Faz o total de letras no texto

    for i in dicionario:
        dicionario[i] = dicionario[i]/soma  # Transforma a frequência de cada letra em porcentagem
    return dicionario


def decodifica(texto, freq):
    maiscomumAlfabeto = max(freq.items(), key=operator.itemgetter(1))[0]  # Procura a letra mais frequênte do alfabeto
    letrasTexto = frequencia(texto)  # Pega a frequência do livro que desejamos decodificar
    maiscomumTexto = max(letrasTexto.items(), key=operator.itemgetter(1))[0]  # Procura a letra codificada mais frequênte do arquivo
    chave = abs(ord(maiscomumTexto) - ord(maiscomumAlfabeto))  # Compara as letras mais frequêntes para gerar a chave
    decriptaTexto(texto, chave)  # Com a chave podemos usar a função de decriptar

# Apenas strings
print("ENCRIPTANDO")
print(encriptaFrase("abcdefghijklmnopqrstuvwxyz", 7))
print("\nDECRIPTANDO")
print(decriptaFrase("hijklmnopqrstuvwxyzabcdefg", 7))

# Verifica a frequência de letras em um livro qualquer e a usará como base para descobrir a chave
print("\nFREQUÊNCIA: O Cortiço")
freq = frequencia("Cortico.txt")
print(freq)

# Encripta um livro para depois descobrirmos sua chave e descriptografamos
#print("\nENCRIPTANDO O ALQUIMISTA")
#encriptaTexto("Alquimista.txt", 5)

# Verifica a frequência de letras criptografadas para comparar com a base
print("\nFREQUÊNCIA: O ALQUIMISTA")
print(frequencia("Alquimista.txt"))

# Decripta o livro
print("\nDECRIPTANDO O ALQUIMISTA\n")
decodifica("AlquimistaCripto.txt", freq)
