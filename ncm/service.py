from api.api_repository import GetNCMAPI


class NCMService:

    def __init__(self, ncm):
        self.ncm_repository = GetNCMAPI(ncm)

    def get_ncm(self):
        ncm = self.ncm_repository.get_ncm_api()
        return ncm
