import json
from abs_strategy import Screening
from patient.null_class import NullClass
from inspect import getmembers, isclass, isabstract
import patient


def handler(event, context):
    humans = {}

    class_list = getmembers(patient,
                            lambda m: isclass(m) and not isabstract(m))

    for name, _type in class_list:
        if isclass(_type) and issubclass(_type, patient.AbsPatient):
            humans.update([[name, _type]])

    body = event['data']
    sex = str(body['sex']).lower().capitalize()
    age = body['age']
    total_cholesterol = body['total_cholesterol']
    smoker = body['smoker']
    hdl_cholesterol = body['hdl_cholesterol']
    systolic_blood_pressure = body['systolic_blood_pressure']
    email = body['email']

    if sex in humans:
        human = humans[sex](age, total_cholesterol, smoker, hdl_cholesterol, systolic_blood_pressure, email)
        screening = Screening(human)
    else:
        null_class = NullClass(sex)
        screening = Screening(null_class)

    return {'statusCode': 200,
            'body': json.dumps(screening.calculate_framingham()),
            'headers': {'Content-Type': 'application/json'}
            }
