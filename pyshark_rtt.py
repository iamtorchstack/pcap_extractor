#very important code
# Need to add total tcp counter
import pyshark

capture = pyshark.FileCapture('C:/testdata/inethi_wan_2019-03-13_05-40-00.pcap')

tcp_counter = 0

for packet in capture:
	try:
		print("Protocol: "+ packet.highest_layer +"source:"+ packet.ip.src +" Destination:"+ packet.ip.dst  +" RTT:"+ packet.tcp.analysis_ack_rtt + "Capture Time:"+ str(packet.sniff_time))
		
	except AttributeError as e:
		pass
