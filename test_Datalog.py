from Datalog import Datalogtest
import time


# Testing that battery reading descends over time
def test_timer():
    get_dat = Datalogtest(interval=1, export=False)
    time.sleep(5)
    list = get_dat.data['Battery']
    print(list)
    assert list == sorted(list, reverse=True)
    

# Generate sample output data log
data_log = Datalogtest(1)
time.sleep(3)
data_log.stop()
