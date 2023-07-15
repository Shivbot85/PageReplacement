Page Replacement Algorithms:
This is a Python implementation of three different page replacement algorithms: FIFO, LRU, and OPT.

Algorithms:
FIFO
This algorithm replaces the oldest page in memory with the new page. It stores the pages in a queue and removes the oldest page (i.e., the page at the front of the queue) when a page fault occurs.

LRU
This algorithm replaces the least recently used page in memory with the new page. It keeps track of the order in which pages are accessed and removes the page that has not been accessed for the longest time when a page fault occurs.

OPT
This algorithm replaces the page that will not be used for the longest time in the future. It looks ahead to find the page that will not be used for the longest time and replaces it with the new page. 

Usage:
To use this code, simply run the following command in your terminal:
python3 paging.py [number of page frames]
Here, [number of page frames] is the number of frames in the memory.

To use preferably- 
Open on vscode and open the project after you have downloaded my submission. Then on the terminal run the the prompt python3 paging.py [number of page frames]


If all else fails the issue could be that it is the wrong version of python so use python instead of python3

