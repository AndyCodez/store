# Simple Store Service
This is a simple python service store app written in Django. It uses Firebase for authentication. This will handle google signin with Oauth2 and OpenID.

## Live API url
The live API url can be found here: https://store-alpha-mocha.vercel.app/api

## Prerequisites

1. Python3 installed on your machine.
2. Docker and Docker Compose installed to run the PostgreSQL database.
3. Firebase project set up with authentication enabled.
   
## Setup Instructions

1. Clone the Repository:

```bash

git clone https://github.com/AndyCodez/store
cd store
```

2. Configure Firebase
   1. Set up a Firebase project on the Firebase Console. 
   2. Enable Firebase Authentication for your project and configure it according to use google authentication. 
   3. Download the Firebase configuration file and take note of the values in the file to be populated in the env variables below.

3. Set Up Environment Variables:

Create a .env file in the root directory of your project with the following content, replacing with your actual values:

```dotenv

AT_USER=
AT_API_KEY=
TC4A_DB_NAME=
TC4A_DB_USER=
TC4A_DB_PASSWORD=
TC4A_DB_HOST=
TC4A_DB_PORT=
FIREBASE_TYPE=
FIREBASE_PROJECT_ID=
FIREBASE_PRIVATE_KEY_ID=
FIREBASE_PRIVATE_KEY=
FIREBASE_CLIENT_EMAIL=
FIREBASE_CLIENT_ID=
FIREBASE_AUTH_URI=
FIREBASE_TOKEN_URI=
FIREBASE_AUTH_PROVIDER_X509_CERT_URL=
FIREBASE_CLIENT_X509_CERT_URL=
```

4. Install Dependencies:

```bash

pip install -r requirements.txt
```

5. CI/CD:

The application is configured to utilize GitHub Actions to run automated tests and manage releases by building images and deploying to a Docker registry automatically upon pushing to the main branch.

The service is configured to be deployed to Vercel automatically.

6. Running the Application:

Use Django's manage.py to run the application locally:

```bash

python manage.py runserver
```
7. Authentication is token-based and designed to work via Firebase Authentication, which supports OAuth2 and OpenID Connect. The frontend application interacts directly with Firebase for OAuth2 (e.g., via Google) and interacts with this backend Python service, which validates the given token.

8. Testing
To run tests:

```bash
python manage.py test
```
To run tests with coverage:

  Install the testing dependencies:

```bash

pip install coverage
```
  Run the tests with coverage:

```bash

coverage run manage.py test
```
  Generate the coverage report:

```bash

coverage report
```
  To generate an HTML report for better visualization:

```bash

coverage html
```
Open the htmlcov/index.html file in a web browser to view the detailed coverage report.