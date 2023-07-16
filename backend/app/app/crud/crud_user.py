from app.models.user import User, UserCreate, UserUpdate
from app.core.security import get_password_hash
from app.crud.base import CRUDBase


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def create(self, db, *, obj_in: UserCreate) -> User:
        user_obj = User(
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            is_superuser=obj_in.is_superuser,
            full_name=obj_in.full_name,
        )
        db.add(user_obj)
        db.commit()
        db.refresh(user_obj)
        return user_obj


user = CRUDUser(User)
