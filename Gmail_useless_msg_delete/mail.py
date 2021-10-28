import imaplib,email
import pprint
import getpass

imap_host = 'imap.gmail.com'

print ("""Before entering email or password \n
    Step1: Turn on access to third party apps
            (this can be found in Manage Google Accounts under Security tab; in chrome) \n
    Step2: Open gmail on pc click Settings -> See All Settings 
            -> Forwarding and POP/IMAP -> (Under Imap Access Status:) Select Enable IMAP -> finally click Save Changes \n
    Last Step: Once the process is complete turn off the things mentioned in step 1 & 2 \n
    Note: Once the deleting process is completed the mails will be in trash folder 
    just click Empty Trash in Gmail to delete the mails forever \n""")

imap_user = input("Email: ")
imap_pass = getpass.getpass()

imap = imaplib.IMAP4_SSL(imap_host)

imap.login(imap_user,imap_pass)

imap.select('Inbox')
# 'Medium Daily Digest','IQ Option',
topic_arr = ['Youtube','Facebook','Britannica','LinkedIn Editors','Quora','Academia.edu','Zoomcar','Freelancer.com','Sharekhan','Testbook.com','Internshala',
'Internshala Trainings','AMCAT Alerts','Best Price','Astrology.com','Astrology.com Specials','TarotReadingDaily.com','GaneshaSpeaks','Coursera',
'Hooman Mardox','Numerologist.com','Uber Eats',
'Reliance General Insurance','Jenn at Mailchimp','Mary','Quora Trending Stories','Zomato','TechGig Job Alert','online course','FlexJobs','Collegepond',
'Claim','Pocket','LinkedIn Notifications','Eliano','Studysid.com','Imperial Overseas','Bata Club','LinkedIn','Flex jobs','Embarcadero','Paytm']

def getBody(msg):
    if msg.is_multipart():
        return getBody(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)
        
        
def getData(topic):
    tmp, data = imap.search(None, 'FROM', '"{}"'.format(topic))
    return data
    
total_mail_moved_to_trash = 0;   
for topic in topic_arr:
    data = getData(topic)
    total_mail_moved_to_trash += len(data[0].split());
    print( "{t} {n}".format(t=topic,n=len(data[0].split())) )
    if(len(data) != 0):
        for num in data[0].split():
            # tmp, data = imap.fetch(num, '(RFC822)')
            # print(getBody(email.message_from_bytes(data[0][1])))
            imap.store(num,'+X-GM-LABELS','\Trash')

print("Total Mails moved to Trash: {mails}".format(mails = total_mail_moved_to_trash))
imap.close()
imap.logout()