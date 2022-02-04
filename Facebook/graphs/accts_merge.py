from typing import List
from collections import defaultdict


class Person:
    def __init__(self, key, name):
        self.key = key
        self.name = name
        self.emails = set()


class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # TODO: change to large graph with nodes = Name and edges = email
        #       traverse graph for each email with a DFS, add to parent/connected node if found

        # Prime
        key, idx = 0, 0
        visited = defaultdict(int)
        persons = list() # unique Person objects

        # Logic
        while idx < len(accounts):
            name = accounts[idx][0]
            adj = set()
            found = False
            print(idx,key)
            for email in set(accounts[idx][1:]):
                if email in visited:
                    person = persons[visited[email]]
                    person.emails.update(accounts[idx][1:])
                    for e in set(accounts[idx][1:]): visited[e] = person.key
                    found = True
                    break
                else:
                    visited[email] = key
                    adj.add(email)
            if not found:
                p = Person(key, name)
                p.emails = adj
                persons.append(p)
                key += 1
            idx += 1

        # Unfortunate
        result = []
        idx = 0
        for obj in persons:
            result.append([obj.name])
            for i in sorted(obj.emails):
                result[idx].append(i)
            idx += 1

        return result


if __name__ == "__main__":
    accounts = [
            ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ]
    accounts = [
            ["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
            ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],
            ["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
            ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],
            ["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]
        ]
    accounts = [
            ["David","David0@m.co","David1@m.co"],
            ["David","David3@m.co","David4@m.co"],
            ["David","David4@m.co","David5@m.co"],
            ["David","David2@m.co","David3@m.co"],
            ["David","David1@m.co","David2@m.co"]
        ]

    obj = Solution()
    print(obj.accountsMerge(accounts))
