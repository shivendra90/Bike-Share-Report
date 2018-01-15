# Out first DictReader script. While soft warap is enabled, this python file will remain softwrapped.

with open('Chicago-Divy-2016.csv', 'r') as trip_file:
      csv_reader = csv.DictReader(trip_file)

      for line in csv_reader:
          print(line)
