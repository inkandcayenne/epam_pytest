## Test Automation Part 1 PyTest HW

In this task you will create a project for running PyTest and perform basic testing of data from OrangeHRM website (https://opensource-demo.orangehrmlive.com/)

**Prerequisites**:  
1. Install Python  
2. Install PyTest  
3. Install Selenium Library  
4. Install chromedriver    
Instructions for macOS:    
    <code>
    $ cd $HOME/Downloads  
    $ wget http://chromedriver.storage.googleapis.com/2.22/chromedriver_mac32.zip  
    $ unzip chromedriver_mac32.zip  
    $ mkdir -p $HOME/bin  
    $ mv chromedriver $HOME/bin  
    $ echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_profile  
   </code>  
5. Use your favorite IDE (for example, PyCharm)

Please use repository https://bitbucket.org/kaliningleb25/test-automation-for-dqe-part1-pytest/src/master/ as a reference 
(You should have an access to the repository. If you don't have an access please let me know via email - Gleb_Kalinin@epam.com with Subject 'DQ Automation repository access')

---

## Task

1. Create a project for running PyTest  
You can fork **this project** as a template or create your own from scratch
2. Implement test_login() function to login to the website https://opensource-demo.orangehrmlive.com/
3. Implement get_table() function in main.py  
(*20 points*)  
Expected result - dictionary with column name as a KEY and list of records as a VALUE  
Hint: Use Selenium to login, go to Admin page, and get table with users
4. Implement test_data() function in main.py  
(*20 points*)  
Hint: use assert on list of errors from each DQ check (```assert not list_of_errors```)
5. Create 5 DIFFERENT test cases for data checks on OrangeHRM website and document them  
(*40 points*)  
Examples:  
- All records are completed (no blank values)  
- All records have length less than expected max length  
- All records have only allowed values
5. Create README
(*20 points*)

---

## Expected result

1. Repository with python files  
Suggested structure:  
```
main.py
checker.py
README.md
```

## Grades

- 5 stars - 100 points
- 4 stars - 80 points
- 3 stars - 60 points
- 2 stars - 40 points
- 1 star - 20 points