from datetime import datetime, timedelta
from check_email import OpenEmail, CheckEmails, ParseBody, CloseEmail
from navigate_vitalcheck import GetWebPage
from time import sleep
import pytz

checkTime = (7, 0)  # The time for the script to check for the VitalCheck email in hours, minutes (default is 7:00 AM)

# Localize time from UTC to US/Eastern (now it doesn't matter WHERE the program is running!)
utc = pytz.timezone('UTC')
est = pytz.timezone('US/Eastern')
now = utc.localize(datetime.utcnow()).astimezone(est)

# Check if the current time is before/after the time to check for email. If after, set next check for following day
nextCheck = est.localize(datetime(now.year, now.month, now.day, hour=checkTime[0], minute=checkTime[1]))
if nextCheck <= now:
    nextCheck += timedelta(days=1)

completed = False

while 1:
    email = input("Enter email address: ")
    password = input("Enter password: ")

    repeat = False
    print("\nRunning initial email connection test...")
    if OpenEmail(email, password):
        print("Successfully established connection!\n")
        break
    else:
        print("Could not connect to " + email)
        repeat = input("Would you like to try again? [y/n]: ").lower() == 'y'
        if repeat:
            print()
            continue
        else:
            print("Exiting program")
            quit()

print("------------------------------------------------------------------")
print("Waiting for next email. Checking next on " + nextCheck.strftime("%m/%d/%Y") + " at " + nextCheck.strftime("%H:%M"))

while 1:
    now = datetime.now()# - timedelta(hours=5)
    if not completed and (now.hour, now.minute) == checkTime:
        print("Opening connection with " + email)
        imap, messages = OpenEmail(email, password)

        print("Checking for VitalCheck email")
        email_body = CheckEmails(imap, messages, 5)
        if imap and email_body:
            print("Found VitalCheck email, navigating to webpage to complete screening")
            link = ParseBody(email_body)
            if link:
                if GetWebPage(link):
                    print("Successfully completed screening")
                else:
                    print("Could not successfully complete screening")
            else:
                print("Error retrieving link to VitalCheck page")
        else:
            print("VitalCheck email not found")

        print("Closing connection to " + email + "...")
        CloseEmail(imap)
        nextCheck += timedelta(days=1)
        print("Connection to " + email + " closed")
        print("------------------------------------------------------------------\n")
        print("Waiting for next email. Checking next on " + nextCheck.strftime("%m/%d/%Y") + " at " + nextCheck.strftime("%H:%M"))

        completed = True   # Prevent the script from completing the screening over and over again at the specified time
    elif completed and (now.hour, now.minute) != checkTime:
        completed = False  # Reset the script to check again the next day
