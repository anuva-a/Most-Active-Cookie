# Most-Active-Cookie

RUN THE FOLLOWING COMMAND:
```
./most_active_cookie cookie_log.csv -d 2018-12-08
```

**most_active_cookie** is a Bash script that calls the Python script **most_active_cookie.py** and passes the arguments

The Python script takes the arguments and checks the number of arguments before proceeding. It reads the file line by line and matches the date parameter to the timestamp while keeping a count using a dictionary. 
The dictionary is then used to find the cookie(s) with maximum occurence on the specific date.
