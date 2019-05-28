import utils.pulse as pulse
import numpy as np
import random as rnd

class Synchronizer:
    """
    This class implements the synchronizer
    """

    def __init__(self, wave):
        """
        Constructor of the synchronizer

        :param wave: the signal that the waveformer gives as output
        """

        self.wave = wave

