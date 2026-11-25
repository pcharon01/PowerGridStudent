
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

        x0 = randint(0, 10)
        y0 = x0

        while y0 == x0:
            y0 = randint(0, 10)
        
        r.ajouter_noeud(0, (x0, y0))
        r.ajouter_noeud(1, (y0, x0))
        r.ajouter_noeud(2, (x0, y0))

        self.assertTrue(len(r.noeuds) == 3)
        self.assertTrue(len(r.arcs) == 0)

        r.ajouter_arc(2, 3)
        self.assertTrue(len(r.arcs) == 0, f"Expected 0, got {len(r.arcs)}")

        r.ajouter_arc(0, 1)
        self.assertTrue(len(r.arcs) == 1, f"Expected 1, got {len(r.arcs)}")

        r.ajouter_arc(0, 1)
        self.assertTrue(len(r.arcs) == 1, f"Expected 1, got {len(r.arcs)}")

        r.ajouter_arc(1, 2)
        self.assertTrue(len(r.arcs) == 2, f"Expected 2, got {len(r.arcs)}")

        r.ajouter_arc(2, 3)
        self.assertTrue(len(r.arcs) == 2, f"Expected 2, got {len(r.arcs)}")

    def test_validation_un_seul_noeud_correcte(self):
        r = Reseau()

        x0 = randint(0, 10)
        y0 = randint(0, 10)

        r.ajouter_noeud(0, (x0, y0))
        r.definir_entree(0)

        self.assertTrue(r.valider_reseau())

    def test_validation_un_seul_noeud_incorrecte(self):
        r = Reseau()

        x0 = randint(0, 10)
        y0 = randint(0, 10)

        r.ajouter_noeud(0, (x0, y0))
        r.ajouter_noeud(1, (y0, x0))
        r.definir_entree(0)

        self.assertFalse(r.valider_reseau())

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

