
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["project"] == "Taxability AI"


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_gst_calculation():
    response = client.post(
        "/api/tax/gst/calculate",
        json={
            "amount": 10000,
            "tax_category": "taxable",
            "supply_type": "intra_state",
            "gst_rate": 18,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["cgst"] == 900
    assert data["sgst"] == 900
    assert data["igst"] == 0
    assert data["total_tax"] == 1800
    assert data["total_amount"] == 11800


def test_tax_classification():
    response = client.post(
        "/api/tax/classify",
        json={
            "description": "Purchase of office stationery",
            "amount": 5000,
        },
    )

    assert response.status_code == 200


def test_invoice_invalid_gstin():
    response = client.post(
        "/api/invoices/analyze",
        json={
            "invoice_number": "INV-001",
            "supplier_gstin": "invalid",
            "buyer_gstin": "invalid",
            "taxable_amount": 1000,
            "gst_rate": 18,
            "supply_type": "intra_state",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["valid"] is False
    assert "Invalid supplier GSTIN format" in data["errors"]
    assert "Invalid buyer GSTIN format" in data["errors"]
