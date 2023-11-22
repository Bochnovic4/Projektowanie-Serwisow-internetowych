from weather_app.repositories.IWeatherRepo import IWeatherRepo


class WeatherRepo(IWeatherRepo):
    def get_data(self) -> str:
        return 'Data from txt file'
