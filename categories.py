class Categories:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        ret = ""
        for i, p in enumerate(self.data):
            number = str((self.data)[i].get("num"))
            name = str(self.data[i].get("name"))
            ret += number + ": " + name + "\n"

        return ret