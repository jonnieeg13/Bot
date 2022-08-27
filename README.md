# Syllabus Bot
This script allows you to create folders and place within them syllabus for classes in a specified semester or current from UTA MyMav and Canvas

To get this repository working for you a couple of extra steps need to be taken
1. Clone this repo "https://github.com/jonnieeg13/Bot"
2. Make sure Python 3.7 or later is installed in your system
3. Run the command "pip install -r requirements.txt" to download required python packages
4. make a file named "unconstant.py" to store your username and password:  
    Create "unconstant.py" under syllabusbot directory (DO NOT SAVE THE unconstant.py FILE TO GIT)  
    Place within user name and password for UTA mymav:  
        USER = r"YOURUSERNAME"  
        PASS = r"YOURPASSWORD"
5. Create a file name .env in the syllabusbot directory:
    - Login to Canvas and generate API token
    - add API token to .env file as CANVAS_API_TOKEN="API TOKEN HERE" (DO NOT SAVE THE .env FILE TO GIT)
   
6. To run program run from IDE or CLI as "python run.py" in the correct directory

    
