import mouse  # ?
import numpy as np
import time

while True:
    mouse.click("left")
    time.sleep(1 + np.random.rand(1)[0])
