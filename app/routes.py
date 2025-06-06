# routes.py
from fastapi import APIRouter
router = APIRouter()
@router.get('/admin')
def admin(): return {'msg': 'admin ok'}