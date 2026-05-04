from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas, auth
from ..database import get_db

router = APIRouter(prefix='/api/auth', tags=['Authentification'])

@router.post('/login')
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(models.Utilisateur).filter(
        models.Utilisateur.email == form_data.username
    ).first()
    
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if not user.actif:
        raise HTTPException(400, "Compte desactive")
    
    access_token = auth.create_access_token(data={'sub': user.email, 'role': user.role})
    
    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user': {
            'id': user.id,
            'nom': user.nom,
            'prenom': user.prenom,
            'email': user.email,
            'role': user.role
        }
    }

@router.get('/me', response_model=schemas.UtilisateurOut)
def get_current_user_info(
    current_user: models.Utilisateur = Depends(auth.get_current_user)
):
    return current_user
