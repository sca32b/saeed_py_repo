
# Recursive walk from source to destination

def srcdest (src,dst):
# base case
    if src == dst:
        print("Source and destination are same")
    else:
# processing    
       print(src)
       src+=1
# recursive case
       srcdest(src,dst)

srcdest(1,10)