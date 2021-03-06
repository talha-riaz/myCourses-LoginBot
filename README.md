# myCourses Login Bot
A bot to automatically login to McGill's myCourses website with just one command.

<img src="https://github.com/talha-riaz/myCourses-LoginBot/blob/master/img/img1.png" height="250" width="1000">

<h3> Using the bot </h3>
Before you can start using the bot, make sure you complete all the steps in the section below.
Once you're all set up, you can run the following command to initiate the bot!

`$ python login_bot.py`

<h2> Getting started </h2> 
Before you can start using the bot, make sure all the system requirements are being met.

<h3> System Requirements </h3>
<ul>
  <li> Python installed on your system <br>
    <br>
       To check, open terminal and type <br>

        $ python --version

        Python 3.7.4
  </li>
  <li> Google Chrome (verify version for next steps) <br>
    <br>
       To check, goto Chrome > Settings > About Chrome <br>
       <img src="https://github.com/talha-riaz/myCourses-LoginBot/blob/master/img/img2.png" height="100" width="400">
 
  </li>
</ul>        

<h3> Installing Dependencies </h3>
In order to use the bot, we need to perform a one time setup. This is to install all the necessary dependencies. 
<ol>
  <li> <b> Installing Chromedriver </b> <br>
    Download the version of chromedriver corresponding to your Google Chrome version from <a href="https://chromedriver.chromium.org/downloads"> here. </a><br>
    Once downloaded, unzip the archive file 
   <br>  
    
    $ unzip chromedriver
    
   <br>
    Then move the file as shown to complete the installation of chromedriver
    <br>
    
     $ mv chromedriver /usr/local/bin
    
   <br>
    
    
    
  </li>
  <li> <b> Installing Selenium </b> <br>
  Make sure you are in the project repository. <br>
  Then run the following command on the terminal: <br>
  
  
    $ pip install selenium
  
  <br>
  </li>
   
</ol>

<h3> Setting up Login Credentials </h3>
A one time setup is required to save the myCourses login credentials, which the bot will use to log in automatically.<br>
This will be done as follows:<br>
<ol>
  <li>Navigate to ./data directory. </li>
  <li>Open secrets.py</li>
  <li>Modify the username and pw fields, following the same format as given</li>
</ol>
<img src="https://github.com/talha-riaz/myCourses-LoginBot/blob/master/img/img3.png">
<br>
IMPORTANT: Keep this information in a safe location, only accssible to you, as the credentials can be read off if the file is accessed. This is by no means a secure way to save login credentials. <br>
Future releases will focus more on security.

<h3> You're all set! </h3>
After completing the annoying (but necessary) steps, you should be able to run the bot using the simple run command mentioned at the beginning of this README. 
