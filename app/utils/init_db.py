from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Utilisateur, RoleEnum
from ..auth import get_password_hash

def init_database():
    db = SessionLocal()
    try:
        admin_email = "stypojulvier009@mail.com"
        admin = db.query(Utilisateur).filter(Utilisateur.email == admin_email).first()
        if not admin:
            admin = Utilisateur(
                nom="Administrateur",
                prenom="Principal",
                email=admin_email,
                hashed_password=get_password_hash("Mukend123"),
                role=RoleEnum.SUPER_ADMIN,
                actif=True
            )
            db.add(admin)
            db.commit()
            print("Admin cree")
        else:
            print("Admin existe")
    except Exception as e:
        print(f"Erreur: {e}")
    finally:
        db.close()
