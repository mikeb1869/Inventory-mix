# Inventory-mix
CarMax is the largest used car retailer in the US. They operate approximately 200 locations nationwide and have approximately 30,000 cars in inventory available to Customers at any given time. My python program is intended for use by CarMax employees and managers for the purpose of manipulating and tracking the inventory available at their respective location. The program can perform the following functions:

•	Read in a large dataset from a .txt file
•	Traverse the dataset and extract information from it
•	Process input from the user
•	Calculate the average listing price of vehicles in inventory
•	Calculate the number of vehicles in each inventory segment
•	Compare the number to vehicles in each segment to pre-determined targets.
•	Display output to the user

The program, while very simple, can be very powerful when used as a tool by management to glean information needed to make sound business decisions.  As a Purchasing Manager for CarMax, my job is to make sure that my specific territory maintains the proper mix of vehicle types. For example, in my assigned territory (the Las Vegas market), there are roughly 1000 vehicles in inventory at any given time. It would not make sense if all 1000 of those vehicles were convertibles. While we do have many customers looking for convertibles, we also have many shopping for vans, trucks, sedans, etc. In order to best meet customer needs, we establish targets for each inventory segment. Knowing how current inventory compares to optimal targets is critical for me to do my job effectively. For example, if after analyzing the inventory I discover that we are severely under inventoried in SUVs, I know that I need to implement a plan to source more SUVs to keep up with customer demand. In addition, it is useful to know the mean list prices of each segment of inventory. Knowing average prices will help me determine if I need to source lower or higher priced inventory. My Python program would help automate the process of tracking each mix category and comparing the results to pre-determined targets.

The project has two main aspects:

1.	It displays an interactive menu to the user for the purpose of running analytics from the .txt document (current inventory levels & average list price)
2.	A second program prompts the user to enter the current inventory levels returned by the first program, then compares those entries to Company targets, and finally displays results to the user.

To demonstrate the capabilities of my program, I have created a .txt document to simulate an inventory list similar to one used by CarMax employees. In a real-world application, this list would be a true representation of actual vehicle inventory. However, for the sake of simplicity as well as the eliminating the risk of using proprietary Company information, I have opted for this “fake” list. I created this list with a simple Python which makes use of the random() method and a for loop. While this small program has nothing to do with the functionality of my main 2 programs, I have included it for your reference along with the .txt document used to test my program. 

