from weather_app.repositories.IWeatherRepo import IWeatherRepo
from weather_app.services.iweather_service import IWeatherService


class WeatherService(IWeatherService):
    def __init__(self, repo: IWeatherRepo) -> None:
        self.repo = repo

    def get_weather(self) -> str:
        data = self.repo.get_data()
        return f'{data}: Weather from weather service'
