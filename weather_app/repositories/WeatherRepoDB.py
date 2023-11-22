from weather_app.repositories.IWeatherRepo import IWeatherRepo


class WeatherRepoDB(IWeatherRepo):
    def get_data(self) -> str:
        return 'Get data from DB'
