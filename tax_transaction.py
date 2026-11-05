
from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class TaxTransaction(Base):
    __tablename__ = "tax_transactions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    transaction_type: Mapped[str] = mapped_column(
        String(30), nullable=False, default="gst_calculation"
    )

    amount: Mapped[float] = mapped_column(Float, nullable=False)
    gst_rate: Mapped[float] = mapped_column(Float, nullable=False)

    cgst: Mapped[float] = mapped_column(Float, nullable=False, default=0)
    sgst: Mapped[float] = mapped_column(Float, nullable=False, default=0)
    igst: Mapped[float] = mapped_column(Float, nullable=False, default=0)

    total_tax: Mapped[float] = mapped_column(Float, nullable=False)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)

    tax_category: Mapped[str] = mapped_column(String(30), nullable=False)
    supply_type: Mapped[str] = mapped_column(String(30), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
