import pyshark
import csv

#For documention on csv visit (https://docs.python.org/3.1/library/csv.html)
#tried to implement adding a field name using the DictWriter but failed.
#video on (https://www.youtube.com/watch?v=0Vl0iwkXrQ8) at time 4:22 will help to complete this task using DictWriter
capture = pyshark.FileCapture('C:/testdata/inethi_wan_2019-03-13_05-40-00.pcap')
#fieldnames = ["time","packetsize"]
bandwithWriter = csv.writer(open('bandwidth.csv','a',newline=''))
#bandwithWriter = csv.DictWriter(open('bandwidth.csv','a',newline=''),fieldnames=fieldnames)

for packet in capture:
	bandwithWriter.writerow([str(packet.sniff_time),str(packet.length)])
	print("Time: "+ str(packet.sniff_time) + "Packet Size"+ str(packet.length))