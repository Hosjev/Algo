class CPUThresholds:
    def user_space(self, nth):
        #procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
        #r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
        #2  0       177764       193216       294848      1218692    0    0     0     0  533  468  (51) 1  49   0   0
        # Above "51" reps a single CPU taken
        count = 1
        last, current = 0, 1
        while count != nth:
            temp = last + current
            last = current
            current = temp
            count += 1
        return current

    def system_space(self):
        # dd if=/dev/urandom of=/tmp/500MofShit bs=1M count=500
        #procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
        #r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
        #1  1      177764       134624      281660      1297124      0  0       0 40996  790  728  0  (55)  6  39   0
        return

    def user_sys_space(self):
        # Toptal/mult_proc.py => fire 12 children off a fork pool and download 40+ images avg 225k in size
        #procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
        #r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
        #1  0       177764       589380       203284       902644    0    0   124     0  387  505   8   1  91   1   0
        #3  0       177764       525948       203288       904596    0    0    12     0 5550 6971  17  19  56   7   0
        #1  0       177764       521444       203288       906416    0    0     0     0 5758 7687  14  12  74   0   0
        #1  0       177764       594288       203296       911756    0    0     0    48 3399 5262   8   7  82   2   0
        return


if __name__ == "__main__":
    us = CPUThresholds()
    print(us.user_space(1000000))
