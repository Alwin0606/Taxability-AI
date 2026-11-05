
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.tax_transaction import TaxTransaction

router = APIRouter(
    prefix="/api/tax",
    tags=["GST Transaction History"],
)


@router.get("/history")
def get_tax_history(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    gst_rate: float | None = Query(None, ge=0, le=100),
    supply_type: str | None = Query(None),
    tax_category: str | None = Query(None),
    db: Session = Depends(get_db),
):
    query = db.query(TaxTransaction)

    if gst_rate is not None:
        query = query.filter(TaxTransaction.gst_rate == gst_rate)

    if supply_type:
        query = query.filter(
            TaxTransaction.supply_type == supply_type
        )

    if tax_category:
        query = query.filter(
            TaxTransaction.tax_category == tax_category
        )

    total_records = query.count()

    transactions = (
        query.order_by(TaxTransaction.id.desc())
        .offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return {
        "total_records": total_records,
        "page": page,
        "page_size": page_size,
        "total_pages": (
            total_records + page_size - 1
        ) // page_size,
        "transactions": [
            {
                "id": t.id,
                "amount": t.amount,
                "gst_rate": t.gst_rate,
                "cgst": t.cgst,
                "sgst": t.sgst,
                "igst": t.igst,
                "total_tax": t.total_tax,
                "total_amount": t.total_amount,
                "tax_category": t.tax_category,
                "supply_type": t.supply_type,
                "created_at": t.created_at.isoformat(),
            }
            for t in transactions
        ],
    }
