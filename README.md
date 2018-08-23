# StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

heroku link: https://whispering-lake-52466.herokuapp.com/

[![Build Status](https://travis-ci.org/KicaRonaldOkello/StackOverflow-lite.svg?branch=api)](https://travis-ci.org/KicaRonaldOkello/StackOverflow-lite)
[![Coverage Status](https://coveralls.io/repos/github/KicaRonaldOkello/StackOverflow-lite/badge.svg?branch=api)](https://coveralls.io/github/KicaRonaldOkello/StackOverflow-lite?branch=api)
[![Maintainability](https://api.codeclimate.com/v1/badges/ceac1a4f17c0022ca7bb/maintainability)](https://codeclimate.com/github/KicaRonaldOkello/StackOverflow-lite/maintainability)

# Getting Started.
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
# Prerequisites.
- Serverside Framework: Flask Python Framework.
- Testing Framework: PyTest
- API development environment: Postman


# Installing.
- Create a directory called StackOverflow-lite.

    `mkdir StackOverflow-lite`
- Enter the directory.

    `cd StackOverflow-lite`
- Clone the project from github using:

     git clone http://www.github.com/KicaRonaldOkello/StackoOverflow-lite/tree/api
- Install virtualenvironment.

    `pip install virtualenv`
- Activate virtualenvironment 

    `. bin/activate`
- Install flask

    `pip install flask`
- Install Postman.
 # Running the API.
 - Run the flask app in your terminal.
 
    `python run.py`
    
 -There are 4 endpoints which can be accessed in the following way.
 
   | Method | Endpoint | Status Code |
   |--------|----------|-------------|
   | GET | "/api/v1/questions" | 200 |
   | GET | "/api/v1/questions/<questionId>" | 200 |
   | POST | "/api/v1/questions" | 201 |
   | POST | "/api/v1/questions/<questionId>/answers" |201 |
    
  
 - Open Postman, choose any of the methods from the table and enter its approopiate end point.
 - After clicking send, Postman should return the corresponding status code.
  
 # Features.
 - users can post questions.
 - Users can get all questions.
 - Users can get one question.
 - Users can add an answer.
  
  # Running unittests.
  In order to know whether our endpoints are working, we can run unittests.
  - In your terminal:
  
    `pip install pytest`
  - Test your endpoints in the terminal
  
    `pytest tests/test_views.py`
  - It returns results showing which endpoints passed the tests and which endpoints failed the tests.
  
  # Authors.
  - Kica Ronald Okello.
  
  # Contributors.
  - Innocent Asiimwe
 
  


