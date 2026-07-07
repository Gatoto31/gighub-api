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