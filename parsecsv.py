import csv
import os

files_in = ['D:\\Backups\\ISMMarch2017\\PycharmProjects\\AdHoc\\Exclusions\\test.txt']
file_out = 'D:\Backups\\ISMMarch2017\\PycharmProjects\\AdHoc\\Exclusions\\all.csv'
run_date = '3/17/2017'

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
                print((date))
                for key, value in date.items():
                    if value and len(value) > 15:
                        date_key = key
                    if not value:
                        end_time = key

                for i in range(2):
                    l = next(file_reader)
                
                for row in file_reader:
                    print(row)

                    new_point = {}

                    new_point['Date'] = date_key
                    new_point['Time_Interval'] =row[date_key]+'-'+row[end_time]
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


all = summarize_data(files_in, file_out)
