
from enum import Enum

from pydantic import BaseModel, Field


class ClassificationCategory(str, Enum):
    TAXABLE = "taxable"
    EXEMPT = "exempt"
    NON_GST = "non_gst"
    UNKNOWN = "unknown"


class ClassificationRequest(BaseModel):
    description: str = Field(min_length=3, max_length=500)
    transaction_type: str = Field(
        default="sale",
        description="sale, purchase, service, or other"
    )


class ClassificationResponse(BaseModel):
    description: str
    transaction_type: str
    category: ClassificationCategory
    reason: str
    confidence: float
    review_required: bool
    disclaimer: str

