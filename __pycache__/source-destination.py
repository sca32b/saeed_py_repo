

def srcdest (src,dst):
    if src == dst:
        print("Source and destination are same")
    else:

       print(src)
       src+=1
       srcdest(src,dst)

srcdest(1,10)