class ScoreByMoves:
    """ O(S * 3) """
    def _ways(self, total, subarr, ph, c, results):
        # Recurse through ways of ME and all moves, backtrack by removing ONE
        if total == 0:
            results.append(list(ph))
            return

        for _ in range(1):
            of_me_ph = ph + [c]
            if (total - c) < 0: break
            self._ways(total - c, subarr, of_me_ph, c, results)
        of_me_ph.pop()

        for i,e in enumerate(subarr):
            if total - e < 0:
                break
            nested_ph = of_me_ph + [e]
            nested_sa = [c] + subarr[:i] + subarr[i+1:]
            self._ways(total - e, nested_sa, nested_ph, e, results)
            nested_ph.pop()

        return results

    def solve(self, moves, score):
        if moves > 1:
            subarr = [i for i in range(2, moves+1)]
        else: return [[1] * score]
        return self._ways(score, subarr, [], 1, [])


if __name__ == "__main__":
    print(ScoreByMoves().solve(3, 5))
    print(ScoreByMoves().solve(1, 5))
