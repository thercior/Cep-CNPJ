from api.api_repository import GetCNPJ


class CNPJService:

    def __init__(self, cnpj):
        self.cnpj_repository = GetCNPJ(cnpj)

    def get_cnpj(self, cnpj):
        cnpj = self.cnpj_repository.get_cnpj()
        return cnpj
