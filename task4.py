import numpy as np
from mpi4py import MPI
import time
import math


def countPiValue(generatedDots):
    amountOfAllDots = len(generatedDots)
    dotsInCircle = \
        np.count_nonzero(((generatedDots.T[0])**2 + (generatedDots.T[1])**2) <= 1)
    PiValue = 4 * (dotsInCircle / amountOfAllDots)
    return PiValue


if __name__ == '__main__':

    startTime = time.time()
    communicator = MPI.COMM_WORLD
    size = communicator.Get_size()
    rank = communicator.Get_rank()
    dotsData = []


    if rank == 0:
        totalDots = 10000000
        dotsOnAxis = np.random.rand(totalDots, 2)
        dotsPerSize = math.ceil(totalDots / size)

        for i in range(0, size):
            dotsData.append(dotsOnAxis[0: (i + 1) * dotsPerSize])


    scatterdData = communicator.scatter(dotsData, root=0)
    PiValue = countPiValue(scatterdData)
    endTime = time.time() - startTime
    outputs = communicator.gather({"value": PiValue, "time": endTime}, root=0)

    if rank == 0:
        for output in outputs:
            print("PI value: ", output["value"], "\nFinished in", output["time"])
