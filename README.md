# GigHub API - Nairobi Freelance Gigs

## Student Information
- **Admission Number:** C027-01-0899/2024
- **Project:** GigHub API for Nairobi Freelance Platform

## Overview
A RESTful API for managing freelance gigs in Nairobi. The API allows clients to post jobs and freelancers to find work opportunities. Built with FastAPI and Python.

## Dataset Information
Based on my admission number:
- **Last digit (9):** 5 + 9 = **14 gigs**
- **xxxx number (0899):** Odd → Categories: **Marketing, Data, Consulting**
- **First two digits (08):** < 10 → Currency: **KES**

## Features
- ✅ List all gigs with filtering (category, budget range)
- ✅ View specific gig by ID
- ✅ Search gigs by title
- ✅ Create new gigs
- ✅ Update gig budget or status
- ✅ Delete gigs

## Technologies Used
- FastAPI (Python web framework)
- Pydantic (Data validation)
- Uvicorn (ASGI server)
- Python 3.8+

## Installation

```bash
# Clone the repository
git clone https://github.com/Gatoto31/gighub-api.git

# Navigate to project
cd gighub-api

# Install dependencies
pip install fastapi uvicorn

# Run the server
python -m uvicorn main:app --reload

## Written Answers - Part 6

### Question 1: Design Decisions (2 marks)

**(i) What is your admission number, and how did it determine your dataset?**
My admission number is C027-01-0899/2024. The last digit is 9, which means I created 5 + 9 = 14 gigs. The xxxx number 0899 is odd, so my categories are ["Marketing", "Data", "Consulting"], and since the first two digits are 08 (less than 10), my currency is KES.

**(ii) Why did you choose to include the status field in your gig data model?**
I included the status field to track each gig's progress from posting to completion. The three statuses are "Open", "In Progress", and "Closed" to represent the lifecycle of each gig.

### Question 2: Validation (2 marks)

**(i) What validation rules did you apply to the budget field?**
I applied the rule that budget must be greater than zero (gt=0) to ensure all gigs have a positive budget amount. This is important to protect data integrity.

**(ii) How did you ensure category only accepts assigned values?**
I created a `GigCategory` enum class containing only my assigned categories: "Marketing", "Data", and "Consulting". The Pydantic model automatically validates input against these values.

### Question 3: Error Handling (2 marks)

**(i) What status code for a gig that does not exist?**
My API returns a 404 Not Found status code. This clearly communicates to the client that the requested gig ID does not exist in the database.

**(ii) What status code for invalid data?**
My API returns a 422 Unprocessable Entity status code. This indicates that the request format is correct but the content fails validation rules.

### Question 4: Search and Filtering (2 marks)

**(i) How does /gigs/search work?**
The endpoint accepts a `q` parameter and performs a case-insensitive title search. If no matches are found, it returns a 404 error with an explanatory message.

**(ii) How does /gigs with filtering work?**
The endpoint supports `category`, `min_budget`, `max_budget`, `skip`, and `limit` parameters. Each filter is applied sequentially to return only matching gigs.

### Question 5: Code Walkthrough (2 marks)

**(i) Explain the PUT /gigs/{gig_id} endpoint.**
This endpoint updates the budget or status of an existing gig. If the gig ID doesn't exist, it raises a 404 Not Found exception.

**(ii) Explain the POST /gigs endpoint.**
This endpoint creates a new gig by validating all fields and checking for duplicates. It auto-generates an ID, sets currency to KES, status to "Open", and adds a timestamp.