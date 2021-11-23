from os.path import join


class Localisation:
    DIR = "Common/Localisation"

    def __init__(self):
        self.files = [
            "technology/beyond.txt",
            "technology/civil.txt",
            "technology/military.txt",
            "jobs.txt",
            "resources.txt"
        ]

        self._dict = self.localisation()

    def localisation(self):
        _dict = dict()
        for file in self.files:
            with open(join(self.DIR, file), 'r') as d:
                for line in d:
                    line = line.strip()
                    if line:
                        key, value = line.split('=')
                        _dict[key] = value
        return _dict

    def __getitem__(self, item):
        return self._dict.get(item)
