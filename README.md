# Django Project - iTrade

## How To Setup
1. Clone This Project `git clone https://github.com/musfiqraihan/iTrade.git`
2. Create a Virtual Environment `python -m venv env`
3. Activate Virtual Environment `source env/Scripts/activate` or `cd env/Scripts` then `activate` *if you do this second step then you have to come back to the iTrade directory using directory using `cd ..` 2 times
4. Install Requirements Package `pip install -r requirements.txt`
5. Create Migration `python manage.py makemigrations`
6. Migrate Database `python manage.py migrate`
7. Create Super User `python manage.py createsuperuser`
8. Finally Run The Project `python manage.py runserver`

## Step 1
Says that " if the user with the email address already exists it logs the user in and shows a dashboard for the user. If the email address does not exist, a user is created with the email address, and the user logs in."

### My Opinion:
But i think this is not suitable because when a user, unfortunately mistyped his or her email address instead of the old one, that time he will get register with that email address even doesn't want to while sign in.
So, i differentiate them with two separate pages such as login and register as like as eBay.

### Challenging Part:
Users can log with their usernames or email address. In that case, I needed some help through online documentations that are provided below:
https://stackoverflow.com/questions/37332190/django-login-with-email <br>
https://stackoverflow.com/questions/25316765/log-in-user-using-either-email-address-or-username-in-django

## Step 2
Says that " If the user hits that button, a form appears, which lets the user input Product Name, Product Description, Product Photo, Minimum Bid Price, and Auction End DateTime."

### My Works:
I have done all parts as mention include the publisher name in the post.

### Challenging Part:
Facing no challenges at all.

## Step 3
Says that "  Users can place bids on items posted by others within the Auction End DateTime. Also, An user can input their bid in the auction item page for that product. After inputting a bid, it shows up in the bid list. The user can edit their bid before the auction ends."

### My Works:
I have done all parts as mention. But most enjoying this part when the date expires, bid form vanished.

### Challenging Part:
After the expiring date, the form vanished means users can't bid anymore for that particular product. In that case, I needed some help through online documentation that is provided below:
https://www.reddit.com/r/django/comments/bsi5mu/how_to_delete_django_object_after_specific_time/

## Step 4
Says that " The auction will end at Auction End DateTime, If you enter the auction item page for any item, it will show the bid winner for that item."

### My Works:
I have done all parts as mention. I will figure it out by sorting the maximum bidding amount.

### Challenging Part:
Not challenging at all. I needed some help through online documentation:
https://medium.com/programminginpython-com/python-program-to-find-the-largest-and-smallest-number-in-a-list-fd8fac8aba08
Note: For lazy purpose.....I can do my own without help internet if I think a little bit more.

## Step 5

### My Works:
admin can login into the same portal as well as users. 
username: admin or email: admin@gmail.com
password: admin
admin can justify running auctions and their value too.
The first chart for the auction's added and completed lists (but I didn't complete the completed list)
The second one for the auction's total value. 
Both are for 6 months calculation.

### Challenging Part:
Face a lot and learning new things is quite enjoyable.
Need some help with these:
https://stackoverflow.com/questions/4668619/how-do-i-filter-query-objects-by-date-range-in-django<br>
https://stackoverflow.com/questions/47875045/chart-js-creating-a-line-graph-using-dates

## Step 6

### My Works:
Trying my best to look pretty but taken mostly priority for the backend functionality.


