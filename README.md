# automate-vital-check
A script to automatically complete your VitalCheck screening each morning

# Explanation
VitalCheck, as any student at Fordham University is well aware by now, is a service designed to reduce the risk of COVID being spread
among members of a community, by requiring that each individual answer a daily questionnaire, confirming they have taken all possible 
steps to reduce their risk of spreading COVID-19 (not currently exhibiting symptoms, has not travelled elsewhere in the last two weeks,
etc.). 

While beautiful in theory, I believe VitalCheck really offers nothing as far as protecting the well-being of Fordham students. There is
no guarantee of honesty on the part of the students (and we've all seen how wary of COVID Fordham students can be /s), and we've learned 
quite well in the past year of the prevalence of asymptomatic carriers of COVID. As such, I find VitalCheck to be truly quite useless,
and have decided to save myself the 15 seconds I take to complete it each morning.

# Description
The code itself is pretty simple. Every day at a time specified in main.py, check_email.py uses IMAP4 to login to an email with the provided
credentials. It iterates through a certain number of emails (default is 5) and finds the first occurrence with the subject that our beloved
VitalCheck emails all come with. It parses the body for the link to the screening, and Selenium navigates to the webpage and clicks the "No
to all above" button. Congrats, you are now permitted to enter campus!

Regrettably, because I don't feel like going through the motions of having Google approve my "application", Gmail (reasonably) blocks requests
from the script to login. To work around this, I've instead used a trash email I have and enabled "Access to less secure apps". I've also added
a filter to my Fordham email to forward every VitalCheck email I receive to this email. After this it worked like a charm (and now my throwaway
email account is utterly unsecure; don't forget 2FA!).

It runs flawlessly from my computer, though I don't particularly feel like leaving my PC running 24/7 so it can spend five seconds per day 
completing my VitalCheck for me.

# Running it on a server
It turns out I know nearly absolutely nothing about actually deploying an application to "the cloud", and this proved to be perhaps the most 
difficult part of the project. I decided on Google Cloud Platform, and am running the script on a VM instance. After wrestling with dependencies
and inconsistencies for many hours, I finally got it to work by downloading and using GNU Screen. This allows the program to stay running in one 
"screen" even when the terminal is logged out of.

First, type ```screen``` and start the program in the newly opened screen. Once it is running, press Ctrl+Shift+A, then D to detach from the screen.

In order to return to the program to stop it and/or make changes, type ```screen -r```

# Doing it yourself
Good luck.

No but really I probably spent the most time to save myself the least time of any project I've ever done. Something like this:


[![Image](https://i.imgur.com/heiO3JR.png)](https://xkcd.com/1319/)

In order to recreate this, you will have to: 
* create another email to forward VitalCheck emails to
* decide on and start up a server to run main.py on perpetually
* tear your hair out fixing the problems that inevitably arise from moving a Windows-oriented application to a Linux server

Overall I probably spent 10 hours doing this, and I plan to save about 15 seconds every morning. As such I will have to make use of this script
for 2,400 days to make back my lost time. Whoo.
