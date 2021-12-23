class Dinos:

    def __init__(self):
        self.cache = dict()

    def _get_speed(self, leg, stride):
        # Missing force of gravity, obvs
        return float(leg) * float(stride)

    def _build_speed(self):
        for k, v in self.cache.items():
            self.cache[k]["SPEED"] = self._get_speed(self.cache[k]["LEGL"], self.cache[k]["STRIDE"])

    def _open(self, infile):
        header = ""
        contents = []
        with open(infile, "r") as fd:
            header = fd.readline().strip()
            for line in fd.readlines():
                contents.append(line.strip())
        self._add_to_cache(header, contents)

    def _add_to_cache(self, header, contents):
        headers = header.split(",")
        for i in range(1, len(headers)):
            for dino in contents:
                line = dino.split(",")
                try:
                    self.cache[line[0]][headers[i]] = line[i]
                except KeyError:
                    self.cache[line[0]] = {headers[i]: line[i]}

    def get_bipeds(self):
        result = []

        for k, v in self.cache.items():
            if v["TYPE"] == "bipedal":
                result.append((k, v["SPEED"]))
        result.sort(key=lambda x: x[1], reverse=True)
        return result


if __name__ == "__main__":
    obj = Dinos()
    obj._open("Facebook/IN/dino1.csv")
    obj._open("Facebook/IN/dino2.csv")
    obj._build_speed()
    print(obj.cache)
    print(obj.get_bipeds())
