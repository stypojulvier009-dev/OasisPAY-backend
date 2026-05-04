from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(prefix='/api/admin', tags=['Admin'])

@router.post("/create-super-admin")
def create_super_admin(db: Session = Depends(get_db)):
    email = "stypojulvier009@mail.com"
    user = db.query(models.Utilisateur).filter(models.Utilisateur.email == email).first()
    if not user:
        admin = models.Utilisateur(
            nom="Administrateur",
            prenom="Principal",
            email=email,
            hashed_password=auth.get_password_hash("Mukend123"),
            role=models.RoleEnum.SUPER_ADMIN,
            actif=True
        )
        db.add(admin)
        db.commit()
        return {"message": "Super admin cree avec succes"}
    return {"message": "Le super admin existe deja"}
