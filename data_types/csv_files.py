import csv

# with open('test.csv','r') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         # next(csv_reader)##skips the email printing text 
#         with open('new_name.csv','w') as new_file:
#             csv_writer = csv.writer(new_file,delimiter='\t')##delimeter is the in between the words
        
        
#             for line in csv_reader:
#                 csv_writer.writerow(line)
 



 #DICTIONARY READER and writer

with open('test.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # for line in csv_reader:
    #     print(line['email'])
    with open('new_name.csv','w') as new_file:
        fieldname = ['first_name','last_name','email']
        csv_writer = csv.DictWriter(new_file,fieldnames = fieldname,delimiter='\t')##delimeter is the in between the words
        

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
    