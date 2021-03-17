class Screening(object):

    def __init__(self, person):
        self._person = person

    def calculate_framingham(self):
        return self._person.calculate_framingham()