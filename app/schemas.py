from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class RoleEnum(str, Enum):
    SUPER_ADMIN = "super_admin"
    CAISSIER = "caissier"

class UtilisateurCreate(BaseModel):
    nom: str
    prenom: Optional[str] = None
    email: str
    password: str
    role: RoleEnum = RoleEnum.CAISSIER

class UtilisateurOut(BaseModel):
    id: int
    nom: str
    prenom: Optional[str] = None
    email: str
    role: RoleEnum
    actif: bool
    created_at: datetime

class PaiementCreate(BaseModel):
    etudiant_id: int
    montant: float
    type_frais: str
    methode_paiement: Optional[str] = None

class PaiementOut(BaseModel):
    id: int
    montant: float
    type_frais: str
    reference: str
    date: datetime

    class Config:
        from_attributes = True
