class Buscador:

    def Busca_por_titulo(self, playlist, titulo):
        for c in range(len(playlist)):
            if playlist[c].titulo == titulo:
                return c
        return -1

    def Busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:  # busca na primeira metade da lista
                    ultimo = meio - 1  # já foi visto que não está no elemento meio, então vai um a menos
                else:
                    primeiro = meio + 1
        return -1
