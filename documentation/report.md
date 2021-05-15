# Report
For my assignment of SuperPy I chose to write multiple files with specific functions. This way I want to keep the code organized and simpler for error handling and debugging. Personally, I am not in favor of one and the same and long files of code. In addition, functions must be easier to reuse when they are on a smaller scale.

<b>Advantages</b>:
+ Easier to navigate instead of scrolling through one huge file
+ Changing one function or variable wouldn't mess up your main file
+ Errors are defined with a specific location
+ Making recompile works only on files related to the change
+ Errors will indicate in what file the problem is (easier to find)
+ The program needs much less capacity (less requirement to hardware)

### Pandas
In addition to the existing assignments, I have chosen to export my CSV files through Pandas. I found it challenging to get started with Pandas and after reading some documentation this application turned out to be quite simple. Pandas has a variety of utilities to perform input/output operations in a seamless manner. It can read data from a variety of formats such as CSV, TSV, MS Excel. I find this a real advantage for future programs. I have noticed through experience that you must be able to work with multiple data files. Pandas seems to be able to remedy that question in a broad perspective.

### JSON
I also use the module 'json' for simultaneously exporting JSON files. In my current work I make extensive use of JSON files, which made me want to explore these two additional functionalities. The JSON structure is straightforward and readable. You have an easier time mapping to domain objects, no matter what programming language you're working with. It's a data format that I need to know.
