from patient.abs_patient import AbsPatient


class Male(AbsPatient):

    def calculate_framingham(self):
        self._score_age()
        self._score_total_cholesterol()
        self._score_smoker()
        self._score_hdl_cholesterol()
        self._score_systolic_blood_pressure()
        self.reporting()
        return self.score_risk

    def _score_age(self):
        my_age = {(range(20, 34)): -9,
                  (range(35, 39)): -4,
                  (range(40, 44)): 0,
                  (range(45, 49)): 3,
                  (range(50, 54)): 6,
                  (range(55, 59)): 8,
                  (range(60, 64)): 10,
                  (range(65, 69)): 11,
                  (range(70, 74)): 12,
                  (range(75, 79)): 13}
        for key, value in my_age.items():
            if self.age in key:
                self._score += value

    def _score_total_cholesterol(self):
        age = self.age
        total_cholesterol = self.total_cholesterol
        self._score += 9

    def _score_smoker(self):
        smoker = self.smoker
        if smoker:
            self._score += 9

    def _score_hdl_cholesterol(self):
        self._score += 2

    def _score_systolic_blood_pressure(self):
        self._score += 3

    def _score_risk(self):
        return self._score
