
import array
import random
import wave

# Code in this module follows examples from:
#
# http://code.activestate.com/recipes/578168-sound-generator-using-wav-file/
# http://noisehack.com/generate-noise-web-audio-api/

def create_white_noise(fn, duration=2):
    data = array.array('h')
    sample_rate = 44100
    num_channels = 1
    data_size = 2

    for i in range(sample_rate * duration):
        sample = (2 * random.random()) - 1
        data.append(int(sample * 32767))
        
    fd = wave.open(fn, 'w')
    fd.setparams((num_channels,
                  data_size,
                  sample_rate,
                  sample_rate * duration,
                  "NONE",
                  "Uncompressed"))
    fd.writeframes(data.tostring())
    fd.close()

    return

def create_pink_noise(fn, duration=2):
    data = array.array('h')
    sample_rate = 44100
    num_channels = 1
    data_size = 2

    b0 = 0.0
    b1 = 0.0
    b2 = 0.0
    b3 = 0.0
    b4 = 0.0
    b5 = 0.0
    b6 = 0.0
    
    for i in range(sample_rate * duration):
        white = (2 * random.random()) - 1
        b0 = (0.99886 * b0) + (white * 0.0555179)
        b1 = (0.99332 * b1) + (white * 0.0750759)
        b2 = (0.96900 * b2) + (white * 0.1538520)
        b3 = (0.86650 * b3) + (white * 0.3104856)
        b4 = (0.55000 * b4) + (white * 0.5329522)
        b5 = (-0.7616 * b5) - (white * 0.0168980)
            
        sample = (b0 + b1 + b2 + b3 + b4 + b5 + b6 + (white * 0.5362)) * 0.11
        sample *= 32767
        data.append(int(sample))

        b6 = white * 0.115926
        
    fd = wave.open(fn, 'w')
    fd.setparams((num_channels,
                  data_size,
                  sample_rate,
                  sample_rate * duration,
                  "NONE",
                  "Uncompressed"))
    fd.writeframes(data.tostring())
    fd.close()

    return

def create_brown_noise(fn, duration=2):
    data = array.array('h')
    sample_rate = 44100
    num_channels = 1
    data_size = 2

    last_sample = 0.0
    for i in range(sample_rate * duration):
        white = (2 * random.random()) - 1
        sample = (last_sample + (0.02 * white)) / 1.02
        last_sample = sample
        data.append(int(sample * 32767 * 3.5))
        
    fd = wave.open(fn, 'w')
    fd.setparams((num_channels,
                  data_size,
                  sample_rate,
                  sample_rate * duration,
                  "NONE",
                  "Uncompressed"))
    fd.writeframes(data.tostring())
    fd.close()

    return    

if __name__ == '__main__':
    create_white_noise('collateral/samples/white_noise.wav')
    create_pink_noise('collateral/samples/pink_noise.wav')
    create_brown_noise('collateral/samples/brown_noise.wav')
    
