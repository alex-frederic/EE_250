# Lab 8

## Team Members
- Alex Frederic (GitHub: alex-frederic, arfreder@usc.edu)

## Lab Question Answers

Answer to Question 1:

Green: Penny (Mean of about 2.45 g is closest to the 2.500 g weight of the penny)
Blue: Nickel (Mean of about 4.95 g is closest to the 5.000 g weight of the nickel)
Orange: Dollar (Mean of about 8.05 g is closest to the 8.1 g weight of the dollar coin)

Though each denomination may be specified to be a specific weight, uncontrollable random defects in
manufacturing may cause coins of the same denomination to vary slightly in weight according to
a Gaussian distribution. In other words, random noise followig a Gaussian distribution may be
unavoidably introduced into the intended weights to muddle the expected weights.

I would use the weight sensor of the vending machine to check the weight of each coin and then use
the above distributions to see if that measured weight was within 2 standard deviations of the
expected weights of each coin. If a given measured weight was within 2 standard deviations (which
should contain ~95% of the expected data for a coin and shouldn't overlap with each other) of the 
expected value of a specific coin, identify the inserted coin as that coin.


Answer to Question 2:

The light sensor in the GrovePi kit would be used for that.


Answer to Question 3:

Dataset A is linearly separable because the blue and yellow points leave enough space for a
diagonal line cleanly separating the two classes.
Dataset B is not linearly separable because there is no way to draw a line that separates the
pair of points near (6, 13) and the pair of points near (12, 10) while also separating the rest of
the points. In others words, the blue and yellow points encroach too much upon each other's
territory at those two points.
Dataset C is linearly separable because a vertical line at about x1 = 6.75 would cleanly separate
the two classes.
Dataset D is not linearly separable because the points at (3, 7.5) and (5, 5) encroach too much
upon the other class's territory for them to be cleanly separated with a line while also separating
the rest of the data points.
Dataset E is not linearly separable because the two clusters for each class intersects with both
the x range and the y range of at least one of the clusters from the other class. Therefore, with
the clusters within a class so far apart from one another, it is impossible for a single line to
cleanly separate the data of one cluster from the other class while also including the other
cluster from that class on the same side.
Dataset F is not linearly separable because the blue data points surround the yellow ones on all
sides, so a single line cannot separate two classes entirely.


Answer to Question 4:

(x - h)^2/a^2 + (y - k)^2/b^2 = r^2 would be good for dataset F since an elipse could be fitted to
cleanly encapsulate all of the yellow points while excluding all of the blue points on the outside.
(x - h)(y - k) = 0 would be good for dataset E since a hyperbola could be fitted so that the yellow
datapoints fall within its two lobes while the blue points fall within the region between them.
(y - k)^2 = 4a(x - h) would be good for dataset D since the slight curve provided by the sideways
parabola may help to separate the points near the border of the blue and yellow territory.
Dataset B would likely require a high-degree polynomial function (i.e. fourth or fifth) to
separate the points in the middle because they encroach upon the other class's territory so much.


Answer to Question 5:

net = 2*(1) + 1*(-2) + 2*(3) + -2 = 4
sigmoid(net) = sigmoid(4) = 1 / (1 + exp(-4)) ~= 0.95 (from graph)