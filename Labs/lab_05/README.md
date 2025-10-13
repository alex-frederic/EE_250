# Lab 5

## Team Members
- Alex Frederic (Github: alex-frederic, arfreder@usc.edu)

## Lab Question Answers

PART 1
Answer for Question 1: 

dBm is a measure of power given by 10*log_10( P [mW] ). Generally, higher values are better
for WiFi strength because it means that the received power is greater, allowing for more
reliable distinguishing of different data symbols and an overall higher data rate.


Answer for Question 2:

Not only do the different OS's have different commands for getting the IP addresses, but they
also have different numbers of arguments and differently structured outputs. Thus, different
post-processing needs to be done on each of the outputs to extract the necessary data (received
power in dBm).
Linux: iwconfig wlan0
Windows: netsh wlan show interfaces
Darwin: wdutil info


Answer for Question 3:

subprocess.check_output runs the given command in the OS and returns its stanbdard output as a
string. It also checks its return code and raises an error if it's non-zero to inform the program
whether or not the command was successful.


Answer for Question 4:

It scans through a given string looking for a given pattern expressed in regex. If it finds a
match, it returns a Match object to represent that match, allowing further analysis to be
performed on it and information to be extracted from it.


Answer for Question 5:

The wlanSignalQuality attribute in Windows represents signal quality as a percentage with 0%
representing -100 dBm and 100% representing -50 dBm. Therefore, to find the actual physical
quantity in dBm, the following conversion must be performed:
actual_dBm = -100 + windows_signal_quality / 2


Answer for Question 6:

Standard deviation is the square root of the sum of the squares of the deviataions from the mean
of each data point: std_dev = sqrt( sum( (data_value - mean)^2 ) ). It is a measure of how spread
out the data is from the mean. Calculating it can inform us how consistent or how variable a
random quantity is when measured multiple times.


Answer for Question 7:

A dataframe is a datatype from the pandas library that stores lists of data in
labeled columns. If each row corresponds to a specific kind of measurement, rows
can optionally be labeled as well. This is convenient for our purposes because
it integrates directly with plotly for making bar charts, letting us specify the
location column as the labels for each bar, the signal_strength_mean column as
the height of each bar, and the signal_strength_std column as the error bar
distance for each column. Thus, each row conveniently represents all of the data
for one bar in such a way that I don't have to do any more processing of the
dataframe myself; plotly handles it.


Answer for Question 8:

The error bars tell us how much variation from the mean was seen in each of
the measurements. Therefore, we can determine how much random noise was present
in each of the measurements. This tells us how reliably we can expect the signal
strength to behave near the mean on subsequent measurements, giving a sense of
the reliability of the connection to the router. Alternatively, it can also tell
you how precisely the measurement apparatus was able to measure the actual value
of the received dBm.


Answer for Question 9:

Generally, it decreased as I moved further from the router (which was located
in the living room). Additionally, if there were obstructions in the way (walls,
doors, etc.) the signal tended to be a little worse, but this was not as strong
a factor as distance. For instance, the living room and outdoors measurements
were very near each other, only the door was closed on the outdoors measurement,
separating the router and laptop physically. From the graph, this only produced
a tiny drop in signal strength. The bathroom was the furthest away and separated
by multiple walls and a door, so of course it had the lowest signal strength.
The closet was similarly far away, but with not as many obstructions and a more
direct path to the router in the living room, accounting for it being the second
worst after the bathroom. Overall, signal strength can vary greatly across a
single appartment based on locaition, but in my case, it's never quite enough
that I can't still get a decently strong signal from the router.


PART 2
Answer for Question 1:

In my data, average TCP throughput varied wildly across distances with no clear
pattern as distance increases. We should expect it to decrease with distance,
but I suppose that my router was operating too reliably across all measured
distances to be able to detect it. I also experienced far lower throughput from
TCP than expected. It's possible that the TCP tests were for some reason
configured to optimize for distance over all runs instead of throghput. UDP
remained even more consistent for all distances. That is what you would expect
up to a certain point until the router moved too far away for UDP to reliably
deliver packets, at which point throughput was drop significantly. I suppose I
never reached the threshhold at which UDP would fail significantly at any of my
tests from 2m to 18m. My router must have been too strong.


Answer for Question 2:

UDP never incurred any significant package loss for me. It did jump
significantly to 0.0224 at 14m from 0.0094 at 8m and again to 0.0502 at 18m.
However, those percentages are still negligibly low. I don't think that any of
my tests were far enough away for UDP to fail significantly.


Answer for Question 3:

The reason UDP experiences more package loss than TCP is because it is
connectionless, while TCP establishes a handshake between sender and receiver
to ensure reliable, in-order delivery. Thus, UDP's fire-and-forget method has no
guarantee of delivery, and the sender won't even know if a package made it or
not. However, TCP can re-send lost packages when no ACK message returns from the
receiver.


Answer for Question 4:

Increasing the UDP bandwidth would decrease the distance at which significant
package loss occurs. Higher bandwidth requires a higher received power to be
able to successfully and reliably decode received symbols. Thus, the distance at
which that is possible will decrease since received power decreases with
distance. In short, more packages would arrive garbled and unreadable at shorter
distances, causing more packages to be lost at shorter distances.


Answer for Question 5:

It would not be significantly different unless interference with other devices'
signals were occuring at one frequency but not the other. Generally, the
frequency has no impact on the symbol rate and, therfore, the data rate.
However, if one of the frequencies experienced external interference, TCP
throughput would be decreased by requiring more retransmissions, and UDP package
loss would increase at lower distances since collisions would caues more
packages to become unreadable. For instance, if operating in the presence of
many embedded devices using the 802.15.4 2.4GHz standard, a frequency of 5 GHz
would provide the better transmission by reducing collisions.