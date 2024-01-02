from pathlib import Path
import sys
import traceback
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy import exc as sqlalchemy_exc
from sqlalchemy.orm import Session
from utils.db_api.home_db.models.user import User

engine = create_engine(f'sqlite:///{Path("files/home.db")}')
session = Session(engine)


def add(
    UserId: int,
    UserFullName: str,
    DateStart: str,
    Status: str = "user",
):
    try:
        user: User = session.query(User).filter(User.UserId == UserId).one()
        return False
    except sqlalchemy_exc.NoResultFound:
        user = User(
            UserId=UserId,
            UserFullName=UserFullName,
            DateStart=DateStart,
            Status=Status,
        )
        session.add(user)
        session.commit()
        return user
    except Exception as e:
        traceback.print_exception(e)
        return False


def update(
    UserId: int,
    UserFullName: str = None,
    Status: str = None,
):
    try:
        user: User = session.query(User).filter(User.UserId == UserId).one()
        user.UserFullName = UserFullName or user.UserFullName
        user.Status = Status or user.Status
        session.add(user)
        session.commit()
        return user
    except sqlalchemy_exc.NoResultFound:
        return False
    except Exception as e:
        traceback.print_exception(e)
        return False


def get(UserId: int = None, UserFullName: str = None):
    try:
        if UserId:
            user: User = session.query(User).filter(User.UserId == int(UserId)).one()
        elif UserFullName:
            user: User = (
                session.query(User).filter(User.UserFullName == UserFullName).one()
            )
        return user
    except sqlalchemy_exc.NoResultFound:
        return False
    except Exception as e:
        traceback.print_exception(e)
        return False


def filters(Status: list = None):
    try:
        if Status:
            users: list[User] = session.query(User).filter(User.Status == Status).all()
    except sqlalchemy_exc.NoResultFound:
        return []
    except Exception as e:
        traceback.print_exception(e)
        return []


def delete(UserId: int):
    try:
        user: User = session.query(User).filter(User.UserId == UserId).one()
        session.delete(user)
        session.commit()
        return True
    except sqlalchemy_exc.NoResultFound:
        return False
    except Exception as e:
        traceback.print_exception(e)
        return False
