# TAXABILITY AI

<p align="center">
  <img src="https://img.shields.io/badge/TAXABILITY-AI-0F766E?style=for-the-badge&logo=python&logoColor=white"/>
</p>

<h3 align="center">
  Intelligent Indian Tax Analysis Platform
</h3>

<p align="center">
  <b>Automating GST. Simplifying Taxation. Empowering Businesses.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=flat-square&logo=fastapi"/>
  <img src="https://img.shields.io/badge/API-REST-black?style=flat-square"/>
  <img src="https://img.shields.io/badge/AI-Tax%20Intelligence-8B5CF6?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active%20Development-orange?style=flat-square"/>
</p>

---

## 💎 About the Project

**Taxability AI** is a modern taxation intelligence platform built to simplify Indian tax workflows through automation, intelligent analysis, and scalable backend architecture.

Designed with FastAPI and Python, it provides GST calculation, invoice analysis, and a foundation for AI-powered tax classification and compliance automation.

> **Vision:** Transform traditional taxation into an intelligent, automated, and efficient digital experience.

---

## ⚡ Core Capabilities

<table>
<tr>
<td width="50%">

### 🧮 GST ANALYZER

- Automated GST calculation
- CGST & SGST computation
- IGST computation
- Intra-state taxation
- Inter-state taxation

</td>
<td width="50%">

### 📄 INVOICE INTELLIGENCE

- Invoice data analysis
- Supplier GSTIN processing
- Customer GSTIN processing
- GST rate analysis
- Invoice processing foundation

</td>
</tr>
<tr>
<td width="50%">

### 🧠 TAX INTELLIGENCE

- Tax classification foundation
- Intelligent tax analysis
- Tax automation architecture
- Compliance intelligence roadmap

</td>
<td width="50%">

### 🚀 API ENGINE

- FastAPI backend
- REST API architecture
- Swagger documentation
- Modular service design
- Automated testing

</td>
</tr>
</table>

---

## 🛠️ Technology Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,git,github,vscode"/>
</p>

| Technology | Application |
|---|---|
| Python | Core development |
| FastAPI | API framework |
| Pydantic | Schema validation |
| Uvicorn | Application server |
| Pytest | Testing |
| Git | Version control |
| GitHub | Repository management |

---

## 🏛️ System Architecture

```text
                  ┌──────────────────────┐
                  │     TAXABILITY AI   │
                  │   Tax Intelligence  │
                  └──────────┬──────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
       GST ANALYZER    INVOICE AI     TAX ENGINE
              │              │              │
              └──────────────┼──────────────┘
                             │
                    ┌───────────────┐
                    │  FASTAPI API  │
                    └───────┬───────┘
                            │
                    REST API SERVICES
```

---

## 📂 Project Structure

```text
Taxability-AI/
│
├── backend/
│   └── app/
│       ├── api/
│       │   ├── tax.py
│       │   ├── invoice.py
│       │   └── classification.py
│       │
│       ├── core/
│       ├── models/
│       ├── schemas/
│       ├── services/
│       │
│       └── main.py
│
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Alwin0606/Taxability-AI.git
cd Taxability-AI
```

### Create Virtual Environment

```powershell
python -m venv backend\.venv
```

### Activate Environment

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
backend\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Application

```bash
python -m uvicorn app.main:app --app-dir backend --reload
```

---

## 🌐 API Documentation

| Service | URL |
|---|---|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |
| OpenAPI | http://127.0.0.1:8000/openapi.json |

### Available APIs

- `POST /api/tax/gst/calculate`
- `POST /api/invoices/analyze`

---

## 📊 GST Calculation

### Request

```json
{
  "amount": 10000,
  "tax_category": "taxable",
  "supply_type": "intra_state",
  "gst_rate": 18
}
```

### Response

```json
{
  "cgst": 900,
  "sgst": 900,
  "igst": 0,
  "total_tax": 1800,
  "total_amount": 11800
}
```

---

## 🗺️ Development Roadmap

- [x] GST Calculation Engine
- [x] Invoice Analysis API
- [x] FastAPI Backend
- [x] Swagger API Documentation
- [x] Backend Tests
- [ ] AI Tax Classification
- [ ] Intelligent Invoice OCR
- [ ] GST Compliance Automation
- [ ] Tax Anomaly Detection
- [ ] AI Tax Reports
- [ ] Advanced Tax Analytics

---

## 👨‍💻 Developer

<p align="center">
  <img src="https://avatars.githubusercontent.com/u/339983034?v=4" width="120"/>
</p>

<h3 align="center">Alwin0606</h3>

<p align="center">
  <a href="https://github.com/Alwin0606">
    <img src="https://img.shields.io/badge/GitHub-Alwin0606-181717?style=for-the-badge&logo=github"/>
  </a>
</p>

---

<p align="center">
  <b>⚡ TAXABILITY AI</b>
  <br/>
  <i>Making Tax Intelligence Smarter.</i>
  <br/><br/>
  ⭐ Built for the Future of Intelligent Taxation
</p>
