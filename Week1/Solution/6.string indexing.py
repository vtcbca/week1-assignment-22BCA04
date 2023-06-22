#write a python script to enter any string and print only part of string.
name=input('enter string: ')
start=input('start character:')
end=input('Ending character:')
#using .index we can easily perform this programe
start_index=name.index(start)
end_index=name.index(end)
print(name[start_index:end_index+1])
