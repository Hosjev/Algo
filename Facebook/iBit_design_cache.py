class Cache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        Performant issues: scalability, availability
        Questions: Without going to external/ready-to-use load balancers,
                   what is best intra/extranet solution?
                   How many machines? Cores? How much memory? Type of memory?
                   Multiprocessing better than threading if memory bottlenecked.
                   Availability vs consistency?
                   *Implement LRU when cache reaches size or as error handling?
        """
        self.cache = dict().fromkeys([i for i in range(capacity)])


    def get(self, key):
        """
        :type key: int
        :rtype: value
        """
        try:
            return self.cache[key]
        except KeyError:
            return self.put(key)
        

    def put(self, key):
        """
        :type key: int
        :type value: int
        :rtype: value
        """
        self.cache[key] = self._get_database(key)
        return self.cache[key]

        
    def _get_database(self, key):
        """
        :type key: int
        :type value: int
        :rtype: None
        MOCK database call
        TODO: 1) set limit size
              2) set wait time
              3) at the least, async call here
        """
        return None


dc = Cache(10)
print(dc.get(12))
