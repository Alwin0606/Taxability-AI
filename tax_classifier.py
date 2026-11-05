
from app.schemas.classification import (
    ClassificationCategory,
    ClassificationRequest,
    ClassificationResponse,
)

# Demonstration keyword rules only.
# Not an authoritative GST classification database.

EXEMPT_KEYWORDS = {
    "exempt supply",
    "exempt service",
    "exempt goods",
}

NON_GST_KEYWORDS = {
    "petrol",
    "diesel",
    "alcohol for human consumption",
}


def classify_transaction(
    data: ClassificationRequest,
) -> ClassificationResponse:

    description = data.description.strip()
    normalized = description.lower()

    category = ClassificationCategory.UNKNOWN
    reason = "No matching demonstration rule found."
    confidence = 0.30
    review_required = True

    if any(keyword in normalized for keyword in NON_GST_KEYWORDS):
        category = ClassificationCategory.NON_GST
        reason = "Matched a demonstration non-GST keyword."
        confidence = 0.70

    elif any(keyword in normalized for keyword in EXEMPT_KEYWORDS):
        category = ClassificationCategory.EXEMPT
        reason = "Matched a demonstration exempt keyword."
        confidence = 0.70

    else:
        category = ClassificationCategory.UNKNOWN
        reason = (
            "Description alone is insufficient to establish "
            "GST taxability."
        )
        confidence = 0.30

    return ClassificationResponse(
        description=description,
        transaction_type=data.transaction_type,
        category=category,
        reason=reason,
        confidence=confidence,
        review_required=review_required,
        disclaimer=(
            "Demonstration classification only. Verify applicable "
            "GST legislation, notifications, HSN/SAC and conditions "
            "before making tax decisions."
        ),
    )

