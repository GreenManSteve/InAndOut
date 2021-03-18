import abc
from .email import Email as email
dynamodb = boto3.client('dynamodb')
import datetime

class AbsPatient(metaclass=abc.ABCMeta):
    _score = 0
    _total = 0

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
        self.append_to_dynamodb()
        pass

    def save_to_s3(self):
        pass

    def append_to_dynamodb(self):
        date_stamp = datetime.datetime.now()
        class_name = self.name
        age = self.age
        percentage = self.percentage

        table = dynamodb.Table('FramScores')
        response = table.put_item(
            item={
                'pk': {'S': '{0}'.format(date_stamp)},
                'sk': {'S': '{0}'.format(class_name)},
                'age': {'S': '{0}'.format(age)},
                'percentage': {'S': '{0}%'.format(percentage)},
            }
        )
        return response


        table = dynamodb.Table('Movies')
        response = table.put_item(
            Item={
                'year': year,
                'title': title,
                'info': {
                    'plot': plot,
                    'rating': rating
                }
            }
        )
        return response

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
        risk = self.percentage

        return "Your risk of developing cardiovascular " \
               "disease in the next ten years is {val:.0f}%".format(val=risk)

    @property
    def name(self):
        return self.cls_name

    @property
    def score(self):
        return self._score

    @property
    def total(self):
        return self._total

    @property
    def percentage(self):
        score = self.score
        total = self.total
        risk = (score / total) * 100
        return risk
