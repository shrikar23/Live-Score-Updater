# Live-Score-Updater
A very basic python code that provides live cricket updates on the Desktop.

Overview:

The website from where the data is to be crawled will be provided to the program. 
The program will retreive the data from the provided website. The retrieved data will be in the XML format. 
This data is passed through a data package which converts the data into a easily traversable tree. The tree can be traversed based on the XML tags.
Once converted, the required information is extracted from the data and displayed on the desktop.
This operation is performed continuously. The data is retrieved from the website every 10 seconds, so the scoreboard is auto updated every 10 seconds.
