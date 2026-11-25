
from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []

        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat

    def valider_reseau(self) -> bool:
        noeuds = [self.noeud_entree]
        processing = True

        arcs_entree = list()

        for arc in self.arcs:
            if arc[0] == n or arc[1] == n:
                arcs_entree.append(arc)

        if len(arcs_entree) == 0:
            return len(self.noeuds) == 1

        while processing:                
            for n in noeuds:
                if n == self.noeud_entree and len(noeuds) > 1:
                    print(f"Longueur: {len(noeuds)}")
                    processing = False

                arcs_noeud = list()

                #print(f"Noeud {n}")

                # Liste des arcs contenant ce noeud
                for arc in self.arcs:
                    if arc[0] == n or arc[1] == n:
                        arcs_noeud.append(arc)

                #print(f"\tArcs partants: {arcs_noeud}")

                for arc in arcs_noeud:
                    if arc[0] == n:
                        if arc[1] not in noeuds:
                            noeuds.append(arc[1])
                    else:
                        if arc[0] not in noeuds:
                            noeuds.append(arc[0])

                #print(f"\tNoeuds decouverts: {noeuds}")
                #input()

        return len(noeuds) == len(self.noeuds)

    def valider_distribution(self, t: Terrain) -> bool:
        # TODO
        return False

    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs  = self.strat.configurer(t)

    def afficher(self) -> None:
        # TODO
        pass

    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne, l in enumerate(t.cases):
            for colonne, c in enumerate(l):
                if (ligne, colonne) not in self.noeuds.values():
                    if c == Case.OBSTACLE:
                        print("X", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("~", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
                else:
                    if c == Case.OBSTACLE:
                        print("T", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("+", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        for _ in self.arcs:
            cout += 1.5
        for n in self.noeuds.values():
            if t[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout

