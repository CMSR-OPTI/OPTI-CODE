import smbus # is this the one needed?
# might need to enable i2c in system settings

class Thermometer:

    def __init__(self):
        self.temperature = 0
        # this could be changed
        self.TEMP_ADDR = 0x48

        # is this the right bus? is it set up somewhere else?
        self.bus = smbus.SMBus(0)

        #have something to check if device is connected? maybe later

    def get_measurement(self):
        t_low = self.bus.read_byte_data(self.TEMP_ADDR, 0b10)
        t_high = self.bus.read_byte_data(self.TEMP_ADDR, 0b11)

        bit_value = (t_high<<4) | (t_low>>4);
        # do negatives need to be handled? in that case, fix this
        # if((bit_value & 0x800) != 0):
        #     # this means we have a negative number
        #     bit_value |= 0xFFFFF000;
        result = bit_value*0.0625;
        
        self.temperature = result;

    def display_data(self):
        print(f"temperature: {self.temperature}")