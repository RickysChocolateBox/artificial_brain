import pyaudio
import numpy as np
import threading
import scipy.signal
import librosa


class AudioSource:
    def __init__(self, rate=44100, channels=2, chunk_size=1024):
        self.rate = rate
        self.channels = channels
        self.chunk_size = chunk_size

        self.p = pyaudio.PyAudio()

        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk_size)

        self.audio_buffer = []
        self.recording = False

    def start_recording(self):
        self.recording = True
        self.capture_thread = threading.Thread(target=self.capture_audio)
        self.capture_thread.start()

    def stop_recording(self):
        self.recording = False
        self.capture_thread.join()

    def capture_audio(self):
        while self.recording:
            data = self.stream.read(self.chunk_size)
            audio_data = np.frombuffer(data, dtype=np.int16)
            self.audio_buffer.append(audio_data)

    def apply_high_pass_filter(self, cutoff_frequency=100):
        sos = scipy.signal.butter(4, cutoff_frequency, 'hp', fs=self.rate, output='sos')
        filtered_audio = []
        for audio_chunk in self.audio_buffer:
            filtered_chunk = scipy.signal.sosfilt(sos, audio_chunk)
            filtered_audio.append(filtered_chunk)
        self.audio_buffer = filtered_audio

    def apply_noise_reduction(self, noise_reduction_factor=0.9):
        noise_reduced_audio = []
        for audio_chunk in self.audio_buffer:
            reduced_chunk = audio_chunk * noise_reduction_factor
            noise_reduced_audio.append(reduced_chunk)
        self.audio_buffer = noise_reduced_audio

    def apply_pitch_shift(self, pitch_shift_factor=2):
        pitch_shifted_audio = []
        for audio_chunk in self.audio_buffer:
            shifted_chunk = librosa.effects.pitch_shift(audio_chunk, self.rate, pitch_shift_factor)
            pitch_shifted_audio.append(shifted_chunk)
        self.audio_buffer = pitch_shifted_audio

    def get_audio_data(self):
        return self.audio_buffer

    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()