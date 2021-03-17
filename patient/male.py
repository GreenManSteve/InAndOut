from patient.abs_patient import AbsPatient


class Male(AbsPatient):

    def calculate_framingham(self):
        self._score_age()
        self._score_total_cholesterol()

        return self._score

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

        if 20 <= age <= 39:
            if 160 <= total_cholesterol <= 199:
                self._score += 4
            elif 200 <= total_cholesterol <= 239:
                self._score += 7
            elif 240 <= total_cholesterol <= 279:
                self._score += 9

    def _score_smoker(self):
        pass

    def _score_hdl_cholesterol(self):
        pass

    def _score_systolic_blood_pressure(self):
        pass

    def _score_risk(self):
        return self._score