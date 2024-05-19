from pydantic import BaseModel

from pamps.security import HashedPassword
from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from pamps.models.post import Post


class User(SQLModel, table=True):
    """Represents the User Model"""

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: HashedPassword

    posts: List["Post"] = Relationship(back_populates="user")


class UserResponse(BaseModel):
    """Serializer for User Response"""

    """
    If a user wants to view information from another user, 
    this model contains what will be returned to him.
    """

    username: str
    avatar: Optional[str] = None
    bio: Optional[str] = None


class UserRequest(BaseModel):
    """Serializer for User request payload"""

    """
    Default model to be used when the user registers on the platform.
    """

    email: str
    username: str
    password: str
    avatar: Optional[str] = None
    bio: Optional[str] = None
