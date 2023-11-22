from dependency_injector import containers
from dependency_injector import providers

from weather_app.repositories.WeatherRepoDB import WeatherRepoDB
from weather_app.services.weather_service import WeatherService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    repo = providers.Singleton(
        WeatherRepoDB
    )

    service = providers.Factory(
        WeatherService,
        repo=repo
    )
