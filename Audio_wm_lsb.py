# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:44:44 2023

@author: ADITYA VENKATA
"""

import os.path
import wave

from Audiowm import Audio_wm


class LSB_Audiowm(Audio_wm):  
    def saveToLocation(self, audioArray, location):
      
        dir = os.path.dirname(location)
        self.newAudio = wave.open(dir + "/encoded_audio.wav", 'wb')
        self.newAudio.setparams(self.audio.getparams())
        self.newAudio.writeframes(audioArray)
        self.newAudio.close()
        self.audio.close()
        return dir + "/encoded_audio.wav"

    def enc_Audio(self, audioLocation, stringToEncode) -> str:
        #audioLocation is the path and stringtoEncode is the message- the binary representation
        # is taken as a string and encoded on to the lsb
        audioArray = self.convertToByteArray(audioLocation)
       
        #appending the string upto a length that is a multiple of 8 so that it can be converted
        # into the byte representation. The string is appended with #
        #the ord function converts each character to ASCII
        #bin converts each ASCII to binary
        
        stringToEncode = stringToEncode + int((len(audioArray) - (len(stringToEncode) * 8 * 8)) / 8) * '#'
        #the resultant list of integers is sored in the bits array
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in stringToEncode])))
        #iterating ovr the bits array and encoding each bit to the LSB of the audio 
        for i, bit in enumerate(bits):
            audioArray[i] = (audioArray[i] & 254) | bit
        encodedAudio = bytes(audioArray)
        return self.saveToLocation(encodedAudio, audioLocation)

    def dec_Audio(self, audioLocation) -> str:   #perfroming decoding
       
        audioArray = self.convertToByteArray(audioLocation)  #converting the encoded audio file to a byte array
        #extracting the LSB of each byte in the audioArray and storing it in decodedArray
        decodedArray = [audioArray[i] & 1 for i in range(len(audioArray))]
        self.audio.close()
        return \
            "".join(
                chr(int("".join(map(str, decodedArray[i:i + 8])), 2)) for i in range(0, len(decodedArray), 8)).split(
                "###")[0]  #

    def convertToByteArray(self, audioLocation):
      
        self.audio = wave.open(audioLocation, mode="rb")
        return bytearray(list(self.audio.readframes(self.audio.getnframes())))