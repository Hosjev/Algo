"""
Given a list of people with their birth/death dates, return the year in which
the populace was greatest.
--what is the input data type?
--are only years listed?
--this is an averages problem
"""


def brute_force_alive(peeps):
    # Brute force approach
    # 1- get min from tuples [0], get max from [1]
    # 2- O(N) build hash table where key = year from min to max
    # 3- loop through every range and add to key value if present
    min_birth = min(peeps, key=lambda x: x[0])[0]
    max_death = max(peeps, key=lambda x: x[1])[1]

    # create hash
    years = dict()
    for year in range(min_birth, max_death+1):
        years[year] = int()

    # loop thru peeps ranges
    # O(N)
    for birth, death in peeps:
        # not counting death year?
        # adds to runtime but not space
        # O(N*Yrs)
        for peep_date in range(birth, death-1):
            # O(1) constant time and space
            years[peep_date] += 1

    winning_year = max(years.items(), key=lambda x: x[1])[0]

    return winning_year


def dp_alive(peeps):
    # Because birth year is a solid launching point...
    # Review all birth years and check to see if that number
    #   is present in all other ranges.
    # Instead of using a hash table, simply keep track of the max
    #   year in a tuple. (year, max winner)
    # STEPS:
    #     1. loop through peeps array
    #     2. take birth year, assess by slice if in range
    #     3. if each positive get a local add
    #     4. then finally compare to current max
    # TCs -- O(N) 1st for loop Time/Space
    #     -- O(N) 2nd and 3rd fors Time/Space
    #        this could be improved w/hash

    #            year,   max init
    max_alive = (0, float("-inf"))

    for idx in reversed(range(len(peeps))):
        # identify slice (nested for?)
        # backward and forward (assume middle on first)
        birth = peeps[idx][0]
        arrears = peeps[0:idx] # not inclusive of current
        forward = peeps[idx+1:len(peeps)-1] # me to end of peeps
        # don't forget to count self
        local_max = 1
        for si, ei in arrears:
            if birth in range(si, ei): # already a tuple with ints
                local_max += 1
        for sy, ey in forward: 
            if birth in range(sy, ey):
                local_max += 1

        # finally, we update max if necessary
        if local_max > max_alive[1]: # strictly greater than
            max_alive = (birth, local_max)

    # a final return
    return max_alive


def optimized_alive(peeps):
    # We keep track of 2 figures: 1-running alive, 2-max alive
    # We go forward through the timeline by birth
    #   -births add to running total
    #   -deaths subtract
    #   -compare running alive to max, update year and max

    # We need a data structure to allow a linear evaluation
    years = dict()

    # For both births/deaths O(B+D)
    for birth, death in peeps:
        build_years(birth, "B", years)
        build_years(death, "D", years)
    
    # Initialize an answer to compare values
    max_value = (0, 0)
    running_max = max_value[1]

    # Run through from lowest to highest O(Y)
    for year in sorted(years):
        # eval birth then death O(1)
        births = get_event_year(years, year, "B")
        deaths = get_event_year(years, year, "D")
        running_max += births
        running_max -= deaths
        if running_max > max_value[1]:
            max_value = (year, running_max)

    return max_value


def build_years(year, event, years):
    if year in years:
        try:
            years[year][event] += 1
        except KeyError:
            years[year][event] = 1
    else:
        years[year] = {event: 1}


def get_event_year(years, year, event):
    try:
        return years[year][event]
    except KeyError:
        return 0




if __name__ == "__main__":

    # Brute force approach
    # 1- get min from tuples [0], get max from [1]
    # 2- O(N) build hash table where key = year from min to max
    # 3- loop through every range and add to key value if present
    peeps = [
        (1945, 2000), (1944, 2001), (1950, 2001), (1952, 2012), (1948, 2011), (1939, 2001), (1940, 2009), (1941, 2010), (1941, 2009),
        (1965, 2000), (1965, 2001), (1965, 2001), (1965, 2012), (1948, 2011), (1939, 2001), (1940, 2009), (1941, 2010), (1941, 2009),
        (1895, 1905),
        (1905, 1964),
        (1905, 1964),
        (1905, 1964)
    ]

    peeps = [
        (1803, 1900),
        (1825, 1900),
        (1890, 2001),
        (1925, 1999),
        (1999, 2012),
    ]

    years = optimized_alive(peeps)
    print(years)
