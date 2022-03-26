import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        print("Tähän tulee init")
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
    
    def test_luodun_kassapaatteen_saldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_myydyt_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_luodun_kassapaatteen_myydyt_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_onnistunut_maukkaan_kateisosto_palautus_toimii(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(palautus, 100)
    
    def test_onnistunut_maukkaan_kateisosto_kassa_kasvaa(self):
        kassan_saldo = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(kassan_saldo, self.kassapaate.kassassa_rahaa-400)
    
    def test_rahat_palautetaan_jos_maukkaan_kateisosto_epaonnistuu(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(palautus, 300)

    def test_kassa_ennallaan_jos_maukkaan_kateisosto_epaonnistuu(self):
        kassa_saldo = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(kassa_saldo, self.kassapaate.kassassa_rahaa)

    def test_onnistunut_edullisen_kateisosto_palautus_toimii(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(palautus, 260)

    def test_onnistunut_edullisen_kateisosto_kassa_kasvaa(self):
        kassan_saldo = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(kassan_saldo, self.kassapaate.kassassa_rahaa-240)
    
    def test_rahat_palautetaan_jos_edullisen_kateisosto_epaonnistuu(self):
        palautus = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(palautus, 200)

    def test_kassa_ennallaan_jos_edullisen_kateisosto_epaonnistuu(self):
        kassa_saldo = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(kassa_saldo, self.kassapaate.kassassa_rahaa)

    def test_maukkaan_korttiosto_lisaa_myytyjen_annosten_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_korttiosto_pienentaa_kortin_saldoa(self):
        saldo = self.kortti.saldo
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, saldo-400)

    def test_maukkaan_korttiosto_onnistuu_ja_palautetaan_true(self):
        palautus = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(palautus, True)

    def test_edullisen_korttiosto_lisaa_myytyjen_annosten_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_korttiosto_pienentaa_kortin_saldoa(self):
        saldo = self.kortti.saldo
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, saldo-240)

    def test_edullisen_korttiosto_onnistuu_ja_palautetaan_true(self):
        palautus = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(palautus, True)
    
    def test_epaonnistunut_edullisen_osto_palauttaa_false(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        # Kortin saldo on nyt 200
        palautus = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(palautus, False)

    def test_epaonnistunut_korttiosto_ei_kasvata_myytyjen_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        # Kortin saldo on nyt 200
        myydyt = self.kassapaate.maukkaat
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, myydyt)
    
    def test_epaonnistunut_korttiosto_ei_vahenna_kortin_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        # Kortin saldo on nyt 200
        saldo = self.kortti.saldo
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(saldo, self.kortti.saldo)

    def test_epaonnistunut_korttiosto_palauttaa_false(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        # Kortin saldo on nyt 200
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)

    def test_rahan_lataus_kasvattaa_kortin_saldoa(self):
        saldo = self.kortti.saldo
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo, saldo + 1000)

    def test_rahan_lataus_kasvattaa_kassan_rahamaaraa(self):
        saldo = self.kassapaate.kassassa_rahaa
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, saldo + 1000)

    def test_lataa_nolla_euroa_kortille_ei_muuta_saldoa(self):
        saldo = self.kortti.saldo
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 0)
        self.assertEqual(self.kortti.saldo, saldo)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        palautus = self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(palautus, None)




