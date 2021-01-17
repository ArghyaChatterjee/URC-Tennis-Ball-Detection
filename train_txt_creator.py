#! /usr/bin/env python

# Create & Open the file for writing
# Use your pc user name in place of 'user' in the path
dataFile = open('/home/user/darknet/data/train_ball.txt', 'w')

# Loop through 1 to 271 to write it to the output file.
for i in range (1, 271) :
    dataFile.write('data/train_ball/'+str(i)+'.jpg'+'\n')

# Close the output file
dataFile.close()