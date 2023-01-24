# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


from openpyxl import Workbook, load_workbook

import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

wb = load_workbook('Beetroot_Final_project.xlsx')
# Завантажуємо дані у сторінку вихідних даних
ws = wb['Расчеты по Коршунову']

# for r in dataframe_to_rows(df, index=False, header=False):
#     ws1.append(r)

for cell in ws['C31:C35']:
    for value in np.linspace(0.2,0.5,num = 6):
        ws.append(value)


#from documentation openpyxl
 # https: // openpyxl.readthedocs.io / en / stable / _modules / openpyxl / worksheet / worksheet.html
# Worksheet.insert_rows

#row_idx = self._current_row + 1
def insert_rows(self, idx, amount=1):
            """
            Insert row or rows before row==idx
            """
    #self._move_cells(min_row=idx, offset=amount, row_or_col="row")
    #self._current_row = self.max_row


#ws['C31'] = 0.2
#ws['C32'] = 0.1
#ws['C33'] = 0.2
#ws['C34'] = 0.15
#ws['C35'] = 0.2


#new_entry = wb['Свод_таблица']['H26':'X26']
#ws.append(new_entry)
wb.save('Beetroot_Final_project1.xlsx')