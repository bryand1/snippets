from copy import deepcopy
import pdb


class Program:
    def __init__(self, id, name, signatures):
        self.id = id
        self.name = name
        self.signatures = signatures

class Application:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Match:
    def __init__(self, program: Program, application: Application):
        self.program = program
        self.application = application


def main():
    p1 = Program(1, 'Amgen Safety Net Foundation', ['Prescriber', 'Patient'])
    a1 = Application(1, 'Amgen PDF')
    m1 = Match(p1, a1)

    # WANT TO COPY m1
    m2 = deepcopy(m1)
    # print(m2)
    pdb.set_trace()


if __name__ == '__main__':
    main()
