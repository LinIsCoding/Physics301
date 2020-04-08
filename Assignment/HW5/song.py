import numpy as np
import subprocess as sub
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

class Tone:
    def __init__(self):
        self.f = 0.
        self.dur = 0.
        self.sr = 44100
        self.signal = None
        self.orig_signal = None
        self.overtones = {}
        self.OT_num = 0
        
    def get_tone(self, f, d, playsound=False):
        amp = 2**10
        time_pts = np.linspace(0, d, int(d*self.sr))
        tone = amp*np.sin(np.pi*2*f*time_pts)
        self.f = f
        self.dur = d
        self.orig_signal = tone
        if playsound:
            self.play_sound()
        return tone
    
    def get_overtone(self, multi, playsound=False):
        amp = 2**10
        time_pts = np.linspace(0, self.dur, int(self.dur*self.sr))
        overtone_signal = amp*np.sin(np.pi*2*multi*self.f*time_pts)
        self.overtones[multi] = overtone_signal
        self.OT_num += 1
        if playsound:
            self.play_sound()
        
    def comb_tones(self, weights=[]):
        sum_weights = sum(weights)
        time_pts = np.linspace(0, self.dur, int(self.dur*self.sr))
        
        if sum_weights == 0:
            new_tone = self.orig_signal
            for key in self.overtones:
                tone = self.overtones[key]
                new_tone += tone
        else :
            counter = 0
            new_tone = self.signal*weights[counter]/sum_weights
            counter += 1
        
            # pre-processing the weights
            length = len(weights)
            for i in range(length, self.OT_num):
                weights.append(0)

            for key in self.overtones:
                tone = self.overtones[key]*weights[counter]/sum_weights
                counter += 1
                new_tone += tone
                
        self.signal = new_tone
        return new_tone
                

    def play_sound(self, vol = 0.05, sample_rate = 44100, outside_signal = None):
        try:
            len(outside_signal)
        except:
            write('temp.wav', sample_rate, self.signal)
        else:
            write('temp.wav', sample_rate, outside_signal)
                  
        sub.call(['afplay', 'temp.wav', '-v', str(vol)])
        sub.call(['rm', 'temp.wav'])
        
    def plot_fourier(self, sample_rate = 44100, freq_lim = 2000., amp_lim = 1e7):
        signal = self.signal
        ft = np.fft.fft(np.float64(signal))
        freq = np.fft.fftfreq(signal.shape[0], d = 1/sample_rate)
        plt.figure()
        plt.title('Real')
        plt.plot(freq, ft.real, 'b-')
        plt.xlim([-freq_lim, freq_lim])
        plt.figure()
        plt.title('Imaginary')
        plt.plot(freq, ft.imag, 'g-')
        plt.xlim([-freq_lim, freq_lim])
        plt.show()
        
    def plot_sound(self, t_lim = 0.02):
        signal = self.signal
        time_pts = np.linspace(0, self.dur, int(self.dur*self.sr))
        plt.figure()
        plt.plot(time_pts, signal, '-')
        plt.xlim(0., t_lim)
        plt.title("Sound Wave vs. Time")
        plt.show()

def generate_melody():
    Atone = Tone()
    A = Atone.get_tone(440., 0.5)
    Btone = Tone()
    B = Btone.get_tone(493.88, 0.5)
    Dtone = Tone()
    D = Dtone.get_tone(587.33, 0.5)
    Gtone = Tone()
    G = Gtone.get_tone(392, 0.5)
    melody = np.concatenate((B,A,G,A,B,B,B,B,A,A,A,A))
    Atone.play_sound(outside_signal = melody)

def demo():
    tone = Tone()
    simple_tone = tone.get_tone(440., 0.5) 
    tone.get_overtone(2) 
    tone.get_overtone(3) 
    tone.get_overtone(4)
    rich_tone = tone.comb_tones()
    print("For A tone, the frequency, sampling_rate, duration,and number of overtones are: {}, {}, {}, {}".format(tone.f, tone.sr, tone.dur, tone.OT_num))
    tone.play_sound()
    tone.plot_sound() 
    tone.plot_fourier(freq_lim = 2000.)

if __name__ == "__main__":
    generate_melody()
    demo()