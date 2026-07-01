import xlrd

def extract_bold_strings(filename):
 strings = []
 workbook = xlrd.open_workbook(filename)
 sheet = workbook.sheet_by_index(0)
 for row in range(sheet.nrows):
  for col in range(sheet.ncols):
   cell_value = sheet.cell(row, col).value
   font_style = sheet.cell_xf_index(row, col).font_record.weight
   if font_style == 700:
    strings.append(cell_value)
 return strings
 
 strings = extract_bold_strings('test.xlsx') 
 print(strings) # prints ['STRING1', 'STRING2']