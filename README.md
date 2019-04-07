# README.md

# Name: Sean Walker

# NetID: skw34

# CPSC 310, Spring 2019

# Homework 3

## A

### 1.

See `Bass Library.pdf` and `Law Library.pdf` for decision tree graphs.

I expect Bass to have a high amount of visitors but comparatively low number of
book returns, seeing as it's a popular library for studying but not many
students actually check out books from Bass (at least in my experience).

I expect the Law Library, comparatively, to be less popular in terms of traffic
but probably have relatively more book returns, since law students actually read
books from the law library.

The Bass tree for Saturday with 2400 visitors first checks a threshold value of visitors: no days with traffic <= 2074.5 are high-return. Since we have mroe visitors (after a check of one outlier high-return day with between 2074.5 and 2075.5 traffic), we continue to the right since we're in the latter part of the week. we continue down all the way, in fact, as traffic is in the highest possible category the tree provides.

I feel like this decision making process might not be very intuitive, as there doesn't seem to be much correlation between traffic being higher and being a high-return day. However, that same lack of correlation is reflective of the data: bass only had 3 high return days overall. If anything, it seems like the tree learned any possible trace of a trend it could, but very few days would end up being high return at Bass.

For the Law Library, we have 96 high return and 54 low return days, so the tree is a lot more complex, as there are more relationships to be found between the variables. For our example, 450 people on a Thursday, we right away are >= 449.5 visitors and so are in a side of the tree with primarily high return days, just based off of traffic. Since it's a thursday, and less than 462.5 traffic, we end up being high-return, although if it was early in the week (sunday or monday) it would've been low-return!

This decision tree is more in-depth but its logic seems to make sense: higher traffic means higher likelihood of being a high-return day, unless you're not _that_ high of traffic and early in the week, which makes sense (fewer visitors and early in the week you'd expect fewer people to come in anyway).

## B

### 1.

Student with id 4237867568296644 likely has a regular Yale Health appointment on Sunday at 8:00.

My algorithm for this problem was to go through every visit to the target building (in this case, Yale Health).
Assuming appointments start at the top of the hour or thirty minutes past the hour (e.g. 12:00, 12:30, 1:00, ...),
Thus, I round the student's swipe time to the nearest 30 minute interval and then keep a record of that student
visiting at that rounded time on that day of the week in a counter.
After going through all the data, any non-appointment swipes will all be maybe 1 or 2 at most--if a student doesn't
have an appointment, there's a very low probability they end up going to Yale Health within a thirty minute window
on the same day more than a few times. In contrast, the most common repeats in the counter end up being much more than
that, meaning there's a strong likelihood a student as an appointment at that time.

### 2.

Student with id 7960088203188404 has the same sleeping schedule as student with id 3398615277913271.
'49', '49', '49', '49', '49', '17', '49'
Sat - Thu Pauli Murray
Fri Davenport

My approach to this problem was to predict a student's sleeping college by simply tallying their most common college per day.
I figure this is an appropriate prediction mechanism because we're only really using one feature per student (day of the week),
so there's no need to use a more complex classifier here, especially because there's also unlikely to be much variance:
students will usually sleep in the same college the same night (usually, one would guess, their own college, for most students).

### 3.

Dear 7143237956228680,
You are only using 6 of your allotted meals per week.

Sincerely,
Yale Dining

For this problem, I first identify all mealplan holders to keep count of all their meal swipes (this is necessary in case someone, for instance, didn't use any meal swipes at all: we'd still want that to be included in the count at the end, but
we wouldn't be able to count that if we didn't identify all mealplan holders first and instead just went through swipe data).

Next, I tallied every swipe by a mealplan holder and the number of weeks in the data set (since the problem specified to
find students "who on average don’t use half their allotted meals a week"), and calculated their average meal swipe utilization
(based on 14 swipes per week \* the number of weeks in the data set), creating a list of students whose utilization was 50% or below.

### 4.

Potential friends for 2969414704160674:
5445587517301194
0519473554825813
9620910935101259
7217437406216078
1748738874555983

For this problem, my biggest challenge was figuring out how to structure the feature vector for samples. Initially, I was
confused as we need to make each "data point" (or "neighbor") correspond to a single student, but each student has 150
samples of their dining data to go by--clearly, there needed to be a reduction of the student's 150 days of swipes into
one single set of features per student. I ended up settling on 15 features: one, their average dinner time, and then one
counting their number of dinner swipes at each of the 14 dining halls. Once I got past that hurdle, implementing it was
fairly straightforward: I take the last swipe at a dining hall per day, as long as it's between 5 and 8pm, and tally the
dining hall they swiped at and add the time to a list which I average at the end. Afterwards, it's only a matter of passing
it into the unsupervised nearest neighbors to get the five nearest students.
