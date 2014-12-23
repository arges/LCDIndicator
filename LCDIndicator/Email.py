import imaplib
import keyring

class Email:
  def __init__(self, server='imap.gmail.com', port='993'):
    self.IMAP_SERVER=server
    self.IMAP_PORT=port
    self.M = None
    self.response = None
    self.mailboxes = []
 
  def login(self, username, password):
    self.M = imaplib.IMAP4_SSL(self.IMAP_SERVER, self.IMAP_PORT)
    rc, self.response = self.M.login(username, password)
    return rc
 
  def logout(self):
    self.M.logout()

  def get_mail_count(self, folder='INBOX'):
    rc, count = self.M.select(folder)
    return count[0]

  def get_unread_count(self, folder='INBOX'):
    rc, count = self.M.select(folder)
    return len(self.M.search(None,'UnSeen')[1][0].split())

  def get_mailboxes(self):
    rc, self.response = self.M.list()
    for item in self.response:
      self.mailboxes.append(item.split()[-1])
    return rc

