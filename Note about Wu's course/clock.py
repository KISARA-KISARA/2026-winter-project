import time
class CLOCK():
    def __init__(self,hour,min,sec):
        self.hour=hour
        self.min=min
        self.sec=sec
    def show(self):
        print(f"{self.hour:02d}:{self.min:02d}:{self.sec:02d}")
    def run(self):
        self.sec+=1
        if(self.sec==60):
            self.min+=1
            self.sec=0
            if(self.min==60):
                self.min=0
                self.hour+=1
                if(self.hour==24):
                    self.hour=0
clock=CLOCK(10,5,30)
while 1:
    clock.show()
    time.sleep(1)
    clock.run()
