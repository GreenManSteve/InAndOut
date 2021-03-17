import abc
from .email import Email as email


class AbsPatient(metaclass=abc.ABCMeta):
    _score = 0

    def __init__(self, age, total_cholesterol, smoker, hdl_cholesterol, systolic_blood_pressure, email=None):
        self._age = age
        self._total_cholesterol = total_cholesterol
        self._smoker = smoker
        self._hdl_cholesterol = hdl_cholesterol
        self._systolic_blood_pressure = systolic_blood_pressure
        self._email = email

    def reporting(self):
        if self.email is not None:
            self._send_mail()

        # self.save_to_s3()
        # self.append_to_dynamodb()

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
        return self._score

    @property
    def email(self):
        return self._email
