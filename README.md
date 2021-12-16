# wuzzuf-web-scraper

A console application where you can enter a job title (for example: "python", "software engineer", ... etc.), and get a .csv file containing the collected data about this job title. This data is collected from scraping [wuzzuf.net](https://wuzzuf.net/jobs/egypt).  


## Console output
The following screenshot is the console output obtained while searching for ***python*** jobs ...

<img width="412" alt="result" src="https://user-images.githubusercontent.com/35142459/146295780-41d91ef9-041f-46e0-a479-dbd248073f82.PNG">

*Note:*
*The program need optimization; It took **6~7 minutes** to obtain **214 job results only**.*


## What I learnt

* Extracting specific data from a multiple pages website (a.k.a. Web Scraping)
* Directory/File manipulation using code (Add, Move, Delete, and Open)
* Saving data from code into .csv files
* Applying one of the S.O.L.I.D. principles, i.e. (the "S" part) --> (Single Responsibility Principle)


## Used libraries

* [**requests** library](https://pypi.org/project/requests/): used to get page content from a given URL
* [**bs4** library](https://pypi.org/project/bs4/): used to parse markup content using 'lxml' parser
* **csv** library: used to manipulate .csv files
* [**datetime** library](https://pypi.org/project/DateTime/): used to obtain current date and time
* **time** library: used to cause some delay while checking user's input
* **os** library: used to manipulate directories
* **math** library: used to round up (ceil) the estimated number of pages

