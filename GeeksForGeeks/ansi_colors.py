import random


c = (
    "\033[0m",
    "\033[36m",
    "\033[91m",
    "\033[35m"
)


# the colon is an annotation used to describe the expected argument type
# the dash greater-than is an annotation used to describe the return type
def color_me(idx: int) -> int:
    # tho technically here, I return nothing
    print(c[idx + 1] + f"This is my num: {idx}" + c[0])


random.seed(444)
color_me(0)
color_me(1)
color_me(2)
