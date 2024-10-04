from test_lib import test, report

toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','

def get_value(data: str, separator: str, position: int) -> str:
    splitted_strings = data.split(separator)  
    if position < len(splitted_strings):  
        return splitted_strings[position]  


data = toets_data
seperator = separator
position = 8
expect_content = 'Bram:6'
calculated_content = get_value(data, seperator, position)
name = 'naam'
test(name, expect_content, calculated_content )
report()