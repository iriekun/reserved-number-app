
## How to Install

`` $ git clone https://github.com/iriekun/telenor-poc.git``

``$ pip install -r requirements.txt``

## How to Setup Dynamo db

1. Create an AWS account

2. Generate AWS access key ID and secret access key from IAM AWS console

3. Store the key ID and secret in  ~/.aws/credentials 

## How to Run

To create dynamo db table

`` python createTable/createUserTable.py``

`` python createTable/createNumberTable.py``

To load data to dynamo db table

`` python loadTable/loadNumberTable.py``

`` python loadTable/loadUserTable.py``

To run the application

``$ flask run``

## How To Deploy Serverless

``zappa init``

``zappa deploy dev``

To update deployment

``zappa update dev``

