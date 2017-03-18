import csv
import os
import datetime
from os import listdir
from os.path import isfile, join

files_in = ['D:\\Backups\\ISMMarch2017\\PycharmProjects\\AdHoc\\Exclusions\\01142017test.txt']
file_out = 'D:\Backups\\ISMMarch2017\\PycharmProjects\\AdHoc\\Exclusions\\all.csv'
mypath = 'D:\\Backups\\ISMMarch2017\\PycharmProjects\\AdHoc\\Exclusions\\'


def get_all_files(dir):
    files_in = []
    for file in os.listdir(mypath):
        if file.endswith(".txt"):
            files_in.append(os.path.join(mypath, file))
    return files_in


def summarize_data(files_in, file_out):
    with open(file_out, 'w') as f_out:
        out_colnames = ['Date', 'Time_Interval', 'Avg_Speed_Ans', 'Avg_Aban_Time', 'ACD_Calls', 'Avg_Talk_Time', 'Avg_After_Call',
        'Aban_Calls', 'Max_Delay', 'F_in', 'F_out', 'Extn_Out_Calls', 'De_Ave_Talk_Time', 'De_Calls', 
        'Avg_Queue_Time', '%ACD', '%Ans', 'Avg_Pos_Stf', 'Calls_per_Pos']
        
        file_writer = csv.DictWriter(f_out, fieldnames=out_colnames)
        file_writer.writeheader()
        
        for f in files_in:
            with open(f, 'r') as f_in:
                file_reader = csv.DictReader(f_in, delimiter='\t')
                date = next(file_reader)
                #print((date))
                for key, value in date.items():
                    if value and len(value) > 15:
                        date_key = key


                for i in range(2):
                    l = next(file_reader)
                
                for row in file_reader:
                    new_point = {}
                    new_point['Date'] = date_key
                    start_time = datetime.datetime.strptime(date_key + ' ' + row[date_key], '%m/%d/%Y %H:%M')
                    end_time = start_time + datetime.timedelta(minutes=15)
                    new_point['Time_Interval'] = str(start_time.time())+ \
                                                 '-' + str(end_time.time())
                    #print(row)
                    if None in row:
                        new_point['Avg_Speed_Ans'] = row[None][0]
                        new_point['Avg_Aban_Time'] = row[None][1]
                        new_point['ACD_Calls'] = row[None][2]
                        new_point['Aban_Calls'] = row[None][3]
                        new_point['Max_Delay'] = row[None][4]
                        new_point['F_in'] = row[None][5]
                        new_point['F_out'] = row[None][6]
                        new_point['Extn_Out_Calls'] = row[None][7]
                        new_point['De_Ave_Talk_Time'] = row[None][8]
                        new_point['De_Calls'] = row[None][9]
                        new_point['Avg_Queue_Time'] = row[None][10]
                        new_point['%ACD'] = row[None][11]
                        new_point['%Ans'] = row[None][12]
                        new_point['Avg_Pos_Stf'] = row[None][13]
                        new_point['Calls_per_Pos'] = row[None][14]

                    file_writer.writerow(new_point)


files_in = get_all_files(mypath)
print(files_in)
all = summarize_data(files_in, file_out)
