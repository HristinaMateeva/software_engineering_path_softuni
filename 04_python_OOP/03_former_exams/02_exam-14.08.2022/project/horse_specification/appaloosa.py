from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    TRAINING_RATE = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + Appaloosa.TRAINING_RATE > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += Appaloosa.TRAINING_RATE
