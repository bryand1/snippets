import json


class Diagnosis:

    def __init__(self, name: 'Optional[str]' = None):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value


class Patient:

    def __init__(self, name: 'str'):
        self.name = name
        self.diagnosis = Diagnosis()

    def set_diagnosis(self, name: 'str'):
        self.diagnosis.name = name
    
    def to_json(self):
        return json.dumps({
            'name': self.name,
            'diagnosis': self.diagnosis.name
        })


if __name__ == '__main__':
    bryan = Patient('Bryan')
    bryan.set_diagnosis('Sore throat')
    print(bryan.to_json())
