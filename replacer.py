import csv
import json

def replaceFields(original_file_name, modified_file_name, replacement_map):
  with open(original_file_name, 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = [cell for cell in reader]

  for cell in data:
    for i in range(len(cell)):
      if cell[i] == '-24':
        cell[i+1] = 'Bills'
        cell[i+2] = 'Tabacco'

      for original, replacement in replacement_map.items():
        if original in cell[i]:
          cell[i] = replacement['replace']
          cell[i-1] = replacement['category']

  with open(modified_file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

  return modified_file_name

with open('config.json', 'r') as f:
    replacement_map = json.load(f)

output_filename = replaceFields('aa.csv','bb.csv', replacement_map)
print(f'Modified CSV file saved as: {output_filename}')