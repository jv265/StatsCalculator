# Statistics Calculator

[![Build_Status](https://travis-ci.com/jv265/StatsCalculator.svg?branch=master)](https://travis-ci.com/jv265/StatsCalculator)

<h1>Project Plan</h1>
<h2>Outline</h2>
Statistics Object <br>
<pre>
<b>Methods</b>

    Mean → Calls mean static method from Mean class
    Median → Calls median static method from Median class
    Mode → Calls mode static method from Mode class
    Standard Deviation → Calls standard deviation method from StandardDeviation class
    Variance → Calls variance method from Variance class
    Z-Score → Calls z-score method from ZScore class
</pre>
Static Classes
<pre>
1. Mean
    Methods
        Sum a list of numbers and divide by length of that list
2. Median
    Methods
        Find the middle element in a list of numbers, or the mean of the two middle elements if the length of a list is event
3. Mode
    Methods
        Find the number that appears most in a list of numbers
4. Variance
    Methods
        Finds the difference between the mean of a list and an element with the list, squared
5. Standard Deviation
    Methods
        Finds the square root of a the variance of some given data
6. Z-Score
    Methods
        Divide the difference between the data mean and the raw score from the standard deviation
</pre>
<h2>Task List</h2>
<pre>
<b>1. Mean </b>
__________________
<b>Description</b>
Calculates the average from a given sample. <br>
<b>Formula</b>
∑Xi / n <br>
<b>Example</b>
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
(0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9) / 10 = 4.5 <br>
<b>2. Median </b>
__________________
<b>Description</b>
Calculates the middle number in a sorted list. <br>
<b>Formula</b>
Find the middle from a sorted list. If there are odd numbers, the median
is the middle number. Otherwise, the median is the middle 2 numbers divided
by 2.<br>
<b>Example</b>
[ 8, 5, 4, 3, 1, 9, 4]
Sorted
[ 1, 3, 4, 4, 5, 8, 9]
Result:  4 <br>
<b>3. Mode </b>
__________________
<b>Description </b>
Calculates the number that is repeated often. <br>
<b>Formula </b>
Iterate through the list and find the number that repeats the most. 
If there are more than one, exit. <br>
<b>Example: </b>
[9, 0, 1, 3, 8, 2, 4, 2, 5]
Result: 2 <br>
<b>4. Standard Deviation </b>
__________________
<b>Description</b>
Measures the variation within a set of values. <br>
<b>Formula</b>
√(∑(x - u)^2 / n); Where u stands for our mean; The square root of the variance.<br>
<b>Example</b>
[0, 2, 4, 6]
Step 1. Find Mean
(0 + 2 + 4 + 6) / 4 = 3
Step 2. Find squared distance from each data point to the mean
0, (0 - 3)^2; 2, (2 - 3)^2; 4, (4 - 3)^2; 6, (6 - 3)^2
= 9; 1; 1; 9
Step 3. Add values from step 2, divide by N and  square root
√(∑(9 + 1 + 1 + 9) / 4) = 2.2<br>
<b>5. Variance</b>
__________________
<b>Description</b>
Measures the spread between numbers in a data set. <br>
<b>Formula</b>
(∑(x - u)^2 / n); Where u stands for our mean <br>
<b>Example</b>
[0, 2, 4, 6]
Step 1. Find Mean
(0 + 2 + 4 + 6) / 4 = 3
Step 2. Find squared distance from each data point to the mean
0, (0 - 3)^2; 2, (2 - 3)^2; 4, (4 - 3)^2; 6, (6 - 3)^2
= 9; 1; 1; 9
Step 3. Add values from step 2 and divide by N 
(9 + 1 + 1 + 9) / 4) = 5 <br>
<b>6. Z-Score</b>
__________________
<b>Description</b>
Also known as a standard score, it tells us how far from the mean a data point is. <br>
<b>Formula</b>
(x - u) / o; Where u stands for mean, x stands for our raw score  and o our standard deviation <br>
<b>Example</b>
[0, 2, 4, 6], raw score 10
Step 1. Find Mean
(0 + 2 + 4 + 6) / 4 = 3
Step 2. Find our Standard Deviation
= 2.2
Step 3. Subtract raw score from mean and divide by standard deviation
(10 - 3) / 2.2 = 3.18

</pre>
