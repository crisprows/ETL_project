# ETL_project
We were tasked with Extracting, Transforming and Loading a self chosen set of data. 

Extract: We took an exported CSV of keywords from Wordstream as well as lists of keywords scraped from websites to compare.
Transform: We compared the string lists using Python functions and then stored the resultant ratings (amounts of hits between both lists) in a variable for storage. 
Load: Having combined the results together into dictionaries, we used Pandas dataframes to assemble a dictionary of dictionaries to be loaded into MongoDB using PyMongo. This was chosen beause the data was ultimately all text information and MongoDB is an efficient and useful system for list-like objects. 
