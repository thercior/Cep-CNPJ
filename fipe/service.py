from api.api_repository import GetFipeApi


class FipeService:

    def __init__(self, type_vehicle=None, brand=None, model=None, year=None, fipe_code=None):
        self.fipe_repository = GetFipeApi(
            type_vehicle=type_vehicle,
            brand=brand,
            model=model,
            year=year,
            fipe_code=fipe_code
        )

    def get_fipe_vehicle(self):
        fipe_vehicle = self.fipe_repository.get_fipe_vehicle_api()
        return fipe_vehicle

    def get_fipe_code_year(self):
        fipe_code = self.fipe_repository.get_fipe_code_api()
        return fipe_code

    def get_fipe_code_history(self):
        fipe_code_history = self.fipe_repository.get_fipe_code_history_api()
        return fipe_code_history

    def get_model(self):
        model = self.fipe_repository.get_models_api()
        return model

    def get_model_year(self):
        model_year = self.fipe_repository.get_model_year_api()
        return model_year
