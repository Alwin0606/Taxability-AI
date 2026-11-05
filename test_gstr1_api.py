
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_gstr1_summary_success():
    response = client.post(
        "/api/gstr1/summary",
        json={
            "invoices": [
                {
                    "invoice_number": "INV-001",
                    "supply_category": "B2B",
                    "taxable_amount": 10000,
                    "gst_rate": 18,
                    "cgst": 900,
                    "sgst": 900,
                    "igst": 0,
                },
                {
                    "invoice_number": "INV-002",
                    "supply_category": "B2C",
                    "taxable_amount": 2000,
                    "gst_rate": 5,
                    "cgst": 50,
                    "sgst": 50,
                    "igst": 0,
                },
            ]
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["invoice_count"] == 2
    assert data["totals"]["taxable_value"] == 12000
    assert data["totals"]["total_tax"] == 1900
    assert data["totals"]["total_value"] == 13900


def test_gstr1_summary_empty_invoices():
    response = client.post(
        "/api/gstr1/summary",
        json={"invoices": []},
    )

    assert response.status_code == 200
    assert response.json()["invoice_count"] == 0
    assert response.json()["totals"]["total_tax"] == 0


def test_gstr1_summary_invalid_invoice():
    response = client.post(
        "/api/gstr1/summary",
        json={
            "invoices": [
                {
                    "invoice_number": "INV-003",
                    "supply_category": "B2B",
                    "taxable_amount": -1000,
                    "gst_rate": 18,
                }
            ]
        },
    )

    assert response.status_code == 422


