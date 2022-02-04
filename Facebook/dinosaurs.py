from collections import defaultdict


class Dinos:

    def __init__(self):
        #self.cache = dict()
        self.cache = defaultdict(dict)

    def _calc_speed(self, leg, stride):
        # Missing force of gravity, obvs
        return float(leg) * float(stride)

    def _build_speed(self):
        for k, v in self.cache.items():
            self.cache[k]["SPEED"] = self._calc_speed(self.cache[k]["LEGL"], self.cache[k]["STRIDE"])

    def _open(self, infile):
        with open(infile, "r") as fd:
            header = fd.readline().strip().split(",")
            contents = [l.strip() for l in fd.readlines()]
        self._add_to_cache(header, contents)

    def _add_to_cache(self, headers, contents):
        # Trash first column
        for i in range(1, len(headers)):
            for dino in contents:
                line = dino.split(",")
                self.cache[line[0]][headers[i]] = line[i]
        if "STRIDE" in headers: self._build_speed()

    def get_bipeds(self):
        """ Return fastest to slowest """
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
    print(obj.cache)
    print(obj.get_bipeds())
