from fastapi import APIRouter
from src.routes.get_templates import router as get_templates

router = APIRouter()

router.include_router(get_templates)
