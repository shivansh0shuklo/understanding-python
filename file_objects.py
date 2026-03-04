#file objects basics
# f  = open('test.txt','r')
# print(f.name)#printing the name of the file
# print(f.mode)#for printing the mode of the file 
# f.close()#if we open the file with 'open' then we have to close it otherwise we will end up with leaks and it can throw and error




# WITH OPEN ### it will act as a block of code so if we went outside the code block it will atomatically close the file    
# with open('test.txt','r') as f:
#     pass
# print(f.closed)##just check if its closed or not

# with open('test.txt','r') as f:

    ##1ST WAY OF READING
    #IF WE WANT TO READ A line
    # f_contents = f.readline()##for single line
    

    #2ND  WAY OF READING LINES
    # f_contents = f.readlines()#for all the lines
    # #readlines will return a list so list opertiona are valid
    # print(f_contents[1])
 

    #3RD WAY OF READING
    # for line in f:
    #     print(line,end="")##this end will remove the extraline that comesbecause of the \n at the ed of the each line
    

    #4TH WAY OF READING LINES
    # size_of_read = 10
    # f_contents = f.read(size_of_read)##in () we can specify how many characters do we want to display
    # print(f_contents,end='')
    # f.seek(0)
    # f_contents = f.read(size_of_read)
    # print(f_contents)
    # print(f.tell())
    # while len(f_contents)>0: 
    #     print(f_contents,end='*')
    #     f_contents = f.read(size_of_read)



##WRINTING IN THE FILE IN THE PYHTON
# with open('test2.txt','w') as f:#for creating the file test2 just use'w' and it will create the file if it does'nt exist 
#     f.write('hello')
#     f.seek(0)#this will overote the first one with the second one and it will not delete if the text is remaining in the first block 
#     f.write('r')



##COPING FROM ONE FILE TOO ANOTHER FILE 
with open('os_module.png','rb') as rf:##rb is used to copy the bytes of the image into the othen png 
    with open('os_copy.png','wb') as wf:
            # for line in rf:
            #       wf.write(line)
            chunk_size = 4096
            rf_chunk = rf.read(chunk_size)
            while len(rf_chunk)>0:
                  wf.write(rf_chunk)
                  rf_chunk = rf.read(chunk_size)