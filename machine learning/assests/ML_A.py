import pandas as pd
from collections import Counter
import xlsxwriter

# read the csv file
file = pd.read_csv("Process.csv")
# get only the process column
processes = file.Process

# creating a temporary list
temp = []
for process in processes:
    # stores each process in the temporary list
    temp.append(process)

new_list = Counter(temp)
# gets the list of occurrence of each process
frequency = []
for freq in new_list:
    frequency.append(new_list[freq])
# gets each process and stores it in a list
p_list = []
for p in new_list:
    p_list.append(p)

total_list = [p_list, frequency]

with xlsxwriter.Workbook('runner.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    worksheet.write("A1", "index")
    worksheet.write("C1", "processes")
    worksheet.write("E1", "frequency")
    for n in range(len(p_list)):
        worksheet.write(f"A{n + 2}", n)
    n = 2
    for data in p_list:
        worksheet.write(f"C{n}", data)
        n += 1
    m = 2
    for data in frequency:
        worksheet.write(f"E{m}", data)
        m += 1
