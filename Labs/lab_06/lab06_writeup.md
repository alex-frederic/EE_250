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

For this lab, we mainly edited the files on the local environment of the laptop and
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

<!-- TODO -->


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

<!-- TODO -->