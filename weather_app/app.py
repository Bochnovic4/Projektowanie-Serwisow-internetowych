from dependency_injector.wiring import Provide

from weather_app.services.iweather_service import IWeatherService
from container import Container


def main(service: IWeatherService = Provide(Container.service)) -> None:
    weather = service.get_weather()

    print(f'from interface: {weather}')


if __name__ == '__main__':
    container = Container()
    container.wire(modules=[__name__])

    main()
