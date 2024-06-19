from api.api_repository import GetCnpjApi


class CNPJService:

    def __init__(self, cnpj):
        self.cnpj_repository = GetCnpjApi(cnpj)

    def get_cnpj(self):
        cnpj = self.cnpj_repository.get_cnpj_api()
        return cnpj
