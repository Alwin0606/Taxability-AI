
from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.invoice_validator import (
    validate_gstin,
    validate_invoice_number,
    calculate_invoice_tax,
)

router = APIRouter(
    prefix="/api/invoices",
    tags=["Invoice Analyzer"],
)


class InvoiceRequest(BaseModel):
    invoice_number: str = Field(min_length=1)
    supplier_gstin: str
    buyer_gstin: str
    taxable_amount: float = Field(ge=0)
    gst_rate: float = Field(ge=0, le=100)
    supply_type: str


@router.post("/analyze")
def analyze_invoice(invoice: InvoiceRequest):
    errors = []

    if not validate_invoice_number(invoice.invoice_number):
        errors.append("Invalid invoice number format")

    if not validate_gstin(invoice.supplier_gstin):
        errors.append("Invalid supplier GSTIN format")

    if not validate_gstin(invoice.buyer_gstin):
        errors.append("Invalid buyer GSTIN format")

    try:
        tax_details = calculate_invoice_tax(
            taxable_amount=invoice.taxable_amount,
            gst_rate=invoice.gst_rate,
            supply_type=invoice.supply_type,
        )
    except ValueError as exc:
        errors.append(str(exc))
        tax_details = None

    return {
        "invoice_number": invoice.invoice_number,
        "valid": len(errors) == 0,
        "errors": errors,
        "tax_details": tax_details,
        "disclaimer": (
            "GSTIN format validation only. "
            "Actual GST registration status is not verified."
        ),
    }
