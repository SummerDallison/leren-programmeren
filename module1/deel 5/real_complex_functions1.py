def get_value(data: str, separator: str, position: int) -> str:
   splitted_strings = toets_data.split(separator)
   
   if 0 <= position < len(splitted_strings):
      return splitted_strings[position]
   else:
      return None

toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','
position = 8

result = get_value(toets_data, separator, position)
print(result)