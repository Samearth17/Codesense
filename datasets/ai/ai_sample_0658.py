def temperature_conversion(temperature, conversion):
 switch (conversion):
  case 'FtoC':
   return (temperature - 32) * (5 / 9)
  case 'CtoF':
   return (temperature * (9 / 5)) + 32
  case 'FtoK':
   return (temperature - 32) * (5 / 9) + 273.15
  case 'KtoF':
   return (temperature - 273.15) * (9 / 5) + 32
  case 'CtoK':
   return temperature + 273.15
  case 'KtoC':
   return temperature - 273.15

# converting a temperature of 100F to Celsius
temperature_in_celsius = temperature_conversion(100, 'FtoC')
print("Temperature in Celsius:", temperature_in_celsius)