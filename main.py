class SpaceAgency:
    def __init__(self, name):
        self.name = name

    def agency_info(self):
        return f"Агентство {self.name} занимается изучением космоса и разработкой космических технологий."

class NASA_Rocket(SpaceAgency):
    def __init__(self, rocket_name, max_speed):
        super().__init__("NASA")
        self.rocket_name = rocket_name
        self.max_speed = max_speed

    def launch_rocket(self):
        return f"Ракета {self.rocket_name} от NASA запущена, максимальная скорость — {self.max_speed} км/ч."

class Roscosmos_Rocket(SpaceAgency):
    def __init__(self, rocket_name, max_speed):
        super().__init__("Роскосмос")
        self.rocket_name = rocket_name
        self.max_speed = max_speed

    def launch_rocket(self):
        return f"Ракета {self.rocket_name} от Роскосмос запущена, максимальная скорость — {self.max_speed} км/ч."

class Ozbekkosmos_Rocket(SpaceAgency):
    def __init__(self, rocket_name, max_speed):
        super().__init__("O'zbekkosmos")
        self.rocket_name = rocket_name
        self.max_speed = max_speed

    def launch_rocket(self):
        return f"Ракета {self.rocket_name} от O'zbekkosmos запущена, максимальная скорость — {self.max_speed} км/ч."


nasa_rocket = NASA_Rocket("Artemis", 32000)
roscosmos_rocket = Roscosmos_Rocket("Союз", 28000)
ozbekkosmos_rocket = Ozbekkosmos_Rocket("Uz-1", 26000)

print(nasa_rocket.agency_info())
print(nasa_rocket.launch_rocket())
print(roscosmos_rocket.agency_info())
print(roscosmos_rocket.launch_rocket())
print(ozbekkosmos_rocket.agency_info())
print(ozbekkosmos_rocket.launch_rocket())
