import pyaudio
import wave


def play(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data = wf.readframes(chunk)

    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    pa.terminate()

class Transport:
    def __init__(self, state_number, number_of_wheels, engine_power, maximum_speed):
        self.state_number = state_number
        self.number_of_wheels = number_of_wheels
        self.engine_power = engine_power
        self.maximum_speed = maximum_speed

        if self.check_data() == False:
            print("Incorrect data!")
        else:
            print("Data is correct.")

    def check_data(self):
        if len(self.state_number) != 8:
            return False
        if not self.state_number[:2].isalpha() or not self.state_number[-2:].isalpha():
            return False
        if not self.state_number[2:5].isdigit():
            return False
        if self.number_of_wheels < 0 or self.engine_power < 0 or self.maximum_speed < 0:
            return False
        return True


class Bicycle(Transport):
    def say(self, solo_say = 'Bicycle.wav'):
        print(f'{self.__class__.__name__} say')
        rain = play(solo_say)
        print('STOP')


bicycle01 = Bicycle("AA3234AA", 2, 0, 25)
bicycle01.say()
