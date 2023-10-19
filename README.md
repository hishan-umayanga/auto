# autofill-detection-and-graphical-password-system


## Setup Guide - 

Copy & Paste the below commands step by step.

### clone repo
       git clone the repository

### Navigate to the folder
         cd Graphical-Password-User-Authentincation

### Install dependencies; look for requirements.txt file
       pip install Django

### djanog stuff for database creation
       python manage.py makemigrations
       python manage.py migrate

### create admin account - Create a login to use on admin page
       python manage.py createsuperuser

### create or Run virtual environment
       env\Scripts\activate

### Run Django server
     python manage.py runserver


## introduction

* The current state of online security is reliant on traditional text-based passwords for authentication. 
However, this approach is vulnerable to various security threats such as phishing, brute force attacks, and 
password guessing. These vulnerabilities compromise user data and the overall security of websites.

* Additionally, text-based passwords often lead to poor user experiences due to their complexity and 
difficulty to remember, especially when users need to manage multiple accounts.

* To address the challenge of remembering complex passwords, web browsers have introduced a password 
save option and an auto-fill feature. However, the auto-fill option poses a security risk, as it autofill user 
login details without validating the user.

* This may result in a compromise of user login details and a potential threat to the security of website user 
data

* Consideration of image size is necessary to save storage space and selection of appropriate 
images is needed to accommodate various user conditions, such as color blindness.

* In the autofill feature, some web browsers do not validate the user before Autofilling on 
the login page.

## version

* This project used Django version 4.2.1 and Python version 3.11.3

## homepage
![home page](https://github.com/hishan-umayanga/autofill-detection-and-graphical-password-system/blob/master/readme%20img/new%20home.png)
## Project
![projects](https://github.com/hishan-umayanga/autofill-detection-and-graphical-password-system/blob/master/readme%20img/Screenshot_1.png)

## Display resposive
![projects](https://github.com/hishan-umayanga/autofill-detection-and-graphical-password-system/blob/master/readme%20img/Screenshot_3.png)
![projects](https://github.com/hishan-umayanga/autofill-detection-and-graphical-password-system/blob/master/readme%20img/responive%20g.png)

## graphical password system
![projects](https://github.com/hishan-umayanga/autofill-detection-and-graphical-password-system/blob/master/readme%20img/gp%20l.png)
![projects](https://github.com/hishan-umayanga/autofill-detection-and-graphical-password-system/blob/master/readme%20img/g%20reg.png)



