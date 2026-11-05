
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.tax_transaction import TaxTransaction
from app.schemas.tax import GSTRequest, GSTResponse
from app.services.gst_taxability import calculate_gst

router = APIRouter(prefix="/api/tax", tags=["GST Tax Analyzer"])


@router.post("/gst/calculate", response_model=GSTResponse)
def gst_calculation(
    data: GSTRequest,
    db: Session = Depends(get_db),
):
    # Calculate GST using existing service
    result = calculate_gst(data)

    # Prepare database record
    transaction = TaxTransaction(
        transaction_type="gst_calculation",
        amount=result.amount,
        gst_rate=result.gst_rate,
        cgst=result.cgst,
        sgst=result.sgst,
        igst=result.igst,
        total_tax=result.total_tax,
        total_amount=result.total_amount,
        tax_category=result.tax_category.value,
        supply_type=result.supply_type.value,
    )

    # Save transaction to PostgreSQL
    try:
        db.add(transaction)
        db.commit()
    except Exception as exc:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Failed to save GST transaction",
        ) from exc

    return result
