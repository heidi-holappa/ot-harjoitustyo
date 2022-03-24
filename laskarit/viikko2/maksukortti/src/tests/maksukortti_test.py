import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.kortti = Maksukortti(10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        vastaus = str(self.kortti)

        self.assertEqual(vastaus, "Kortilla on rahaa 10 euroa")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.5 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        # nyt kortin saldo on 2
        self.kortti.syo_edullisesti()

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(25)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 35 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 150 euroa")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        # nyt kortin saldo on 2
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2 euroa")

    def test_negatiivisen_saldon_lataus_ei_muuta_kortin_arvoa(self):
        self.kortti.lataa_rahaa(40)
        self.kortti.lataa_rahaa(-200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 50 euroa")

    def test_kortilla_voi_ostaa_vain_edullisen_lounaan_kun_rahaa_on_vain_edullisen_lounaan_verran(self):
        self.kortti.syo_edullisesti()
        self.kortti.syo_edullisesti()
        self.kortti.syo_edullisesti()
        # Kortin saldo on nyt 2.5
        self.kortti.syo_edullisesti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0.0 euroa")

    def test_kortilla_voi_ostaa_maukkaan_lounaan_kun_rahaa_nelja_euroa(self):
        self.kortti.lataa_rahaa(2)
        self.kortti.syo_maukkaasti()
        self.kortti.syo_maukkaasti()
        # Kortin saldo on nyt 4
        self.kortti.syo_maukkaasti()
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 0 euroa")
