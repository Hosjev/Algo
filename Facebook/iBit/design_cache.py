class Cache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        Performant issues: scalability, availability
        Questions: Without going to external/ready-to-use distributed caches (memcached),
                   what is best intra/extranet solution?
                   What kind of data? What is calling app? Expected throughput?
                   Multiprocessing better than threading if memory bottlenecked.
                   Availability vs consistency?
                   *Implementing LRU seems to be best solution for homegrown
        Aspects of distributed cache:
            1) cache size - the # of records each cache can hold
            2) cache expiration - the expiration time of each record (not accessed?)
            3) cache invalidation - when to remove a cache from network if data out-of-sync/stale
        """
        # Mock cache
        self.capacity = capacity
        self.cache = dict().fromkeys([i for i in range(capacity)])


    def get(self, key):
        """
        :type key: int
        :rtype: value
        """
        try:
            return self.cache[key]
        except KeyError:
            return self.set(key)
        

    def set(self, key):
        """
        :type key: int
        :type value: int
        :rtype: value
        """
        insertion = self._get_database(key)
        if len(self.cache) >= capacity:
            self._remove_tail()
        self.cache[key] = insertion
        return self.cache[key]


    def _remove_tail(self):
        """
        W/o constraints, remove end
        Using Py dict, b/c keys are unique,
            employ swapping method when full
        """
        self.cache.pop()


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
