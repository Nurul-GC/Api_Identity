from services.http_api.http_service import http
import services.http_api.point_url as url
from services.http_api.gov.bi import bi_service


class nif_service():

    Q ="/bi/?bi="

    def __init__(self):
        self.api_service = bi_service()
        

    def verification_nif(self,nif):
        result =self.api_service.verification_bi(nif)
        return result