from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError, jwt, ExpiredSignatureError # Certifique-se de importar ExpiredSignatureError
from dotenv import load_dotenv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os

router = APIRouter()

load_dotenv()
security = HTTPBearer()

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")

        if user_id is None:
            print("DEBUG: O payload do token não possui a reivindicação 'sub'.")

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido: payload sem identificador de usuário." # Mensagem mais descritiva
            )
        return user_id

    except ExpiredSignatureError:
        print("DEBUG: O token expirou.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado."
        )
    except JWTError as e:
        print(f"DEBUG: Token inválido: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido: {e}"
        )
    except Exception as e:
        print(f"DEBUG: Ocorreu um erro *realmente* inesperado e não tratado: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro interno no servidor durante a validação do token. Por favor, tente novamente."
        )