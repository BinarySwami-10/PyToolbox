Team Information:

1)Shivam Jha: 18/11/EC/037
2)Nikhil Swami: 18/11/EC/034
3)Deepanshu Jain: 18/11/EC/0

Details to run the code:

"newsjsoncode.py" is the main file
	it gets all data in systematic order and processeses it to json called "newspost.json"

"jsonXloader.py" is the code for processing the raw data
	it removes junk from the processed data and creates noise free data for better NLP applications.
	it can be modified according to your needs.
	its plug and play.
For twitter code method to use the code is already in the file in the form of comments

Detail to interpret the data:
	
+ first load newspost.json into dictionary
+ suppose dictionary name is "dicto" dicto["Posts"][i][j] is the format
+ i is the post number && j is the index of post
 	j=0 title
	j=1 date/time
	j=2 link of post url
	j=3 post content paragraph

Results of Sentiment Analysis:

+ All the results of the VADER sentiment analysis is stored in the"Group_7/Data/SENTIMENT ANALYSIS" folder.

Memberwise Contribution Report:

Shivam Jha:

percentage contribution:45%

+ basic code structure.
+ scraping modules. 
+ code for display of Title, Date, News Content, Images, etc.
+ bug fixing and debugging.
+ base template.
+ scraping of data
+ final refining of code
+ presentation

Nikhil Swami:

percentage contribution: 45%

+ threading of news scraping (n threads = n times speed )
+ date filter to scrape posts till specific date
+ reordering of json to display Title>Date>link>Newscontent in order.
+ JsonXloader.py which gives access to further process data
+ bug fixing and debugging
+ VADER sentiment analysis
+ Documentation

Deepanshu Jain:

percentage contribution: 10%

+ Json handling and dumping
+ needed optimizations for time and space complexity.