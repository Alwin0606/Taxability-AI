
from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.gstr1_service import generate_gstr1_summary

router = APIRouter(
    prefix="/api/gstr1",
    tags=["GSTR-1 Summary"],
)


class GSTR1Invoice(BaseModel):
    invoice_number: str
    supply_category: str = "B2C"
    taxable_amount: float = Field(ge=0)
    gst_rate: float = Field(ge=0, le=100)
    cgst: float = Field(default=0, ge=0)
    sgst: float = Field(default=0, ge=0)
    igst: float = Field(default=0, ge=0)


class GSTR1Request(BaseModel):
    invoices: list[GSTR1Invoice]


@router.post("/summary")
def create_gstr1_summary(request: GSTR1Request):
    invoices = [
        invoice.model_dump()
        for invoice in request.invoices
    ]

    return generate_gstr1_summary(invoices)
