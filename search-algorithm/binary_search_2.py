data = [50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65]
search_number = 49
def abc(data, start, data_len, search):
    if data_len >  start:
        mid = (start+data_len) / 2 
        print(mid )
        if data[mid] == search:
            return mid
        elif data[mid] > search:
            return abc(data, start, mid-1, search)
        else:
            return abc(data , mid+1, data_len, search)
    else:
        return -1

print(abc(data, 0, len(data) , search_number) )
