class Heart:
    def __init__(self, usage):
        self.usage = usage

    @property
    def state(self):
        if self.usage > 70:
            return 'high blood pressure'
        else:
            return 'feeling good'


class Brain:
    def __init__(self, usage):
        self.usage = usage

    @property
    def state(self):
        if self.usage > 90:
            return 'tired'
        else:
            return 'rested'


class Person:
    def __init__(self, heart_usage, brain_usage):
        self.heart = Heart(heart_usage)
        self.brain = Brain(brain_usage)


class leg:
    def __init__(self, person, moving_speed):
        self.person = person
        self.moving_speed = moving_speed

    @property
    def state(self):
        if self.moving_speed > 10:
            return 'running'
        else:
            return 'walking'


heart = Heart(80)
brain = Brain(85)
person = Person(heart.state, brain.state)
leg = leg(person, 15)
print('heart state:',heart.state)
print('brain state:',brain.state)
print('leg state:',leg.state)