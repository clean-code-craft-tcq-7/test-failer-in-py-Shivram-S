def sensorStubRain():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }
def sensorStubPrep():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 49
    }
def sensorStubCold():
    return {
        'temperatureInC': 20,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 49
    }
def sensorStubSunny():
    return {
        'temperatureInC': 27,
        'precipitation': 10,
        'humidity': 26,
        'windSpeedKMPH': 49
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50 or readings['precipitation'] >= 60:
            weather = "Alert, Stormy with heavy rain"
    else : 
        weather = "Cold day"     
    return weather


def testWeather(StubWeather):
    if StubWeather == 'rain':
        weather = report(sensorStubRain)
        assert("rain" in weather)
    elif StubWeather == 'prep':
        weather = report(sensorStubPrep)
        assert("rain" in weather)
    elif StubWeather == 'cold':
        weather = report(sensorStubCold)
        assert("Cold" in weather)
    elif StubWeather == 'sun':
        weather = report(sensorStubSunny)
        assert("Sunny" in weather)
    else:
        assert(True == False)

if __name__ == '__main__':
    testWeather('rain')
    testWeather('prep')
    testWeather('sun')
    testWeather('cold')
    print("All is well")
