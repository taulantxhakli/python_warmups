import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy
import csv

x = []
y = []
fig = plt.figure(figsize=(13,5))

with open('weather data.csv', 'r') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=',')
    firstRow = next(csvReader)
    secondRow = next(csvReader)
    thirdRow = next(csvReader)
    fourthRow = next(csvReader)
    fifthRow = next(csvReader)
    sixthRow = next(csvReader)
    seventhRow = next(csvReader)
    eighthRow = next(csvReader)

x_labels = [int(i) for i in firstRow[1:]]
y_newyork = [int(i) for i in secondRow[1:]]
y_battlecreek = [int(i) for i in thirdRow[1:]]
y_houghton = [int(i) for i in fourthRow[1:]]
y_chicago = [int(i) for i in fifthRow[1:]]
y_dallas = [int(i) for i in sixthRow[1:]]
y_sanfransisco = [int(i) for i in seventhRow[1:]]
y_columbus = [int(i) for i in eighthRow[1:]]


plt.plot(y_newyork, color='green')
plt.plot(y_battlecreek, color='red')
plt.plot(y_houghton, color='cyan')
plt.plot(y_chicago, color='orange')
plt.plot(y_dallas, color='blue')
plt.plot(y_sanfransisco, color='black')
plt.plot(y_columbus, color='yellow')

plt.title('Weather Data | January 1st Temperatures')
plt.xlabel('Years')
plt.ylabel('Termperature')
plt.xticks(numpy.arange(len(x_labels)), x_labels, rotation=0)

green_patch = mpatches.Patch(color='green', label='New York')
red_patch = mpatches.Patch(color='red', label='Battle Creek')
cyan_patch = mpatches.Patch(color='cyan', label='Houghton')
orange_patch = mpatches.Patch(color='orange', label='Chicago')
blue_patch = mpatches.Patch(color='blue', label='Dallas')
black_patch = mpatches.Patch(color='black', label='San Fransisco')
yellow_patch = mpatches.Patch(color='yellow', label='Columbus')
plt.legend(handles=[green_patch, red_patch, cyan_patch,orange_patch,
                    blue_patch, black_patch, yellow_patch])

plt.grid()
plt.show()
