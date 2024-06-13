from sqlalchemy.orm import Session
from . import models, schemas

def create_configuration(db: Session, configuration: schemas.ConfigurationCreate):
    db_configuration = models.CountryConfiguration(**configuration.dict())
    db.add(db_configuration)
    db.commit()
    db.refresh(db_configuration)
    return db_configuration

def get_configuration(db: Session, country_code: str):
    return db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == country_code).first()

def update_configuration(db: Session, configuration: schemas.ConfigurationUpdate):
    db_configuration = db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == configuration.country_code).first()
    if db_configuration:
        for key, value in configuration.dict().items():
            setattr(db_configuration, key, value)
        db.commit()
        db.refresh(db_configuration)
    return db_configuration

def delete_configuration(db: Session, country_code: str):
    db_configuration = db.query(models.CountryConfiguration).filter(models.CountryConfiguration.country_code == country_code).first()
    if db_configuration:
        db.delete(db_configuration)
        db.commit()
    return db_configuration
