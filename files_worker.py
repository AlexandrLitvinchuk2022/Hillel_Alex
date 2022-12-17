import csv

with open('schedules.csv', 'w', newline ='') as fn:
    writer_obj = csv.writer(fn)
    writer_obj.writerow(["departure point", "departure time", "destination point", "arrival time", "cost ticket"])

with open('schedules.csv', 'a', newline ='') as fn:
    writer_obj = csv.writer(fn)
    writer_obj.writerows([
        ["Odessa", "01.03.2022","Frankfurt", "15.03.2022", "250 dollars"],
        ["Kiev", "12.03.2022","Berlin", "14.03.2022", "150 dollars"],
        ["Milan", "17.03.2022", "Berlin", "17.03.2022", "180 dollars"],
    ])

with open('schedules.csv', "r") as fn:
    reader_obj = csv.reader(fn)

    for row in reader_obj:
        print(f"{type(row)=}, {row=}")
 #####################################################
with open('schedules.csv', "w", newline='') as fn:
    fieldnames = ['departure point', 'departure time', "destination point", "arrival time", 'cost ticket']
    writer = csv.DictWriter(fn, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'departure point': 'Odessa', 'departure time': '01.03.2022', 'destination point': 'Frankfurt', 'arrival time': '15.03.2022', 'cost ticket': '250 dollars'})
    writer.writerow({'departure point': 'Kiev', 'departure time': '12.03.2022', 'destination point': 'Berlin','arrival time': '14.03.2022', 'cost ticket': '150 dollars'})
    writer.writerow({'departure point': 'Milan', 'departure time': '17.03.2022', 'destination point': 'Berlin','arrival time': '17.03.2022', 'cost ticket': '180 dollars'})
# ############################################

with open('schedules.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(
            f"{row=}, {type(row)=}"
        )