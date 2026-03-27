from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_admin_user
from app.db.session import get_db
from app.schemas.user import UserResponse, UserStatusResponse
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/pending", response_model=list[UserResponse])
def list_pending_users(
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin_user),
):
    service = UserService()
    return service.list_pending_users(db, current_admin)


@router.patch("/{user_id}/approve", response_model=UserStatusResponse)
def approve_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin_user),
):
    service = UserService()
    try:
        user = service.approve_user(db, user_id, current_admin)
        return {
            "message": "Empleado aprobado correctamente.",
            "user": user,
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.patch("/{user_id}/deactivate", response_model=UserStatusResponse)
def deactivate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin_user),
):
    service = UserService()
    try:
        user = service.deactivate_user(db, user_id, current_admin)
        return {
            "message": "Empleado desactivado correctamente.",
            "user": user,
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.patch("/{user_id}/reactivate", response_model=UserStatusResponse)
def reactivate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin_user),
):
    service = UserService()
    try:
        user = service.reactivate_user(db, user_id, current_admin)
        return {
            "message": "Empleado reactivado correctamente.",
            "user": user,
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
