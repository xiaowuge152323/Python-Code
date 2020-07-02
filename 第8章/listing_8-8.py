# Listing_8-8.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version $version  ----------------------------

# A while loop

print "Type 3 to continue, anything else to quit."
someInput = raw_input() # raw_input会得到字符串 input会得到整数60

# Keep looping as long as someInput ='3'
while someInput == '3': # while循环 判断，每次进入循环前都要进行判断，每次都执行
    print "Thank you for the 3.  Very kind of you."
    print "Type 3 to continue, anything else to quit."    # Body of the loop
    someInput = raw_input()                               #
print "That's not 3, so I'm quitting now."
