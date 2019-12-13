import csv
import os

def conv_air(root):

    with open(root + 'AircraftType.csv') as csv_file:
        airfile_spec = csv.reader(csv_file, delimiter = ',')
        root += 'Output\\'

        with open(root + 'AircraftData_c.csv', 'a+') as csvfile:
            newfile = csv.DictWriter(csvfile, fieldnames = ['aircraftID', 'model', 'total_seats_int'])

            for s_row in airfile_spec:
                newfile.writerow({'aircraftID' : s_row[0], 'model' : s_row[2], 'total_seats_int' : 'temp'})

    pass

def conv_dest(root):
    with open(root + 'Destinations.csv') as csv_file:
        destfile = csv.reader(csv_file, delimiter = ',')
        root += 'Output\\'

        with open(root + 'DestinationData_c.csv', 'a+') as csvfile:
            newfile = csv.DictWriter(csvfile, fieldnames = ['dest_name', 'dest_id', 'flight_duration', 'contact_nr'])

            for row in destfile:
                newfile.writerow({'dest_name' : row[1], 'dest_id' : row[0]})

    pass

def conv_emp(root):
    with open(root + 'Crew.csv') as csv_file:
        crewfile = csv.reader(csv_file, delimiter = ',')
        root += 'Output\\'

        with open(root + 'EmployeeData_c.csv', 'a+') as csvfile:
            newfile = csv.DictWriter(csvfile, fieldnames = ["ssn", "name", "address", "phone", "email", "pilot_bool", "planeType"])

            for row in crewfile:
                pilot_bool = 0
                if row[2] == 'Pilot':
                    pilot_bool = "True"
                newfile.writerow({"ssn" : row[0], "name" : row[1], "address" : row[5], "pilot_bool" : pilot_bool, "planeType" : 'temp', "phone" : row[6], "email" : 'temp'})
    pass

def conv_voy(root):
    with open(root + 'PastFlights.csv') as csv_file:
        voyfile_past = csv.reader(csv_file, delimiter = ',')

        with open(root + 'UpcomingFlights.csv') as csv_file:
            voyfile_up = csv.reader(csv_file, delimiter = ',')
            root += 'Output\\'

            with open(root + 'VoyageData_c.csv', 'a+') as csvfile:
                newfile = csv.DictWriter(csvfile, fieldnames = ['voyageID','destination', 'departureTime', 'aircraftID', 'pilots_lst', 'flightAttendants_lst', 'captain', 'seatingSold'])
            
                for row in voyfile_up:
                    newfile.writerow({'voyageID' : row[0],"destination" : row[2], "departureTime" : row[3], "aircraftID" : 'temp', "pilots_lst" : 'temp',\
                        "flightAttendants_lst" : 'temp', "captain" : 'temp', 'seatingSold' : 'temp'})

                for row in voyfile_past:
                    pilots_lst = [row[6], row[7]]
                    newfile.writerow({'voyageID' : row[0],"destination" : row[2], "departureTime" : row[3], "aircraftID" : row[5], "pilots_lst" : pilots_lst,\
                        "flightAttendants_lst" : 'temp', "captain" : row[6], 'seatingSold' : 'temp'})
            
    pass

def main():
    root = os.getcwd() +  '\\' #+ 'Group53\\InputData\\'  

    conv_air(root)
    conv_dest(root)
    conv_emp(root)
    conv_voy(root)
        


main()