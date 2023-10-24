# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:47:38 2023

@author: ADITYA VENKATA
"""

from abc import ABC, abstractmethod


class Audio_wm(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def enc_Audio(self, audioLocation, data_to_encode) -> str:
        pass

    @abstractmethod
    def dec_Audio(self, audioLocation) -> str:
        pass

    @abstractmethod
    def convertToByteArray(self, audio):
        pass

    @abstractmethod
    def saveToLocation(self, audioArray, location) -> str:
        pass