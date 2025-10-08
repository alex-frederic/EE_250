import csv
import matplotlib.pyplot as plt

TCP_BASE: str = "iperf_tcp_"
UDP_BASE: str = "iperf_udp_"

distances: list[int] = [2, 6, 10, 14, 18]

tcp_files: list[str] = [TCP_BASE + str(d) + "m.csv" for d in distances]
udp_files: list[str] = [UDP_BASE + str(d) + "m.csv" for d in distances]
print(tcp_files)

tcp_data = []
for trial in tcp_files:
	with open(trial, mode='r') as tcp_file:
		tcp_trial = list(csv.reader(tcp_file))[1]

		tcp_trial_data = []
		for d in tcp_trial:
			tcp_trial_data.append( float(d.strip()) )
		
		tcp_data.append(tcp_trial_data)
for i in tcp_data:
	print(i)
print()

udp_data = []
for trial in udp_files:
	with open(trial, mode='r') as udp_file:
		udp_trial = list(csv.reader(udp_file))[1]

		udp_trial_data = []
		for d in udp_trial:
			udp_trial_data.append( float(d.strip()) )
		
		udp_data.append(udp_trial_data)

for i in udp_data:
	print(i)
print()


plt.plot([1, 2, 3, 4, 5], tcp_data[0][1:6], label="y = x^2", color="blue")
plt.plot([1, 2, 3, 4, 5], udp_data[0][1:6], label="y = x^2", color="blue")
plt.show()