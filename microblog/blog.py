from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.utils import get_db
from . import service
from . schemas import PostCreate, PostList


router = APIRouter()


@router.get("/", response_model=List[PostList])
def post_list(db: Session = Depends(get_db)): # функция перед тем как будет запущена должна быть выполнена зависимость Depends - запустить другую функция get_db
  return service.get_post_list(db)


@router.post("/")
def post_list(item: PostCreate, db: Session = Depends(get_db)):
  return service.create_post(db, item)
