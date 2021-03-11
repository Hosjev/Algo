"""
Given 2 arrays: reds, blues repping students' heights. As photographer, you must align 2 rows for photo. The back (solid red/blue) must be each +1 taller. Return boolean if this can be done.


Input:
    reds = [5, 8, 1, 3, 4]
    blues = [6, 9, 2, 4, 5]
Output:
    true

**will always be = and 2+ count
**sorted 1, 3, 4, 5, 8
**sorted 2, 4, 5, 6, 9
"""
import time


def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.

    redShirtHeights.sort()
    blueShirtHeights.sort()
    if redShirtHeights[0] < blueShirtHeights[0]:
        # reference object
        bottom = redShirtHeights
        top = blueShirtHeights
    elif redShirtHeights[0] > blueShirtHeights[0]:
        bottom = blueShirtHeights
        top = redShirtHeights
    else:
        # equal
        return False

    for idx in range(len(bottom)):
        if (bottom[idx] >= top[idx]):
            return False

    return True


reds = [5, 10, 1, 3, 4]
blues = [6, 9, 2, 4, 5]
print(classPhotos(reds, blues))
