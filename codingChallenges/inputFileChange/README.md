# Coding Exercise


## Challenge

You can select the programming language of your choice to create a command line batch application which takes in an input file with a series of changes in order to generate an output.

Details:
1.	Input File (tr_member_fav_drink.json), this consists of user, drink and favorite_tr_drinks that are part of a marketing service
2.	Your application will take this file (tr_member_fav_drink.json) as input 
3.	Your application will also take a change file as input
4.	You can structure the change file the way you like
5.	The changes file should include multiple changes in one file
6.	You will code for the changes your application should support
7.	Your application will output "tr_member_fav_drink_updated.json" in the same structure as tr_member_fav_drink.json with the processed changes
8.	Sample: appname <inputfile> <changefile> <outputfile> 
 

The types of changes your application needs to support are:
1.	Add an existing drink to an existing favorite_tr_drinks
2.	Add a new favorite_tr_drinks for an existing user; the favorite_tr_drinks should contain at least one existing drink
3.	Remove an existing favorite_tr_drinks



## Challenge Notes

Input data is a json file with three arrays that are composed of the following objects: user, favorite_tr_drinks, and drink. 

