

# Audio Watermarking 

## Objective

The objective of this assignment is to encode and decode a watermark in an audio file, where the watermark is represented by an 8-bit binary number.

## Background

Audio watermarking involves hiding information in an audio signal, known as a watermark. This watermark is embedded into the audio in various ways and can be decoded at the receiver's end. The primary goal is to embed information in a way that is resilient to attacks, noise, and imperceptible to the human ear.

## Applications

Audio watermarking has various applications, including:
- Copyright Protection
- Ownership Identification
- Broadcasting
- Voice Assistants in Smart Home Devices

## Techniques

The assignment explores different techniques for audio watermarking, including:

1. **LSB (Least Significant Bit) Technique**: Modifying the least significant bit of each audio sample to embed a hidden message. This technique is simple and widely used in low complexity applications.

2. **Phase Coding**: Modifying the phase of certain audio samples to embed a hidden message. Phase coding is robust and difficult to remove without degrading audio quality.

3. **Spread Spectrum**: Spreading the hidden message across a wide range of frequencies using a special algorithm. It's challenging to detect and remove the spread spectrum audio signal without the key.

4. **Echo Hiding**: Embedding a hidden message by introducing slight delays in the audio signal to create an echo. The delay times represent binary data, and extracting the message involves analyzing the echo pattern.

## Assignment Summary

In this assignment, the Least Significant Bit (LSB) Audio Watermarking Technique is implemented using Python. Additionally, a GUI is integrated using Tkinter to facilitate user interaction. The following user inputs are collected:

1. The audio file for watermarking (with the option to upload an audio file to the system).
2. The data to be encoded (an 8-bit binary number).

Two buttons, "Encode" and "Decode," correspond to specific functions in the imported Python script to perform encoding and decoding. When an audio file is selected and the "Encode" button is clicked, the encoded version of the WAV file is saved in the same folder. The encoded file can then be uploaded for decoding, and the decoded message is displayed.

## Conclusion and Inference

The assignment successfully implements the LSB Audio Watermarking Technique with minimal noticeable distortion. The methodology used for embedding and extracting data is based on simple bitwise manipulations. Phase coding is identified as a more robust technique that eliminates distortions present in the LSB method. The performance of other audio watermarking techniques was also explored and understood.

## References

- [Audio Watermarking Algorithm](https://www.amazon.science/blog/audio-watermarking-algorithm-is-first-to-solve-second-screen-problem-in-real-time)
- [Hiding Data in Sound](https://medium.com/intrasonics/hiding-data-in-sound-c8db3de5d6e0)
- [How It Works](https://www.intrasonics.com/how-it-works.html)
