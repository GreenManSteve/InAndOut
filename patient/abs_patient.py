import abc
from .email import Email as email
import random

class AbsPatient(metaclass=abc.ABCMeta):
    _score = 0

    def __init__(self, age, total_cholesterol, smoker, hdl_cholesterol, systolic_blood_pressure):
        self._age = age
        self._total_cholesterol = total_cholesterol
        self._smoker = smoker
        self._hdl_cholesterol = hdl_cholesterol
        self._systolic_blood_pressure = systolic_blood_pressure

    def calculate_framingham(self):
        self._score_age()
        self._score_total_cholesterol()
        self._score_smoker()
        self._score_hdl_cholesterol()
        self._score_systolic_blood_pressure()
        self.reporting()
        return self.score_risk

    def reporting(self):
        # self.save_to_s3()
        # self.append_to_dynamodb()
        pass

    def save_to_s3(self):
        pass

    def append_to_dynamodb(self):
        self

    def _send_mail(self):
        email(self.email, self.score_risk)


    @abc.abstractmethod
    def calculate_framingham(self):
        pass

    @abc.abstractmethod
    def _score_age(self):
        pass

    @abc.abstractmethod
    def _score_total_cholesterol(self):
        pass

    @abc.abstractmethod
    def _score_smoker(self):
        pass

    @abc.abstractmethod
    def _score_hdl_cholesterol(self):
        pass

    @abc.abstractmethod
    def _score_systolic_blood_pressure(self):
        pass

    @abc.abstractmethod
    def _score_risk(self):
        pass

    @property
    def age(self):
        return self._age

    @property
    def total_cholesterol(self):
        return self._total_cholesterol

    @property
    def smoker(self):
        return self._smoker

    @property
    def score_risk(self):
        risk = random.randint(0, 17)

        risk_percentage = {(range(0)): "<1%",
                           (range(1, 4)): "1%",
                           (range(5, 6)): "2%",
                           (range(7)): "3%",
                           (range(8)): "4%",
                           (range(9)): "5%",
                           (range(10)): "6%",
                           (range(11)): "8%",
                           (range(12)): "10%",
                           (range(13)): "12%",
                           (range(14)): "16%",
                           (range(15)): "20%",
                           (range(16)): "25%",
                           (range(17)): "over 30%"}

        for key, value in risk_percentage.items():
            if risk in key:
                return "Your risk of developing cardiovascular " \
                       "disease in the next ten years is {}".format(value)
