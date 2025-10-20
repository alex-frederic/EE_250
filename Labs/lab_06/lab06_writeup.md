# Team Members:
- Alex Frederic (GitHub: alex-frederic, arfreder@usc.edu)
- Peyton Crawford

Answer to Question 1:

git clone git@github.com:my-name/my-imaginary-repo.git
touch my_second_file.py
echo "print(\"Hello World\")" > my_second_file.py
git add my_second_file.py
git commit -m "Created and edited my_second_file.py"
git push origin main


Answer to Question 2:

For this lab, we mainly pair-programmed on the local environment of the laptop and
then pushed them to GitHub. The changes were then pulled into the RPi, which contained
the cloned git repository. After testing the code on the RPi, we would make changes we
wanted to test in VSCode on the laptop, commit them, and push to GitHub before pulling
them onto the RPi to test them.

Learning a terminal-based text editor would have tremendously helped for quickly
writing and testing code on the RPi without committing in between each change. We
tried nano, but its native tab spacing differed from that of the start file,
which made it cumbersome to program in. Knowing a more customizable terminal
text-editor (or just knowing how to change nano's tab spacing) would have made it a
lot more convenient.

However, the other reason we opted to program exclusively in the laptop environment is
because we didn't have an SSH key set up on the RPi, meaning that we couldn't push to
GitHub from it. Taking the time to set this up would have enabled us to just push
once to GitHub when the program was finished instead of pushing and pulling in between
each change.


Answer to Question 3:

According to the grovepi source code, the ultrasonicRead() first calls the
write_i2c_block() function to write the command code and pin number to the GrovePi.
This function calls time.sleep(0.002 + additional_waiting) a single time upon a
successful write operation. The additional_waiting variable is set to a constant 0
without modifying the grovepi source code, so this is effectively time.sleep(0.002).
Then, to actually read the value from the ultrasonic ranger via the digital pin its
connected to, it calls the read_identified_i2c_block(), which calls the
read_i2c_block() function. Upon a successful read, read_i2c_block() also calls
time.sleep(0.002 + additional_waiting) = time.sleep(0.002) a single time. If
read_i2c_block() returns a valid list of bytes on the first attempt, then
read_identified_i2c_block() only calls it once. Therefore, ultrasonicRead() incurs a
total waiting buffer in between readings of the ultrasonic sensor of 2 ms + 2ms = 4ms.

As indicated by the "i2c" in the above function calls, the RPi uses the I2C protocol to
communicate with the Atmega328P chip on the GrovePi when using the grovepi python
library. According to Wikipedia, this is a serial, half-duplex protocol.
(https://en.wikipedia.org/wiki/I%C2%B2C)
	

Answer to Question 4:

The GrovePi shield contains an ADC that converts analog voltage values measured on its
analog pins into a 10-bit digital value (accounting for the 2^10 = 1,024 different
values). The analog values from 0-5 V are mapped linearly across 0-1,023 digital range
such that 0 V corresponds to a digital 0 value and 5 V corresponds to a 1,023 digital
value. Thus, the digital interpolation can be achived via a linear equation in point-
slope form:

D_val - 0 = ( (1,023 - 0) / (5 V - 0 V) ) * (A_val - 0 V)
D_val = (1,023 / 5 V) * A_val
D_val = (204.6 V^-1) * A_val (truncate to achieve a whole number)

The reason that the RPi on its own cannot perform this conversion is that is has no ADC. Thus,
it cannot convert the analog voltage on a pin to a readable digital value. For each pin, it can
only read a digital 1 or 0 value from the voltage (whether or it's above a certain threshold or
not) and not where it's magnitude lies on a linear scale. However, since it can read digital
values, it can receive the digital representation of an analog signal transmitted to its digital
pins by an external ADC (like the one on the GrovePi shield). Generally, such a circuit is
implemented by either a ladder circuit of resistors or a timer circuit.


Answer for Question 5:

I would first navigate to the the cloned GrovePi git repo. Then, I would run
"python3 example.py" to verify whether or not the LCD screen is connected to the GrovePi
correctly or not to allow the RPi to communicate with it. Potentially, I'd also do this with the
other two exmaple scripts in the folder to ensure all of the functionality of the libary worked
as intended. If the pre-made example scripts don't work with the LCD screen, that means
something is definitely wrong with the wiring, so I would then adjust the wiring to fix the
issue. Assuming I were using only the functions found in the grove_rgb_lcd directory in my
Python script, it couldn't be a problem with the commands after verifying they can reach the LCD
screen, so it must be a problem with the Python script.

If that wasn't the problem, then the problem must be with my Python script since, assuming I
were using only the functions found in the grove_rgb_lcd directory, it couldn't be a problem with
the commands I was using, having just verified them in the previous step. Then, I would create a
new branch with "git checkout -c debugLCD" and add print statements to the area of the code
responsible for writing to the LCD screen to ensure the code even reached the command
responsible for writing to the LCD screen. If that part of the code didn't trigger when it was
supposed to, I would trace through the while loop to see why it doesn't. Potentially, I'd add
other print statements elsewhere in the program to check what lines the program is actually
accessing and what states the variables are in at various points. Where they don't match what I
intended/expected, that must be where the problem lies. Once I'd verified that the control flow
of the program worked as intended with print statements and that that logic interacted with the
GrovePi as expected, I'd add and commit just the changes that fix the issue without the debug
statements. Finally, I'd merge debugLCD back onto main with "git checkout main;
git merge debugLCD", resolve any merge conflicts, and delete the debugLCD branch with
"git checkout -d debugLCD".