LAB - Class 16
# Project: Serverless Functions
**Author:** Michelle Salazar
----
## Problem Domain

<ul><li>
Create a repository on Github and link it to Vercel account.
</li><li>Use requests library to interact with REST Countries API
</li><li>Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:
</li><li>The serverless function should handle a GET http request with a given country name that responds with a string with the form The capital of X is Y</li>
  <ul><li>E.g./capital-finder?country=Chile should generate an http response of The capital of Chile is Santiago.</li>
  <li>The serverless function should handle a GET http request with a given capital that responds with a string with the form The capital of X is Y</li></ul><ul><li>E.g./capital-finder?capital=Santiago should generate an http response of Santiago is the capital of Chile.</li></ul>

</li></ul>


## Links and Resources

API - https://restcountries.com/#rest-countries 

Severless server url - https://capital-finder-pearl.vercel.app/api/capitals


## Setup

cat requirements.txt


**PORT -** 3000

**DATABASE_URL -** URL to the running Postgres instance/db

*How to initialize/run your application (where applicable)*

Local host - vercel dev

## How to use your library (where applicable)
pip install requests

## Tests

• How do you run tests?
  
• Any tests of note?
  none

• Describe any tests that you did not complete, skipped, etc

## Links

Deployed site: 

https://capital-finder-pearl.vercel.app/api/capitals


---
*Notes:*
