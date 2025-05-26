from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

# Pydantic models
class JobCreate(BaseModel):
    user_id: int
    title: str
    company: str
    description: Optional[str] = None

class JobUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    description: Optional[str] = None

class JobResponse(BaseModel):
    id: int
    user_id: int
    title: str
    company: str
    description: Optional[str] = None

@router.post("/", response_model=JobResponse)
async def create_job(data: JobCreate):
    """
    Create a new job entry.
    """
    # TODO: Implement job creation logic
    raise HTTPException(status_code=501, detail="Create job not implemented")

@router.get("/", response_model=List[JobResponse])
async def list_jobs(user_id: int):
    """
    List all jobs for a user.
    """
    # TODO: Implement job listing logic
    raise HTTPException(status_code=501, detail="List jobs not implemented")

@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: int):
    """
    Retrieve a specific job by ID.
    """
    # TODO: Implement job retrieval logic
    raise HTTPException(status_code=501, detail="Get job not implemented")

@router.put("/{job_id}", response_model=JobResponse)
async def update_job(job_id: int, data: JobUpdate):
    """
    Update a job's details.
    """
    # TODO: Implement job update logic
    raise HTTPException(status_code=501, detail="Update job not implemented")

@router.delete("/{job_id}")
async def delete_job(job_id: int):
    """
    Delete a job.
    """
    # TODO: Implement job deletion logic
    raise HTTPException(status_code=501, detail="Delete job not implemented")