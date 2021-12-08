# Calculates air quality using BSEC
# Outputs air quality in a .csv file

from datetime import datetime
from bme68x import BME68X
import bme68xConstants as cnst
import bsecConstants as bsec
from csv import writer
from time import sleep

def writeCSV(data):

    row = [
    datetime.now().strftime("%H:%M:%S"),
    data["iaq"],
    data["iaq_accuracy"],
    data["temperature"],
    data["raw_temperature"],
    data["raw_pressure"],
    data["humidity"],
    data["co2_equivalent"], 
    data["co2_accuracy"], 
    data["breath_voc_equivalent"], 
    data["breath_voc_accuracy"]]
              
    
    with open('../Outputs/BMEoutput.csv', 'a+', encoding='UTF8', newline='') as writecsv:
        writer(writecsv).writerow(row)



# MAIN
bme = BME68X(cnst.BME68X_I2C_ADDR_LOW, bsec.BSEC_ENABLE)
print("*********************************************************")

header = ["Timestamp", "IAQ", "IAQ Accuracy", "Temperature", "Raw Temperature", "Raw Pressure", "Humidity", "CO2 Equivalent", "CO2 Accuracy", "Breath VOC Concentration", "Breath VOC Accuracy"]

with open('../Outputs/BMEoutput.csv', 'a+', encoding='UTF8', newline='') as writecsv:
        writer(writecsv).writerow(header)

while(True):
    data = bme.get_bsec_data()
    writeCSV(data)
    print("BME688 RECORDING AIR QUALITY - " + datetime.now().strftime("%H:%M:%S"))
    print("********************************\n")
    sleep(3)
