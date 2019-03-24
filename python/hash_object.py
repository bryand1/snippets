"""
When adding objects to a set, objects must be hashable and comparable
"""

class Language:

    def __init__(self, name: 'str'):
        self.name = name

    def __str__(self):
        return "Language: {}".format(self.name)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.name == other.name


if __name__ == '__main__':
    languages = set()
    languages.add(Language('Python'))
    languages.add(Language('Haskell'))
    languages.add(Language('Java'))

    # Add the same language
    languages.add(Language('Python'))

    for language in languages:
        print(language)
