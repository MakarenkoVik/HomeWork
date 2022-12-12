class Temperature_conversion:
        
    def celsius_to_kelvin(self, temperature):
        return temperature + 273.15
    
    def celsius_to_fahrenheit(self, temperature):
        return temperature * (9 / 5) + 32

    def fahrenheit_to_celsius(self, temperature):
        return (temperature - 32) * (5 / 9)

    def kelvin_to_celsius(self, temperature):
        return temperature - 273.15


temperature = Temperature_conversion()
print(temperature.celsius_to_fahrenheit(20))
print(temperature.fahrenheit_to_celsius(50))
print(temperature.celsius_to_kelvin(58))
