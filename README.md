Red Augment - AI Intern Assignment
Problem 1: The Smart Shopper's Dilemma
This project is a solution for the "Smart Shopper's Dilemma" assignment. It consists of a real-time product information pipeline that scrapes data from Google Shopping and exposes it through a REST API built with Django. The pipeline is optimized for speed using asynchronous programming with Playwright.

Project Setup and Installation
Follow these steps to set up the project locally or in a Codespaces environment.

Clone the repository:

Bash

git clone https://github.com/<your-username>/smart-shopper-api.git
cd smart-shopper-api
Install Python dependencies:

Bash

pip install -r requirements.txt
(Note: Create a requirements.txt file with pip freeze > requirements.txt if you haven't already.)

Install Playwright browser binaries and dependencies:

Bash

playwright install
sudo playwright install-deps
Apply database migrations:

Bash

python manage.py migrate
How to Run the API
Start the Django development server:

Bash

python manage.py runserver
The server will start at http://localhost:8000/. If you are using Codespaces, the port will be forwarded and a public URL will be provided.

API Endpoint
The API has a single endpoint that accepts a product name and returns a list of product information.

Endpoint: /api/search/

Method: GET

Parameters: name (string)

Example Request
GET /api/search/?name=365%20WholeFoods%20Peanut%20Butter
Expected JSON Response
A successful response will return a 200 OK status and a JSON array containing product data.

JSON

[
  {
    "product_name": "...",
    "brand": "...",
    "price": "...",
    "total_weight": "N/A"
  },
  {
    "product_name": "...",
    "brand": "...",
    "price": "...",
    "total_weight": "N/A"
  }
]
(Note: An empty array [] will be returned if no products are found by the scraper.)
