class Excel:
    
    def convert_col(self, integer):
        cache = {1: "A", 2: "B", 3: "C"}
        # 1 - int % 26 = letter at back
        # 2 - number from 1 int // 26 = next int
        # 3 - repeat until int at 0

