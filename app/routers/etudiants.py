from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(prefix='/api/etudiants', tags=['Etudiants'])

@router.get("/", response_model=List[schemas.UtilisateurOut])
def get_etudiants(
    db: Session = Depends(get_db),
    current_user: models.Utilisateur = Depends(auth.get_current_user)
):
    return db.query(models.Utilisateur).all()
