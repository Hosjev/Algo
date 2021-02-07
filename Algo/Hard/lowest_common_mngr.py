"""
You're given 3 inputs, all of which are instances of an OrgChart class that have a directReports property pointing to their direct reports. The 1st input is the top manager in an org chart (the only instance that isn't anybody else's direct report), and the other 2 inputs are reports in the org chart. The 2 inputs are guaranteed to be distinct.

Write a function that returns the lowest common manager to the 2 reports.
(this is the lowest common ancestor problem)

Input:
    topManager = Node A
    reportOne = Node E
    reportTwo = Node I

Output:
    Node B

answer - O(1)
       - O(WS + NM)S
"""
import time


class Node:
    def __init__(self, id):
        self.id = id


# Before I hurt myself, the Algo way:
class Report:
    def __init__(self, mngr, count):
        self.mngr = mngr # Our answer!
        self.count = count # Where we store stack btw-frame counts

class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []

def getLowestCommonManager(topManager, reportOne, reportTwo):
    return recur_down_org(topManager, reportOne, reportTwo).mngr

def recur_down_org(top, r1, r2):
    local_count = 0
    for r in top.directReports:
        result = recur_down_org(r, r1, r2)
        local_count += result.count # whatever we may or may not have here
        if result.mngr is not None:
            return result

    if top == r1 or top == r2:
        local_count += 1
    mngr = top if local_count == 2 else None

    return Report(mngr, local_count)


if __name__ == "__main__":

    org = OrgChart("A")
    org.directReports.append(OrgChart("B"))
    org.directReports.append(OrgChart("C"))
    org.directReports[0].directReports.append(OrgChart("D"))
    org.directReports[0].directReports.append(OrgChart("E"))
    org.directReports[1].directReports.append(OrgChart("F"))
    org.directReports[1].directReports.append(OrgChart("G"))
    org.directReports[0].directReports[0].directReports.append(OrgChart("H"))
    org.directReports[0].directReports[0].directReports.append(OrgChart("I"))

    foo = (getLowestCommonManager(org, org.directReports[0].directReports[0].directReports[0], org.directReports[0].directReports[1]))
    print(foo.name)
