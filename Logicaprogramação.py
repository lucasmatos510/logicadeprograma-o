
# Super Trunfo - Trabalho Escolar
# Este programa compara atributos de cartas usando estruturas de decisão e operador ternário.

def menu():
    print("\n=== Super Trunfo ===")
    print("1. Comparar cartas")
    print("2. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

# Lista de cartas do jogo
cartas = [
    {"nome": "Dragão", "forca": 90, "velocidade": 70, "magia": 80},
    {"nome": "Fênix", "forca": 85, "velocidade": 95, "magia": 75},
    {"nome": "Unicórnio", "forca": 80, "velocidade": 60, "magia": 95}
]

# Lista de atributos possíveis
atributos = ["forca", "velocidade", "magia"]

def escolher_carta():
    """Exibe as cartas e permite ao usuário escolher uma."""
    print("\nCartas disponíveis:")
    for i, carta in enumerate(cartas):
        print(f"{i+1}. {carta['nome']}")
    idx = int(input("Escolha o número da carta: ")) - 1
    return cartas[idx]

def escolher_atributo():
    """Exibe os atributos e permite ao usuário escolher um."""
    print("\nAtributos disponíveis:")
    for i, atributo in enumerate(atributos):
        print(f"{i+1}. {atributo}")
    idx = int(input("Escolha o número do atributo: ")) - 1
    return atributos[idx]

def comparar_atributos(carta1, carta2, atributo1, atributo2):
    """
    Compara dois atributos de cartas usando estruturas de decisão aninhadas/encadeadas
    e operador ternário para mostrar o vencedor ou empate.
    """
    print(f"\nComparando {carta1['nome']} ({atributo1}: {carta1[atributo1]}) vs {carta2['nome']} ({atributo2}: {carta2[atributo2]})")
    # Estruturas de decisão aninhadas e encadeadas
    if carta1[atributo1] > carta2[atributo2]:
        print(f"{carta1['nome']} vence no atributo {atributo1}!")
    elif carta1[atributo1] < carta2[atributo2]:
        print(f"{carta2['nome']} vence no atributo {atributo2}!")
    else:
        print("Empate!")
    # Operador ternário para resultado geral
    resultado = carta1['nome'] if carta1[atributo1] > carta2[atributo2] else carta2['nome'] if carta1[atributo1] < carta2[atributo2] else "Empate"
    print(f"Resultado geral: {resultado}")

def main():
    """Função principal que exibe o menu e controla o fluxo do jogo."""
    while True:
        op = menu()
        if op == "1":
            print("\nEscolha a primeira carta:")
            carta1 = escolher_carta()
            atributo1 = escolher_atributo()
            print("\nEscolha a segunda carta:")
            carta2 = escolher_carta()
            atributo2 = escolher_atributo()
            comparar_atributos(carta1, carta2, atributo1, atributo2)
        elif op == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
