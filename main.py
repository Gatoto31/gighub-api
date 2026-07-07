from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from enum import Enum

# STEP 1: APP INITIALIZATION 
app = FastAPI(
    title="GigHub API - Nairobi Freelance Gigs",
    description="API for managing freelance gigs in Nairobi",
    version="1.0.0"
)

# STEP 2: ENUMS
class GigCategory(str, Enum):
    """Categories based on your admission number: odd -> Marketing, Data, Consulting"""
    MARKETING = "Marketing"
    DATA = "Data"
    CONSULTING = "Consulting"

class GigStatus(str, Enum):
    """Status options for gigs"""
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    CLOSED = "Closed"

# STEP 3: YOUR UNIQUE DATASET (14 GIGS)
gigs_db = [
    {
        "id": 1,
        "title": "Digital Marketing Campaign for Tech Startup",
        "description": "Need an experienced digital marketer to run a 3-month campaign for a Kenyan fintech startup. Focus on social media, email marketing, and SEO.",
        "category": "Marketing",
        "budget": 85000.00,
        "currency": "KES",
        "status": "Open",
        "client_name": "FinTech Kenya Ltd",
        "created_at": "2026-07-01T10:30:00"
    },
    {
        "id": 2,
        "title": "Data Analysis for Retail Business",
        "description": "Looking for a data analyst to analyze customer purchase patterns and provide insights for a retail chain. Must be proficient in Python and SQL.",
        "category": "Data",
        "budget": 120000.00,
        "currency": "KES",
        "status": "Open",
        "client_name": "RetailPlus Kenya",
        "created_at": "2026-07-02T09:15:00"
    },
    {
        "id": 3,
        "title": "Business Strategy Consulting for SME",
        "description": "Seeking a business consultant to help a local SME develop a growth strategy and operational efficiency plan. Experience in African markets preferred.",
        "category": "Consulting",
        "budget": 200000.00,
        "currency": "KES",
        "status": "Open",
        "client_name": "GrowthHub Africa",
        "created_at": "2026-07-03T14:20:00"
    },
    {
        "id": 4,
        "title": "Social Media Management for Beauty Brand",
        "description": "Need a creative social media manager to handle content creation and community engagement for a growing beauty brand in Kenya.",
        "category": "Marketing",
        "budget": 65000.00,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "Glow Beauty Kenya",
        "created_at": "2026-06-28T11:00:00"
    },
    {
        "id": 5,
        "title": "Machine Learning Model for Customer Churn",
        "description": "Looking for a data scientist to build a machine learning model to predict customer churn for a telecommunications company.",
        "category": "Data",
        "budget": 180000.00,
        "currency": "KES",
        "status": "Open",
        "client_name": "Telco Kenya Solutions",
        "created_at": "2026-06-30T16:45:00"
    },
    {
        "id": 6,
        "title": "HR Consulting for Remote Work Transition",
        "description": "Experienced HR consultant needed to help a company transition to a remote-first work model. Must have experience in HR policy development.",
        "category": "Consulting",
        "budget": 250000.00,
        "currency": "KES",
        "status": "Closed",
        "client_name": "RemoteWork Africa",
        "created_at": "2026-06-15T08:30:00"
    },
    {
        "id": 7,
        "title": "Content Marketing for EdTech Platform",
        "description": "Need a skilled content marketer to create blog posts, videos, and social media content for an education technology platform in Kenya.",
        "category": "Marketing",
        "budget": 95000.00,
        "currency": "KES",
        "status": "Open",
        "client_name": "EduTech Kenya",
        "created_at": "2026-07-04T13:20:00"
    },
    {
        "id": 8,
        "title": "Data Visualization Dashboard for NGOs",
        "description": "Looking for a data visualization expert to create interactive dashboards for multiple NGOs reporting on development projects in East Africa.",
        "category": "Data",
        "budget": 140000.00,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "Data4Good Initiative",
        "created_at": "2026-06-25T09:00:00"
    },
    {
        "id": 9,
        "title": "IT Governance Consulting",
        "description": "IT consultant needed to develop and implement IT governance frameworks for a medium-sized enterprise. Must understand ISO standards.",
        "category": "Consulting",
        "budget": 220000.00,
        "currency": "KES",
        "status": "Open",
        "client_name": "SecureTech Solutions",
        "created_at": "2026-07-01T10:00:00"
    },
    {
        "id": 10,
        "title": "Influencer Marketing Campaign for Fashion",
        "description": "Seeking a marketing specialist to plan and execute an influencer marketing campaign targeting Kenyan fashion consumers. Must have influencer network.",
        "category": "Marketing",
        "budget": 75000.00,
        "currency": "KES",
        "status": "Open",
        "client_name": "FashionHub Kenya",
        "created_at": "2026-07-02T15:30:00"
    },
    {
        "id": 11,
        "title": "Database Optimization for Healthcare Platform",
        "description": "Need a database expert to optimize and scale the database for a health tech platform serving clinics across East Africa.",
        "category": "Data",
        "budget": 160000.00,
        "currency": "KES",
        "status": "In Progress",
        "client_name": "HealthTech Africa",
        "created_at": "2026-06-20T14:20:00"
    },
    {
        "id": 12,
        "title": "Sustainability Consulting for Manufacturing",
        "description": "Sustainability consultant needed to help a manufacturing company reduce environmental impact and implement green practices.",
        "category": "Consulting",
        "budget": 300000.00,
        "currency": "KES",
        "status": "Closed",
        "client_name": "GreenManufacture Ltd",
        "created_at": "2026-06-10T08:45:00"
    },
    {
        "id": 13,
        "title": "Brand Strategy for Startup",
        "description": "Looking for a brand strategist to develop a complete brand identity and strategy for a new Kenyan startup in the agritech space.",
        "category": "Marketing",
        "budget": 110000.00,
        "currency": "KES",
        "status": "Open",
        "client_name": "AgriTech Kenya",
        "created_at": "2026-07-04T08:00:00"
    },
    {
        "id": 14,
        "title": "BI Reporting for Banking Sector",
        "description": "Need a business intelligence expert to create comprehensive reports and dashboards for a commercial bank in Kenya. Must know Power BI or Tableau.",
        "category": "Data",
        "budget": 190000.00,
        "currency": "KES",
        "status": "Open",
        "client_name": "Equity Bank Kenya",
        "created_at": "2026-07-03T11:30:00"
    }
]

#  STEP 4: PYDANTIC MODELS 
class GigCreate(BaseModel):
    """Model for creating a new gig"""
    title: str = Field(
        min_length=5, 
        max_length=100, 
        description="Gig title (5-100 characters)"
    )
    description: str = Field(
        min_length=20, 
        max_length=500, 
        description="Detailed description (20-500 characters)"
    )
    category: GigCategory = Field(
        description="Gig category (Marketing, Data, Consulting)"
    )
    budget: float = Field(
        gt=0, 
        description="Budget must be greater than 0"
    )
    client_name: str = Field(
        min_length=2, 
        max_length=50, 
        description="Client name (2-50 characters)"
    )

class GigUpdate(BaseModel):
    """Model for updating a gig (partial updates)"""
    budget: Optional[float] = Field(
        None, 
        gt=0, 
        description="Budget in KES"
    )
    status: Optional[GigStatus] = Field(
        None, 
        description="Gig status (Open, In Progress, Closed)"
    )

#  STEP 5: API ENDPOINTS 
@app.get("/")
def root():
    """Welcome endpoint showing API information"""
    return {
        "message": "Welcome to GigHub API - Nairobi Freelance Gigs",
        "student_id": "C027-01-0899/2024",
        "documentation": "/docs",
        "total_gigs": len(gigs_db),
        "categories_available": ["Marketing", "Data", "Consulting"],
        "currency": "KES"
    }

@app.get("/gigs")
def get_gigs(
    category: Optional[str] = Query(None, description="Filter by category (Marketing, Data, Consulting)"),
    min_budget: Optional[float] = Query(None, description="Minimum budget filter"),
    max_budget: Optional[float] = Query(None, description="Maximum budget filter"),
    skip: int = Query(0, description="Number of gigs to skip (pagination)"),
    limit: int = Query(10, description="Maximum number of gigs to return")
):
    """
    Return all gigs with optional filtering by category and min_budget/max_budget.
    """
    filtered_gigs = gigs_db.copy()
    
    if category:
        filtered_gigs = [
            g for g in filtered_gigs 
            if g["category"].lower() == category.lower()
        ]
    
    if min_budget is not None:
        filtered_gigs = [
            g for g in filtered_gigs 
            if g["budget"] >= min_budget
        ]
    
    if max_budget is not None:
        filtered_gigs = [
            g for g in filtered_gigs 
            if g["budget"] <= max_budget
        ]
    
    filtered_gigs.sort(key=lambda x: x["created_at"], reverse=True)
    
    total = len(filtered_gigs)
    paginated_gigs = filtered_gigs[skip:skip + limit]
    
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "currency": "KES",
        "gigs": paginated_gigs
    }

@app.get("/gigs/search")
def search_gigs(q: str = Query(..., description="Search query for title")):
    """
    Search for gigs by title (query param q).
    """
    if not q:
        raise HTTPException(status_code=400, detail="Search query parameter 'q' is required")
    
    results = []
    search_term = q.lower()
    
    for gig in gigs_db:
        if search_term in gig["title"].lower():
            results.append(gig)
    
    if not results:
        raise HTTPException(
            status_code=404, 
            detail=f"No gigs found matching title: '{q}'"
        )
    
    return {
        "query": q,
        "total": len(results),
        "currency": "KES",
        "gigs": results
    }

@app.get("/gigs/{gig_id}")
def get_gig(gig_id: int):
    """
    Return a single gig by its ID (return 404 if not found).
    """
    for gig in gigs_db:
        if gig["id"] == gig_id:
            return gig
    
    raise HTTPException(status_code=404, detail="Gig not found")

@app.post("/gigs")
def create_gig(gig: GigCreate):
    """
    Create a new gig (with validation).
    """
    for existing_gig in gigs_db:
        if existing_gig["title"].lower() == gig.title.lower():
            raise HTTPException(
                status_code=400, 
                detail="A gig with this title already exists"
            )
    
    new_id = max([g["id"] for g in gigs_db]) + 1 if gigs_db else 1
    
    new_gig = {
        "id": new_id,
        "title": gig.title,
        "description": gig.description,
        "category": gig.category.value,
        "budget": gig.budget,
        "currency": "KES",
        "status": "Open",
        "client_name": gig.client_name,
        "created_at": datetime.now().isoformat()
    }
    
    gigs_db.append(new_gig)
    
    return {
        "message": "Gig created successfully",
        "gig": new_gig
    }

@app.put("/gigs/{gig_id}")
def update_gig(gig_id: int, gig_update: GigUpdate):
    """
    Update a gig's budget or status.
    """
    for index, gig in enumerate(gigs_db):
        if gig["id"] == gig_id:
            if gig_update.budget is not None:
                gigs_db[index]["budget"] = gig_update.budget
            
            if gig_update.status is not None:
                gigs_db[index]["status"] = gig_update.status.value
            
            return {
                "message": "Gig updated successfully",
                "gig": gigs_db[index]
            }
    
    raise HTTPException(status_code=404, detail="Gig not found")

@app.delete("/gigs/{gig_id}")
def delete_gig(gig_id: int):
    """
    Delete a gig (return 404 if not found).
    """
    for index, gig in enumerate(gigs_db):
        if gig["id"] == gig_id:
            deleted_gig = gigs_db.pop(index)
            return {
                "message": "Gig deleted successfully",
                "gig": deleted_gig
            }
    
    raise HTTPException(status_code=404, detail="Gig not found")