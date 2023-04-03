# StudentView-Webscrapper

## About the Program

StudentView Webscrapper operates by scrapping the html off of the StudentView account with BeautifulSoup. The program uses the Selenium Python module for importing information and logging in. The application receives your log-in information via a file you must create when first starting the program. 

The speed of receiving your data heavily relies on your wifi speed. The Selenium python module uses your computer's Google Chrome to perform tasks and go into the StudentView website. I average 20 seconds to collect all of the data and displaying it on the screen.


## Set Up

#### Creating the Password File

In the folder StudentView-Application would be downloaded in, create a new file named "id_password.txt". You can create the new file inside the terminal with :
```
> touch id_password.txt
```

Inside the file, write your Student ID on the first line, and write your Password on the second line :
```
Your_ID
Your_StudentView_Password
```
Your Student ID and Password will only be stored in your computer. 

#### Downloading ChromeDriver

Google Chrome downloaded on your computer is required for this application to run.
You first need to check your Chrome version. To check your version, you can go to chrome://version/. The first line will contain the version of your Chrome browser.
Go to https://chromedriver.chromium.org/downloads, and download the correct ChromeDriver version. You should unzip the file, and move it to the same folder this application would be inside.

#### Downloading requirements.txt

Inside of the terminal, go into the StudentView Directory and type:
```
pip install -r requirements.txt
```
to download all necessary Python Libaraies inside of this project.



## Run the Program

To run the program, you need to have python installed (version 3.0 and up). Type in the terminal :
```
./grades.sh
```
to run the program.
If you don't have permission access for the command, run :
```
chmod +x grades.sh
```
to give yourself permission to run the command.

If that doesn't work, do the previous steps, but with "grades.sh" changed to "grades2.sh".