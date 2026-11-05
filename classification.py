
from fastapi import APIRouter

from app.schemas.classification import (
    ClassificationRequest,
    ClassificationResponse,
)
from app.services.tax_classifier import classify_transaction

router = APIRouter(
    prefix="/api/tax",
    tags=["Tax Classification"],
)


@router.post(
    "/classify",
    response_model=ClassificationResponse,
)
def classify_tax_transaction(data: ClassificationRequest):
    return classify_transaction(data)
