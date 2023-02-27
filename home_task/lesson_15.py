import pyaudio
import wave


def play_wav(filename):
    '''
    Функція для відтворення .wav-файлів
    :param filename: ім'я файлу
    :return: None
    '''
    CHUNK = 1024
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    # Відкриваємо аудіо-стрім та відтворюємо аудіо у фрагментах розміром CHUNK
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()


class Transport:
    '''
    Клас-батько, який описує транспортний засіб
    '''
    def __init__(self, state_number, number_of_wheels, engine_power, maximum_speed):
        self.__state_number = state_number
        self.__number_of_wheels = number_of_wheels
        self.__engine_power = engine_power
        self.__maximum_speed = maximum_speed

    def get_state_number(self):
        return self.__state_number

    def set_state_number(self, state_number):
        '''
        Перевірка коректності номеру автомобіля
        :param state_number: номер автомобіля
        :return: None
        '''

        if len(state_number) != 8:
            raise ValueError("State number must have 8 characters")
        if not state_number[:2].isalpha() or not state_number[-2:].isalpha():
            raise ValueError("First two and last two characters of state number must be letters")
        if not state_number[2:6].isdigit():
            raise ValueError("Characters 3-6 of state number must be digits")
        self.__state_number = state_number

    def set_number_of_wheels(self, number_of_wheels):
        '''
        Перевірка коректності кількості коліс
        :param number_of_wheels: кількість коліс
        :return: None
        '''
        if number_of_wheels <= 0:
            raise ValueError("Number of wheels must be positive")
        self.__number_of_wheels = number_of_wheels

    def get_engine_power(self):
        return self.__engine_power

    def set_engine_power(self, engine_power):
        '''
        Перевірка коректності потужності двигуна
        :param engine_power: величина потужності двигуна
        :return:None
        '''
        if engine_power <= 0:
            raise ValueError("Engine power must be positive")
        self.__engine_power = engine_power

    def get_maximum_speed(self):
        return self.__maximum_speed

    def set_maximum_speed(self, maximum_speed):
        '''
        Перевірка коректності максимальної щвидкості
        :param maximum_speed: показник максимальної швидкості
        :return: None
        '''
        if maximum_speed <= 0:
            raise ValueError("Maximum speed must be positive")
        self.__maximum_speed = maximum_speed


class Bicycle(Transport):
    '''
    дочірній клас Transport
    '''
    def honk(self):
        '''
        Викликає звук
        :return:  None
        '''
        print(f'{Bicycle.__name__} honk')
        solo_say = play_wav('Bicycle.wav')
        print('STOP')
        print()


class Car(Transport):
    def __init__(self, state_number, number_of_wheels, engine_power, maximum_speed, body_type):
        super().__init__(state_number, number_of_wheels, engine_power, maximum_speed)
        self.__body_type = body_type

    def get_body_type(self):
        return self.__body_type

    def set_body_type(self, body_type):
        self.__body_type = body_type

    def honk(self):
        print(f'{Car.__name__} honk')
        play_wav('CarHorn.wav')
        print('STOP')
        print()


class Bus(Transport):
    def __init__(self, state_number, number_of_wheels, engine_power, maximum_speed, number_of_passengers):
        super().__init__(state_number, number_of_wheels, engine_power, maximum_speed)
        self.__number_of_passengers = number_of_passengers

    def get_number_of_passengers(self):
        return self.__number_of_passengers

    def set_number_of_passengers(self, number_of_passengers):
        if number_of_passengers <= 0:
            raise ValueError("Number of passengers must be positive")
        self.__number_of_passengers = number_of_passengers

    def honk(self):
        print(f'{Bus.__name__} honk')
        solo_say = play_wav('Bus.wav')
        print('STOP')
        print()


class Truck(Car):
    def __init__(self, state_number, number_of_wheels, engine_power, maximum_speed, body_type, payload_capacity):
        super().__init__(state_number, number_of_wheels, engine_power, maximum_speed, body_type)
        self.__payload_capacity = payload_capacity

    def get_payload_capacity(self):
        return self.__payload_capacity

    def set_payload_capacity(self, payload_capacity):
        if payload_capacity <= 0:
            raise ValueError("Payload capacity must be positive")
        self.__payload_capacity = payload_capacity

    def honk(self):
        print(f'{Truck.__name__} honk')
        solo_say = play_wav('Truck.wav')
        print('STOP')
        print()


class Animals:
    def __init__(self, name, weight, speed):
        self._name = name
        self._weight = weight
        self._speed = speed

    def set_name(self, new_name):
        self._name = new_name

    def set_weight(self, new_weight):
        self._weight = new_weight

    def set_speed(self, new_speed):
        self._speed = new_speed


class Birds(Animals):
    def __init__(self, name, weight, speed, feather_color):
        super().__init__(name, weight, speed)
        self._feather_color = feather_color

    def say(self):
        print(f'{Birds.__name__} say')
        solo_say = play_wav('Birds.wav')
        print('STOP')
        print()


class Reptiles(Animals):
    def __init__(self, name, weight, speed, temperature_preference):
        super().__init__(name, weight, speed)
        self._temperature_preference = temperature_preference

    def say(self):
        print(f'{Reptiles.__name__} say')
        solo_say = play_wav('Reptiles.wav')
        print('STOP')
        print()


class Mammals(Animals):
    def __init__(self, name, weight, speed, milk_production):
        super().__init__(name, weight, speed)
        self._milk_production = milk_production

    def say(self):
        print(f'{Mammals.__name__} say')
        solo_say = play_wav('Mammals.wav')
        print('STOP')
        print()


# створення екземпляру класу Bicycle
bicycle = Bicycle("AB123CD", 2, 1, 20)
bicycle.honk()

# створення екземпляру класу Car
car01 = Car("BC456EF", 4, 200, 180, "Sedan")
car01.honk()

# створення екземпляру класу Bus
bus01 = Bus('AA1234AA', 6, 200, 80, 30)
bus01.honk()

# створення екземпляру класу truck
my_truck = Truck("AB1234BC", 8, 400, 120, "Box", 1200)
my_truck.honk()

bird = Birds("Папуга", 0.2, 10, "Зелений")
reptile = Reptiles("Крокодил", 100, 5, "Теплолюбивий")
mammal = Mammals("Кінь", 500, 40, "Високий")
bird.say()
reptile.say()
mammal.say()
