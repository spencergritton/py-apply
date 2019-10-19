**py-apply**

*Summary:*<br>
This project was very quickly written to automatically apply to jobs (or atleast with much less pain) on greenhouse.io

This program takes in a list of urls. Goes to each url, changes your cover letter for the company and job title, then fills
out the majority of the forms on the application website. You will only have to select your resume, cover letter, maybe a few check boxes, and then submit.

Because this was written very quickly it doesn't completely automate the process so slight work is
needed by the user to finish each application.

*Setup:*<br>
You'll need selenium and python-docx I recommend using pip to install them.
- pip3 install selenium
- pip3 install python-docx

*Running the program:*<br>
Fill in 'inputs/urls.txt' with urls of jobs you want to apply to. Then run app.py. For each url your cover letter in '/outputs/CoverLetter.docx' will be updated to the company and job title 

**NOTE: Job title turned off currently as I'm only applying to software engineering roles. To turn back on remove comment in line 19 of coverLetter.py**. 
Then you'll simply have to check a few boxes, click on your resume and cover letter, then click submit.

**Note: Each url waits for 30 seconds for you to fill out any extra info you may have missed. This time can be changed in line 33 of app.py**

Feel free to use or fork this if it's helpful.

A final note: This project was inspired by a reddit post from https://github.com/harshibar/
