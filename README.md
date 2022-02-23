# Bot

To get this repository working for you a couple of extra steps need to be taken

1. install selenium using the terminal :  
    pip install selenium  
    if you are having a "failed to find module" error. try restarting VScode

2. download chromedriver:  
    go to chrome and check your version under Customize and control Google Chrome(three dot symbol at the top right) >> help >> About Google Chrome  
    go to https://chromedriver.storage.googleapis.com/index.html and download your verisons drivers and place that file directory and use it in constants.py >> DRIVER_PATH

3. make a unconstant file to store your username and password:  
    Create a unconstant.py under syllabusbot  
    Place within:  
        USER = r"YOURUSERNAME"  
        PASS = r"YOURPASSWORD"  
