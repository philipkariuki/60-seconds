# 60 Seconds

IP for MC18 week 3 of Python that requires creating a web application that allows users to create a a pitch within 60 seconds and also allows them to comment on other pitches if signed in.

#### By **Philip Kariuki**


## Description
This is a web application that allows various users to submit a short pitch. Users can also be able to view other pitches from different categories (Pick-up Lines, Interview Pitches, Product Pitches, Promotion Pitches), comment and vote. For a user to do any of that, they need to have registered.

## User Stories
* As a user I would like to view the different categories.
* As a user I would like to see the pitches other people have posted.
* As a user I would like to comment on the different pitches and leave feedback.
* As a user I would like to submit a pitch in any category.
* As a user I would like to vote on the pitch they liked and give it a downvote or upvote.

## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
|Display Various Pitch Categories | N/A | Various pitches grouped by category are displayed |
|Display pitches | **Click** on a Category| A page with a list of pitches from the selected category |
|Add new pitch | **Click** New pitch | User Should register/sign in to add new pitch |
|View Pitches | **Click** on a pitch | View a pitch and comments |
|Comment on a pitch | **Click** Comment | Registered User displays a form where a user can comment on a certain pitch |


## Setup/Installation Requirements
* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh
        
To clone this repo, open terminal in your desired folder then run:

        $ git clone https://github.com/philipkariuki/60-seconds/

To run the Python application within the folder from your cli:
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python
        
        
* Installing all the required modules

        (virtual)$ python3.6 -m pip install -r requirements.txt


## Known Bugs

No known bugs

## Technologies Used

* HTML
* CSS
* Python3.6
* Pip
* Flask
* Bootstrap
* Postgres Database
* gunicorn


## Contributors
<a href="https://github.com/philipkariuki">philipkariuki</a>

## [License](https://github.com/philipkariuki/60-seconds/blob/master/LICENSE)
MIT © 2019 [philipkariuki](https://github.com/philipkariuki
