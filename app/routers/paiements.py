from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, auth
from ..database import get_db
import uuid

router = APIRouter(prefix='/api/paiements', tags=['Paiements'])

@router.get("/", response_model=List[schemas.PaiementOut])
def get_paiements(
    db: Session = Depends(get_db),
    current_user: models.Utilisateur = Depends(auth.get_current_user)
):
    return db.query(models.Paiement).order_by(models.Paiement.date.desc()).all()

@router.post("/")
def create_paiement(
    data: schemas.PaiementCreate,
    db: Session = Depends(get_db),
    current_user: models.Utilisateur = Depends(auth.get_current_user)
):
    paiement = models.Paiement(
        **data.dict(),
        reference=uuid.uuid4().hex[:12].upper(),
        caissier_id=current_user.id
    )
    db.add(paiement)
    db.commit()
    db.refresh(paiement)
    return paiement
