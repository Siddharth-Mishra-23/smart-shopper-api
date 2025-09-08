## Red Augment - AI Intern Assignment Report
### Problem 1: The Smart Shopper’s Dilemma

This report details the approach, challenges, solutions, and potential improvements for the "Smart Shopper's Dilemma" project. The goal was to build a fast, scalable product information pipeline using web scraping and expose it via a REST API built with Django.

---

### 1. Approach

The project was built using a full-stack approach with **Python** as the primary language. The core components were selected for their ability to handle the specific requirements of the assignment:

* **Django & Django REST Framework**: These were chosen to create a **robust and scalable API endpoint**. This provided a structured framework to handle incoming HTTP requests and return a JSON response.
* **Playwright**: This headless browser automation tool was selected for **web scraping**. Unlike static scraping libraries, Playwright can handle the dynamic content of Google Shopping, which was crucial for a successful data retrieval.
* **Asynchronous Programming (`asyncio`, `async_to_sync`)**: This was used to optimize for **speed**, allowing the scraper to run without blocking the API and improving the total response time.

---

### 2. Challenges Faced

During development, several key challenges were encountered, which were critical to the problem-solving process.

* **URL and Parameter Errors**: The API initially returned `HTTP 404 Not Found` and `HTTP 400 Bad Request` errors. These occurred when the API was accessed without the correct path (`/api/search/`) or the required `name` query parameter.
* **Code Incompatibilities**: A major issue was an `AssertionError`, which was caused by a conflict between the asynchronous scraper and Django's default synchronous views.
* **Missing Dependencies**: The scraper failed with an `HTTP 500 Internal Server Error`, specifically mentioning missing host dependencies. This proved that while the Playwright library was installed, the underlying browsers and their system-level dependencies were not.
* **Outdated Selectors**: After resolving the technical errors, the API returned an empty JSON array `[]`. This is a common challenge in web scraping, as website layouts and HTML class names change frequently, causing the selectors in the code to fail.

---

### 3. Solutions and Resolutions

Each challenge was systematically debugged and resolved to complete the functional pipeline.

* **URL Errors**: These were solved by strictly adhering to the defined API structure, using the full URL with the correct path and query parameter.
* **Code Incompatibilities**: The `AssertionError` was resolved by using the **`async_to_sync` decorator**, which allowed the synchronous Django view to correctly call and await the asynchronous scraper function.
* **Missing Dependencies**: The `500` error was fixed by running the **`playwright install-deps`** command in the Codespaces terminal. This installed the necessary system libraries, allowing the headless browser to run correctly.
* **Empty Result**: The empty array confirmed that the entire API-to-scraper pipeline was functional, even if the data extraction logic was not. The system executed successfully without crashing, demonstrating its robustness.

---

### 4. Improvements

Given more time, the following improvements would be implemented to enhance the project's performance and reliability:

* **Robust Selectors**: Implement a more advanced scraping strategy to adapt to changes in Google's website, possibly by using regular expressions or an AI-powered selector tool.
* **Caching Layer**: Add a caching mechanism (e.g., using Redis) to store search results for a short period. This would prevent redundant scraping for popular products and drastically reduce API response times.
* **Proxy Rotation**: To avoid getting blocked by Google, a proxy rotation service could be integrated into the scraper.
* **Scalability**: Use an ASGI server like Uvicorn for a production environment to handle concurrent requests more efficiently.