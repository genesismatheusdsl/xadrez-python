class Peca:
    """Classe base para uma peça de xadrez"""
    def __init__(self, cor):
        self.cor = cor

    def movimentos_validos(self, tabuleiro, x, y):
        """Método genérico para verificar movimentos válidos (deve ser implementado nas subclasses)"""
        raise NotImplementedError("Método 'movimentos_validos' deve ser implementado na classe filha.")


class Rei(Peca):
    """Classe para a peça Rei"""
    def movimentos_validos(self, tabuleiro, x, y):
        """Movimentos válidos para o Rei: uma casa em qualquer direção"""
        movimentos = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0)]
        return [(x + dx, y + dy) for dx, dy in movimentos if 0 <= x + dx < 8 and 0 <= y + dy < 8]


class Rainha(Peca):
    """Classe para a peça Rainha"""
    def movimentos_validos(self, tabuleiro, x, y):
        """Movimentos válidos para a Rainha: qualquer direção (horizontal, vertical, diagonal)"""
        movimentos = []
        for dx in [-1, 1]:
            for dy in [-1, 1]:
                for i in range(1, 8):
                    if 0 <= x + dx * i < 8 and 0 <= y + dy * i < 8:
                        movimentos.append((x + dx * i, y + dy * i))
        return movimentos


class Tabuleiro:
    """Classe para o tabuleiro de xadrez"""
    def __init__(self):
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]  # Criando o tabuleiro 8x8 vazio
        self.inicializa_tabuleiro()

    def inicializa_tabuleiro(self):
        """Inicializa as peças no tabuleiro"""
        # Colocando as peças principais (Reis e Rainhas) no tabuleiro
        self.tabuleiro[0][4] = Rei("preto")
        self.tabuleiro[7][4] = Rei("branco")
        self.tabuleiro[0][3] = Rainha("preto")
        self.tabuleiro[7][3] = Rainha("branco")

    def mostrar_tabuleiro(self):
        """Exibe o estado atual do tabuleiro"""
        for linha in self.tabuleiro:
            print(' '.join(['.' if peca is None else peca.__class__.__name__[0] for peca in linha]))


class Jogo:
    """Classe para gerenciar o jogo de xadrez"""
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador_atual = "branco"

    def mudar_turno(self):
        """Alterna entre os turnos dos jogadores"""
        self.jogador_atual = "preto" if self.jogador_atual == "branco" else "branco"

    def jogar(self):
        """Inicia o loop do jogo"""
        while True:
            self.tabuleiro.mostrar_tabuleiro()
            print(f"Turno do jogador {self.jogador_atual}")
            
            # Aqui você pode adicionar mais lógica para jogar e validar os movimentos
            movimento = input("Digite o movimento (ex: e2 para e4): ")
            if movimento == "sair":
                break
            # Adicionar lógica de movimentação de peças...
            self.mudar_turno()


if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()
