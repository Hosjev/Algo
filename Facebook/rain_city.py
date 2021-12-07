class BuildingsRain:
    """ O(N + 3) """
    def contains(self, buildings):
        # Edge Case(s)
        if len(buildings) < 3:
            return 0

        left = [0] * (len(buildings) + 1)
        right = [0] * (len(buildings) + 1)
        buildings = [0] + buildings
        for idx in range(1, len(buildings)):
            left[idx] = max(buildings[idx - 1], left[idx - 1])
        for idx in reversed(range(len(buildings) - 1)):
            right[idx] = max(buildings[idx + 1], right[idx + 1])

        total = 0
        for i in range(1, len(buildings) - 1):
            min_height = min(left[i], right[i])
            if buildings[i] < min_height:
                total += min_height - buildings[i]

        return total


if __name__ == "__main__":
    obj = BuildingsRain()
    print(obj.contains([7,4,0,9]))
    print(obj.contains([6,9,9]))
