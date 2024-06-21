from api.api_repository import GetCepApi


class CEPService:

    def __init__(self, cep=None, uf=None, locality=None, address=None):
        self.cep_repository = GetCepApi(cep)
        self.address_repository = GetCepApi(uf=uf, locality=locality, address=address)

    def get_cep(self):
        cep = self.cep_repository.get_cep_api()
        return cep

    def get_address(self):
        address = self.address_repository.get_address_api()
        return address
