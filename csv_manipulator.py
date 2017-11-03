import re

# just a test to manipulate integer sign in a csv without modifying the other values
def csv_integer_sign_manip(input_file_name, output_file_name, value_pos):
    with open(input_file_name) as file:
        data = file.readlines()
      
    manip_data = list()
    manip_data.append(data[0])
    for element in data[1:]:
        pos_arr = [m.start() for m in re.finditer(',', element)]
        end_old_string = pos_arr[value_pos] + 1
        value = int(element[end_old_string:pos_arr[value_pos+1]])
        if value is not 0:
            # no manipulate remove or add -
            if value < 0:
                new_element = element[:end_old_string] + element[(end_old_string+1):]
            else:
                new_element = element[:end_old_string] + '-' + element[end_old_string:]
            manip_data.append(new_element)
        else:
            manip_data.append(element)

    with open(output_file_name, 'w') as out:
        out.writelines(manip_data)
