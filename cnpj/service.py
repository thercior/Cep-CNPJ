from api.api_repository import GetCNPJAPI


class CNPJService:

    def __init__(self, cnpj):
        self.cnpj_repository = GetCNPJAPI(cnpj)

    def get_cnpj(self):
        cnpj = self.cnpj_repository.get_cnpj()
        return cnpj
