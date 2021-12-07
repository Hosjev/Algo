class IOThresholds:
    def buffer_in(self):
        # PRE-run
        #1  0       177764       589380       203284       902644    0    0   124     0  387  505   8   1  91   1   0
        # dd if=/tmp/2GofShit of=/dev/null bs=1M => writing to nothing but/w high READs and Cache is filling up/grow
        #procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
        #r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
        #2  0       178020       116736       126776      1453364    0    0 44032     0  458  520   1   6  76  18   0
        #1  1       178020       106976       126776      1463216    0    0 42496     0  385  479   0   4  78  18   0
        #1  1       178020       115288       126776      1454800    0    0 43520     0  496  584   1   5  68  26   0
        #1  1       178020       115312       126776      1453488    0    0 44544     0  350  470   0   4  50  46   0
        return 

    def buffer_out(self):
        # dd if=/dev/urandom of=/tmp/500MofShit bs=1M count=500
        #procs -----------------------memory---------------------- ---swap-- -----io---- -system-- --------cpu--------
        #r  b         swpd         free         buff        cache   si   so    bi    bo   in   cs  us  sy  id  wa  st
        #1  1      177764       134624      281660      1297124      0  0       0 40996  790  728  0  (55)  6  39   0
        return


if __name__ == "__main__":
    io = IOThresholds()
