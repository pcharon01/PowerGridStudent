
import unittest
import xmlrunner

from Reseau import Reseau
from Terrain import Terrain, Case

from random import randint

class TestReseau(unittest.TestCase):

    def test_definition_entree(self):
        for k in range(10):
            r = Reseau()

            for n in range(5):
                x = randint(0, 10)
                y = randint(0, 10)

                r.ajouter_noeud(n, (x, y))

            r.definir_entree(k)

            if k < 5:
                self.assertEqual(r.noeud_entree, k)
            else:
                self.assertEqual(r.noeud_entree, -1)

    def test_ajout_noeud(self):
        r = Reseau()

        self.assertTrue(len(r.noeuds) == 0)

        for n in range(10):
            x = randint(0, 10)
            y = randint(0, 10)

            r.ajouter_noeud(n, (x, y))

            self.assertTrue(r.noeuds[n] == (x, y))

    def test_ajout_arc(self):
        r = Reseau()

        r.ajouter_noeud(0, (randint(0, 10), randint(0, 10)))
        r.ajouter_noeud(1, (randint(0, 10), randint(0, 10)))
        r.ajouter_noeud(2, (randint(0, 10), randint(0, 10)))

        self.assertTrue(len(r.noeuds) == 2)
        self.assertTrue()

        r.ajouter_arc(0, 1)

        self.assertTrue

    def test_validation_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        self.assertTrue(r.valider_reseau())

    def test_validation_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)

        self.assertFalse(r.valider_reseau())

    def test_distribution_correcte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.VIDE, Case.CLIENT],
        ]

        self.assertTrue(r.valider_distribution(t))

    def test_distribution_incorrecte(self):
        r = Reseau()
        r.noeuds[0] = (0, 0)
        r.noeud_entree = 0

        r.noeuds[1] = (1, 0)
        r.arcs.append((0, 1))

        r.noeuds[2] = (0, 1)
        r.arcs.append((0, 2))

        r.noeuds[3] = (0, 2)
        r.arcs.append((2, 3))

        r.noeuds[4] = (1, 2)
        r.arcs.append((3, 4))

        t = Terrain()
        t.cases = [
                [Case.ENTREE, Case.VIDE, Case.VIDE],
                [Case.CLIENT, Case.CLIENT, Case.CLIENT],
        ]

        self.assertFalse(r.valider_distribution(t))

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="test-reports"))

