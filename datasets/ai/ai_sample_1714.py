def convert_temperature(from_scale, to_scale, temperature):
 '''converts temperature between celsius, fahrenheit, and kelvin
 
 Arguments:
 from_scale -- the scale to convert from
 to_scale -- the scale to convert to
 temperature -- the temperature to convert
 
 Returns:
 the converted temperature
 '''
 if from_scale == 'C':
 if to_scale == 'F':
 return temperature * 9/5 + 32
 elif to_scale == 'K':
 return temperature + 273.15
 elif from_scale == 'F':
 if to_scale == 'C':
 return (temperature - 32)*5/9
 elif to_scale == 'K':
 return (temperature - 32)*5/9 + 273.15
 elif from_scale == 'K':
 if to_scale == 'C':
 return temperature - 273.15
 elif to_scale == 'F':
 return (temperature - 273.15)*9/5 + 32
 else:
 return temperature