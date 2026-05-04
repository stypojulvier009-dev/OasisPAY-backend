from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, Enum as SQLEnum
from datetime import datetime
from .database import Base
import enum

class RoleEnum(str, enum.Enum):
    SUPER_ADMIN = "super_admin"
    ADMIN_ECOLE = "admin_ecole"
    DIRECTEUR = "directeur"
    COMPTABLE = "comptable"
    CAISSIER = "caissier"

class Utilisateur(Base):
    __tablename__ = "utilisateurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    telephone = Column(String)
    hashed_password = Column(String, nullable=False)
    role = Column(SQLEnum(RoleEnum), default=RoleEnum.CAISSIER)
    actif = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Etudiant(Base):
    __tablename__ = "etudiants"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    matricule = Column(String, unique=True, index=True, nullable=False)
    actif = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Paiement(Base):
    __tablename__ = "paiements"
    id = Column(Integer, primary_key=True, index=True)
    etudiant_id = Column(Integer, nullable=False)
    montant = Column(Float, nullable=False)
    devise = Column(String, default="CDF")
    type_frais = Column(String, nullable=False)
    methode_paiement = Column(String)
    reference = Column(String, unique=True, index=True)
    date = Column(DateTime, default=datetime.utcnow)
    caissier_id = Column(Integer, nullable=True)
