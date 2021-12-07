import math


class ClockAngles:

    def _radian(self, H, M):
        # (H - M of degree) * pi/180
        # float.__round__(4)
        factor = (abs(H - M)) * math.pi/180
        return float(factor).__round__(4)

    def _degree(self, H, M):
        factor = (abs(H - M)) / 6
        angles = (4 * factor) + factor
        return int(180 - angles)

    def _convert(self, time: str):
        H = int(time[0:2]) * 30
        M = int(time[3:]) * 6
        return H, M

    def solve(self, time: str, unit: str):
        # Should check str format "##:##"
        H, M = self._convert(time)
        if unit == "radians":
            return self._radian(H, M)
        elif unit == "degrees":
            return self._degree(H, M)
        else:
            raise TypeError("Unit not supported")


if __name__ == "__main__":
    obj = ClockAngles()
    print(obj.solve("09:30", "degrees"))
    print(obj.solve("03:00", "radians"))
