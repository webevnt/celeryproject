# Given Django project for Payment Reminders

Here given description for project:-



Scope Of Work
Sending Scheduled Notifications for Payment Reminders
 
KEY Points
 
Create a NEW App e.g Notification (Optional: you can use Library Django Channels) \
Create a MODEL "Subscribers" with Foreign Key (SaleOrder) \
Notifications Rules Setup\
Django Job Celery to Execute in background to send Mail / SMS based on the Subscription. \
 
DND Option for Selective User \
Notification Templates with F.KEY of Country, SuperAgent, Store  ( Already Built) \
Mandatory Management of Bounce (for SMS / Email)\
After completing the daily Activity of Notification Sending – Inform to SuperAgent for Successful delivery and Bounced Delivery.\
 
Admin Actions:
Introduce a method “Rebuild Notification Subscriptions “ in SaleOrder\
 
Admin Datatable:\
Subscribers w.r.t SaleOrder\
Data table for Notification Rules with various List-filter and Search fields\
Data-table for Sent Notifications w.r.t SaleOrder\
Bounced Subscribers with List-Filter and Search

## Installation and setup?

There are few common step for installation we have to follow:

1.) First of all will Create and activate python environment and then navivate into project dir to install requirements

```sh
$ python3 -m venv projenv
$ source projenv/bin/activate
$ cd payreminder/
$ pip install -r requirements.txt
```

Next we have to install some prerequisite like redis-ser:

```sh
$ sudo apt update
```

and 
```sh
$ sudo apt install redis-server
```


And create .env file  with detail to used for Email services
EMAIL_HOST=xxxxxxxx \
EMAIL_PORT=xxxxxxxx \
EMAIL_USE_TLS=True \
EMAIL_HOST_USER=xxxxxxxx \
EMAIL_HOST_PASSWORD=xxxxxxxx


Now finally we run following command related to celery worker and celery beat before running django server


and 
```sh
$ celery -A payreminder worker -l info
$ celery -A payreminder beat -l info
```


Run let's run the django server

```sh
$ python3 manage.py runserver
```
