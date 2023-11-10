from django_mailbox.models import Mailbox
from datetime import datetime
import easyimap as e
import time

def my_scheduled_job():
    print(datetime.now().strftime("%a, %d %b %Y %H: %M: %S %z %Z"))

    mailboxes = Mailbox.active_mailboxes.all()
    mailboxes.get_new_mail()
    
    
   
    
    
               
    
    
    
    
        
        
    
   
    
    
