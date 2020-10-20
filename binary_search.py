def search(x,find_array,start_index,end_index):
    if start_index -end_index ==-1:
        return -1
    if start_index -end_index ==1:
        return -1   
    n = end_index-start_index
    mid_index=start_index+ int(n/2)
    arr_val = find_array[mid_index]
    if arr_val==x:
        return mid_index+1
    elif arr_val>x:
        return search(x,find_array,start_index,mid_index)
    else:
        return search(x,find_array,mid_index,end_index)
arr=[1,3,6,7,8,10,15,20,25,26,29,30,32]
print(search(10,arr,0,len(arr)))
