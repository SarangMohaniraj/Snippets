import time

class Timer:
    def __init__(self):
      self.start_time = time.time()

    def elapsed_time(self,start_time=None):
      start_time = self.start_time if start_time == None else start_time
      return time.strftime("%Hh, %Mm, %Ss", time.gmtime(time.time()-start_time)) if time.time()-start_time > 1 else f"{time.time()-start_time:.3f}μs"


