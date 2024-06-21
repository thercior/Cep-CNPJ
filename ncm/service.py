from api.api_repository import GetNcmApi


class NCMService:

    def __init__(self, ncm):
        self.ncm_repository = GetNcmApi(ncm)

    def get_ncm(self):
        ncm = self.ncm_repository.get_ncm_api()
        return ncm
