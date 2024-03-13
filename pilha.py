class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return not bool(self.itens)

    def empilhar(self, dado):
        self.itens.append(dado)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()

pilha = Pilha()
pilha.empilhar('A')
pilha.empilhar('B')
pilha.empilhar('C')

print(pilha.desempilhar())  
print(pilha.desempilhar())  
print(pilha.desempilhar())  
