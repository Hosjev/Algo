"""
You're a teacher and you've just graded final exam papers. You have a list of student scores in a particular order (array). You need to reward each student score by judging as follows:
    1) All students must receive at least one reward.
    2) Any given student must receive strictly MORE rewards than an adjacent student (to left or right) with a lower score and must receive strictly fewer rewards (to left and right) with a higher score.

Your function must return the minimum number to reward the students given the rules.

Input:
    scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]

Output:
    25 // [4, 3, 2, 1, 2, 3, 4, 5, 1]

* all students will have unique scores

answer - O(N)T / O(1)S
"""

def minRewards(scores):
    # A second solution: find the "center" of a valley and expand outwards
    rewards = [1] * len(scores)
    valleys = find_valley(scores, 0, [])

    for valley in valleys:
        rewards = execute_rewards(rewards, valley, scores)

    return sum(rewards)


def execute_rewards(rewards, middle, scores):
    left = middle-1
    # run loop while left is greater than current/right (right is +1)
    while (left >= 0) and (scores[left] > scores[left + 1]):
        rewards[left] = max(rewards[left], rewards[left + 1] + 1)
        left -= 1

    right = middle + 1

    while (right < len(scores)) and (scores[right - 1] < scores[right]):
        rewards[right] = rewards[right - 1] + 1
        right += 1

    return rewards


def find_valley(scores, mid, lows):
    if mid == len(scores)-1: # end
        # Possible last valley
        if scores[mid] < scores[mid-1]: lows.append(mid)
        return lows
    else:
        if scores[mid-1] > scores[mid] < scores[mid+1]:
            lows.append(mid)
        return find_valley(scores, mid + 1, lows)


def minRewardsW(scores):
    # Naive version
    rewards = [0] * len(scores)
    rewards[0] = 1

    for current in range(1, len(scores)):
        if scores[current] < scores[current-1]:
            rewards[current] = 1
            # If we match, update previous with higher score
            # Current is being reset here so be careful
            # For the last time, Wen, do NOT use negative numbers
            #   when doing a specific index search! It wraps around!
            while True:
                if rewards[current] == rewards[current-1]:
                    rewards[current-1] += 1
                    current -= 1
                else: break
        else:
            # Current score greater than previous
            rewards[current] = rewards[current-1] + 1

    return rewards
    #return sum(rewards)



if __name__ == "__main__":

    scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    # 25 //  [4, 3, 2, 1, 2, 3, 4, 5, 1]
    # There can only be ONE lowest score given all scores are unique.
    # W

    print(minRewards(scores))
    #print(find_valley(scores, 0, []))
