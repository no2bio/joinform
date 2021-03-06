# -*- coding: utf-8 -*-
DEBUG_TO_WEB=True # set to True when debugging
PAGE_TITLE='מתנדבים למאבק במאגר הביומטרי'
PAGE_SUBTITLE='רוצים לעזור? ספרו לנו איך' # html is allowed here
SECURE_PAGE_SUBTITLE='רוצים לעזור? ספרו לנו איך' # subtitle when both gpg and ssl are on. html allowed.
SMTP_FROM='myself@gmail.com' # An email address that you're allowed to send from
SMTP_TOS=['me@home.org','gang@work.com'] # list of recepients
SMTP_HOST='smtp.gmail.com' # This is for gmail, depends on your mail provider
SMTP_PORT=587 # usually 587
SMTP_KEYFILE=None # If you know what it is, you know what to put there
SMTP_CERTFILE=None # Ditto
SMTP_USERNAME=SMTP_FROM # for gmail (and usually), SMTP_FROM is what you need
SMTP_PASSWORD='*******'
SUBJECT_PREFIX='[whatmail] ' # subject line prefix. good for mail filters

### Supported captcha libraries ###
# There are 2 options (in order of priority):
# 1) Winograd text captcha (the default)
# 2) PyCaptcha (requires installing PILLOW)

### Use winograd text captcha
# set to false if you want no captcha
USE_WINOCAPTCHA=True
USE_PYCAPTCHA=False # Requires PILLOW

# Folder containing mustache templates
SKIN_FOLDER='skins/join2he'
#SKIN_FOLDER='skins/default'
## ובעברית...
# SKIN_FOLDER='skins/hebrew'

FIELD_SPREADSHEET='fields-he.csv'

# Messages
MSG_EMPTY_FROM="לא הכנסת כתובת דואל"
MSG_CAPTCHA_FAILED="לא הצלחת להוכיח שאת/ה לא רובוט :)"
MSG_CAPTCHA_TRY_AGAIN="עכשיו ברצינות ;)"
MSG_SUCCESS_TITLE="הטופס נשלח"
MSG_FAIL_TITLE="תקלה בשליחת הטופס"

#MSG_EMPTY_FROM="Empty name/email. I need to know how to get back to you."
#MSG_CAPTCHA_FAILED="You've failed the captcha test. Convince me again that you're not a robot."
#MSG_CAPTCHA_TRY_AGAIN="Try to get it right this time :)"
#MSG_SUCCESS_TITLE="Mesage sent"
#MSG_FAIL_TITLE="Mesage sending failed"

## ובעברית...
#MSG_EMPTY_FROM="לא הכנסת פרטי יצירת קשר"
#MSG_CAPTCHA_FAILED="לא הצלחת להוכיח שאת/ה לא רובוט :)"
#MSG_CAPTCHA_TRY_AGAIN="עכשיו ברצינות ;)"
#MSG_SUCCESS_TITLE="ההודעה נשלחה"
#MSG_FAIL_TITLE="תקלה בשליחת ההודעה"

### gnupg (see README for details)
GPG_ENABLED=False # Enable if you have gpgme and know how to conf this
# This should work for most sane people:
GPG_ENCRYPT_TO=SMTP_TOS
# If you want to get tricky, this would also work:
# GPG_ENCRYPT_TO=['0x......','someone@else.com']

# GPG_HOMEDIR should be a whatmail-specific gpg dir.
# import all GPG_ENCRYPT_TO pubkeys there. E.g. like this:
# gpg --homedir '/path/to/.gnupg' --import < mypub.asc
# Make sure that the user running the web server (e.g. www-data) has sufficient
# permissions at GPG_HOMEDIR (if you get "Error: (7, 16383, u'End of file')" it's
# either permissions, or you forgot to import a GPG_ENCRYPT_TO pubkey).
GPG_HOMEDIR='/path/to/.gnupg'

# REDIRECT_TO_SSL should be an https:// url or you'll loop
# REDIRECT_TO_SSL='https://secure.example.com/path/to/whatmail/'
REDIRECT_TO_SSL=''
