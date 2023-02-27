import pyaudio
import wave


class Transport:
    def __init__(self, state_number, number_of_wheels, engine_power, max_speed):
        self.__state_number = state_number
        self.__number_of_wheels = number_of_wheels
        self.__engine_power = engine_power
        self.__max_speed = max_speed

    def get_state_number(self):
        return self.__state_number

    def get_number_of_wheels(self):
        return self.__number_of_wheels

    def get_engine_power(self):
        return self.__engine_power

    def get_max_speed(self):
        return self.__max_speed

    def check_data(self):
        if len(self.__state_number) != 8:
            return False
        if not self.__state_number[:2].isalpha() or not self.__state_number[-2:].isalpha():
            return False
        if not self.__state_number[2:5].isdigit():
            return False
        if self.__number_of_wheels <= 0 or self.__engine_power <= 0 or self.__max_speed <= 0:
            return False
        return True


class Bicycle(Transport):
    def say(self):
        chunk = 1024
        wav_file = wave.open("Bicycle.wav", 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
                        channels=wav_file.getnchannels(),
                        rate=wav_file.getframerate(),
                        output=True)
        data = wav_file.readframes(chunk)

        while data:
            stream.write(data)
            data = wav_file.readframes(chunk)

        stream.stop_stream()
        stream.close()
        p.terminate()
        wav_file.close()


bicycle = Transport("A142CD", 2, 1, 20)
print(bicycle.get_state_number())

# виклик методу say
