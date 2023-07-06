1. Discuss the time complexity of your solution. What trades did you make?
- The most time was spent on understanding the data model of the artifacts presented, and really understanding what was asked for in the test.
As for the trade-offs, I preferred to focus on using all the native features of python that I could, making use only of data structure tricks, such as indexing for example; to manipulate the information, and make it available in the form needed.

2. How would you change your solution to account for future requestable columns such as “Bill voted on date” or “Co-sponsors”?
I believe that the algorithm already supports this, because I am considering all the fields of the entities at the time of setting up the data structure for manipulation and calculation of the results... that way, I can access them at any time.
It may be necessary to adjust the indexes if the column order is changed in the csv.

3. How would you change your solution if, instead of receiving CSVs of data, you received a list of legislators or bills for which you should generate a CSV?
- Availability of functionality in an api-rest, or data reading via console.
4. How much time did you spend working on the task?
- 2 hours