from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/create_configuration", response_model=schemas.Configuration)
def create_configuration(configuration: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_configuration = crud.get_configuration(db, country_code=configuration.country_code)
    if db_configuration:
        raise HTTPException(status_code=400, detail="Configuration already exists for this country")
    return crud.create_configuration(db=db, configuration=configuration)

@router.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = crud.get_configuration(db, country_code=country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

@router.post("/update_configuration", response_model=schemas.Configuration)
def update_configuration(configuration: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_configuration = crud.get_configuration(db, country_code=configuration.country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return crud.update_configuration(db=db, configuration=configuration)

@router.delete("/delete_configuration", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = crud.get_configuration(db, country_code=country_code)
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return crud.delete_configuration(db=db, country_code=country_code)
