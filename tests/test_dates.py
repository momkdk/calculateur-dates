import unittest
from datetime import date

from calculateur_dates.dates import age_exact, decaler, jours_entre


class TestAgeExact(unittest.TestCase):
    def test_anniversaire_passe_cette_annee(self):
        r = age_exact(date(2000, 3, 15), date(2026, 6, 1))
        self.assertEqual((r.annees, r.mois, r.jours), (26, 2, 17))

    def test_anniversaire_pas_encore_passe(self):
        r = age_exact(date(2000, 10, 15), date(2026, 6, 1))
        self.assertEqual((r.annees, r.mois), (25, 7))

    def test_jour_pile_anniversaire(self):
        r = age_exact(date(2000, 6, 1), date(2026, 6, 1))
        self.assertEqual((r.annees, r.mois, r.jours), (26, 0, 0))

    def test_veille_anniversaire(self):
        r = age_exact(date(2000, 6, 2), date(2026, 6, 1))
        self.assertEqual(r.annees, 25)

    def test_fin_de_mois_fevrier(self):
        # Né un 31 janvier, référence un 1er mars (février n'a pas de 31)
        r = age_exact(date(2000, 1, 31), date(2026, 3, 1))
        self.assertEqual(r.annees, 26)

    def test_naissance_future_leve_erreur(self):
        with self.assertRaises(ValueError):
            age_exact(date(2030, 1, 1), date(2026, 1, 1))

    def test_jours_total_coherent(self):
        r = age_exact(date(2020, 1, 1), date(2020, 1, 11))
        self.assertEqual(r.jours_total, 10)

    def test_sans_date_reference_ne_leve_pas(self):
        r = age_exact(date(2000, 1, 1))
        self.assertGreaterEqual(r.annees, 25)


class TestJoursEntre(unittest.TestCase):
    def test_ordre_normal(self):
        self.assertEqual(jours_entre(date(2026, 1, 1), date(2026, 1, 11)), 10)

    def test_ordre_inverse(self):
        self.assertEqual(jours_entre(date(2026, 1, 11), date(2026, 1, 1)), 10)

    def test_meme_date(self):
        self.assertEqual(jours_entre(date(2026, 1, 1), date(2026, 1, 1)), 0)


class TestDecaler(unittest.TestCase):
    def test_ajout(self):
        self.assertEqual(decaler(date(2026, 1, 1), 10), date(2026, 1, 11))

    def test_soustraction(self):
        self.assertEqual(decaler(date(2026, 1, 11), -10), date(2026, 1, 1))

    def test_changement_de_mois(self):
        self.assertEqual(decaler(date(2026, 1, 28), 5), date(2026, 2, 2))

    def test_annee_bissextile(self):
        self.assertEqual(decaler(date(2028, 2, 28), 1), date(2028, 2, 29))


if __name__ == "__main__":
    unittest.main()
