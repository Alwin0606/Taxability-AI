
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_valid_invoice():
    response = client.post(
        "/api/invoices/analyze",
        json={
            "invoice_number": "INV-001",
            "supplier_gstin": "29ABCDE1234F1Z5",
            "buyer_gstin": "27ABCDE1234F1Z5",
            "taxable_amount": 10000,
            "gst_rate": 18,
            "supply_type": "intra_state",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["valid"] is True
    assert data["tax_details"]["cgst"] == 900
    assert data["tax_details"]["sgst"] == 900
    assert data["tax_details"]["total_tax"] == 1800
    assert data["tax_details"]["total_amount"] == 11800


def test_invalid_gstin():
    response = client.post(
        "/api/invoices/analyze",
        json={
            "invoice_number": "INV-002",
            "supplier_gstin": "INVALID",
            "buyer_gstin": "27ABCDE1234F1Z5",
            "taxable_amount": 1000,
            "gst_rate": 18,
            "supply_type": "intra_state",
        },
    )

    assert response.status_code == 200
    assert response.json()["valid"] is False


def test_inter_state_invoice():
    response = client.post(
        "/api/invoices/analyze",
        json={
            "invoice_number": "INV-003",
            "supplier_gstin": "29ABCDE1234F1Z5",
            "buyer_gstin": "27ABCDE1234F1Z5",
            "taxable_amount": 10000,
            "gst_rate": 18,
            "supply_type": "inter_state",
        },
    )

    data = response.json()

    assert data["valid"] is True
    assert data["tax_details"]["igst"] == 1800
    assert data["tax_details"]["cgst"] == 0
    assert data["tax_details"]["sgst"] == 0


def test_invalid_invoice_number():
    response = client.post(
        "/api/invoices/analyze",
        json={
            "invoice_number": "INVALID@123",
            "supplier_gstin": "29ABCDE1234F1Z5",
            "buyer_gstin": "27ABCDE1234F1Z5",
            "taxable_amount": 1000,
            "gst_rate": 18,
            "supply_type": "intra_state",
        },
    )

    assert response.status_code == 200
    assert response.json()["valid"] is False
