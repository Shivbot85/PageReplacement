from random import seed
from random import randint
import sys

# Function to implement the FIFO page replacement algorithm
def FIFO(size, pages):
    page_list = list(pages)  # split the string of pages into a list of individual pages
    mem = []  # list to hold frames
    queue = []  # queue to track page reference order
    i = 0  # counter to keep track of frame usage
    npfault = 0  # counter for the number of page faults

    for page in page_list:
        # If frames are not full
        if i < size:
            # If the page is not in memory, add it
            if page not in mem:
                mem.append(page)
                queue.append(page)
                i += 1
                npfault += 1
        else:
            # If the page is not in memory, replace the page that has been in memory for the longest time (FIFO)
            if page not in mem:
                q = queue.pop(0)
                queue.append(page)
                j = mem.index(q)
                mem[j] = page
                npfault += 1

    return npfault

# Function to implement the LRU page replacement algorithm
def LRU(size, pages):
    page_list = list(pages)  # split the string of pages into a list of individual pages
    mem = []  # list to hold frames
    usage = []  # list to track page reference order
    i = 0  # counter to keep track of frame usage
    npfault = 0  # counter for the number of page faults

    for page in page_list:
        if i < size:
            # If the page has been used before, move it to the front of the list
            if page in usage:
                usage.remove(page)
            usage.insert(0, page)
            # If the page is not in memory, add it
            if page not in mem:
                mem.append(page)
                i += 1
                npfault += 1
        else:
            # If the page has been used before, move it to the front of the list
            if page in usage:
                usage.remove(page)
            usage.insert(0, page)
            # If the page is not in memory, replace the page that has been least recently used (LRU)
            if page not in mem:
                q = usage.pop(-1)
                j = mem.index(q)
                mem[j] = page
                npfault += 1

    return npfault

# Function to implement the OPT page replacement algorithm
def OPT(size, pages):
    page_list = list(pages)
    mem = [] #list of frames
    i = 0 #frame use counter
    n = 0 #page reference index counter
    npfault = 0

    for page in page_list:
        if i<size:
            if page not in mem:
                mem.append(page)
                i+=1
                npfault+=1
            n+=1

        else:
            if page not in mem:
                #create a usage list, with the index of the page in the future references, else 100000000
                usage = [page_list[n::].index(m) if m in page_list[n:] else 100000000 for m in mem]
                u = usage.index(max(usage)) #get the index of the maximum element in the usage list (page not reference in future or furthest ref)
                mem[u] = page
                npfault+=1
            n+=1

    return npfault


def main():
    pages = ""
    N = int(input('Enter N - the number of pages to generate.\n'))
    if(N < 1): #Validation Check
        print ('Error. N < 1')
        exit()
    for _ in range(N): #Generate Page References
        pages += str(randint(0, 9))

    size = int(sys.argv[1])
    if(size > 7 or size < 1): #Validation
        print ('Error. number of pages parameter not in range [1,7]')
        exit()
    print ('Generated Page Reference String:', ' '.join(pages))
    print ('FIFO', FIFO(size,pages), 'page faults.')
    print ('LRU', LRU(size,pages), 'page faults.')
    print ('OPT', OPT(size,pages), 'page faults.')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print ('Usage: python paging.py [number of page frames]')
    else:
        main()
