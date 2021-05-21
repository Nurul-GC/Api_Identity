import unittest
from domain.validation.bi import Bi
from services.http_api.gov.bi import bi_service
from services.http_api.gov.nif import nif_service
import json



class ValidatePerson(unittest.TestCase):
     #"https://desenvolvimento.gov.ao/dev.api/bi/?bi=006989589LA042"

     def test_BI(self):
         tes_bi = Bi()
         vald = tes_bi.rules("006153280LA047")
         self.assertTrue(vald)

     def test_BI_service(self):
         test_servi = bi_service()
         test_servi.verification_bi("006153280LA047")
         self.assertTrue(test_servi)


     def test_NIF_service(self):
        test_servi = nif_service()
        test_servi.verification_nif("006153280LA047")
        self.assertTrue(test_servi)


if __name__ == '__main__': 
    unittest.main()