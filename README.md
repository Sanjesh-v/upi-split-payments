# UPI Split Payments: Product Strategy & Growth Analytics

## Overview

UPI has transformed digital payments in India, but group transactions remain fragmented. When multiple users share a restaurant bill, travel expense, or household purchase, one individual typically pays the full amount and manually collects repayments from others.

This project explores the design, analytics, and business impact of a **UPI Split Payments** feature that enables users to divide expenses at the point of payment while ensuring merchants receive the full transaction amount instantly.

The project combines Product Management, FinTech strategy, Python analytics, and Power BI visualization to evaluate adoption, operational efficiency, and revenue potential.

---

## Business Problem

Current group payment flows create several challenges:

* Manual repayment collection
* Delayed settlements
* Poor transaction transparency
* Increased user effort
* Missed monetization opportunities

The objective is to create a seamless split-payment experience that improves user convenience and increases payment platform engagement.

---

## Product Vision

**"Pay together, instantly."**

Enable users to:

* Split merchant payments directly through UPI
* Create equal or custom payment shares
* Track pending repayments
* Receive automated payment reminders
* Complete group settlements with minimal friction

---

## Project Objectives

* Design a scalable Split Payments product
* Generate realistic transaction and user datasets
* Analyze user adoption and payment behavior
* Measure settlement efficiency
* Estimate revenue opportunities
* Build executive dashboards for decision-making

---

## Dataset Overview

### Users

Contains demographic and engagement information.

| Field                |
| -------------------- |
| user_id              |
| age                  |
| city                 |
| signup_date          |
| monthly_transactions |

### Merchants

Contains merchant profile information.

| Field       |
| ----------- |
| merchant_id |
| category    |
| city        |

### Transactions

Contains transaction-level payment data.

| Field          |
| -------------- |
| transaction_id |
| user_id        |
| merchant_id    |
| amount         |
| date           |

### Split Requests

Contains split-payment information.

| Field                   |
| ----------------------- |
| split_id                |
| transaction_id          |
| group_size              |
| split_type              |
| settlement_time_minutes |
| status                  |

---

## Project Architecture

```text
upi-split-payments/

│
├── data/
│   ├── users.csv
│   ├── merchants.csv
│   ├── transactions.csv
│   └── split_requests.csv
│
├── scripts/
│   ├── generate_data.py
│   ├── kpi_analysis.py
│   └── business_insights.py
│
├── dashboard/
│   ├── UPI-Splits-Payment.pbix
│
├── docs/
│   ├── PRD.md
│   ├── product_strategy.md
│   └── case_study.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Methodology

### 1. Product Design

Developed a Product Requirements Document defining:

* User personas
* Core pain points
* MVP features
* Success metrics
* Product roadmap

### 2. Synthetic Data Generation

Generated realistic FinTech datasets containing:

* 5,000 users
* 500 merchants
* 50,000 transactions
* 15,000 split-payment requests

### 3. KPI Analysis

Built Python analytics workflows to measure:

* Split Payment Volume
* Settlement Success Rate
* Average Settlement Time
* Average Group Size
* Revenue Potential

### 4. Business Insights

Identified:

* High-performing merchant categories
* Top adoption cities
* Settlement bottlenecks
* User behavior patterns

### 5. Dashboard Development

Developed a four-page Power BI dashboard for executive reporting.

---

## Key Metrics

### North Star Metric

**Monthly Split Payment Volume**

Measures the total value of transactions processed through the Split Payments feature.

### Product Metrics

* Adoption Rate
* Active Users
* Split Transactions per User
* Average Group Size

### Operational Metrics

* Settlement Success Rate
* Average Settlement Time
* Failed Payment Rate

### Financial Metrics

* Merchant Fee Revenue
* Annual Revenue Projection

---

## Power BI Dashboard

### Page 1: Executive Summary

* Total Split Volume
* Active Users
* Settlement Success Rate
* Revenue
* Average Group Size

### Page 2: Transaction Insights

* Merchant Category Analysis
* Split Type Distribution
* Group Size Analysis

### Page 3: Operations Dashboard

* Settlement Status Tracking
* Settlement Time Analysis
* Success Rate Monitoring

### Page 4: Revenue Forecast

* Revenue by Category
* Revenue by City
* Annual Revenue Projection

---

## Key Findings

### Finding 1

Restaurant transactions represent the strongest split-payment use case due to high transaction frequency and naturally shared expenses.

### Finding 2

Equal Split remains the preferred option, indicating user preference for simplicity during checkout.

### Finding 3

Settlement success rates remain consistently high, demonstrating strong feasibility for large-scale deployment.

### Finding 4

Major metropolitan cities drive the majority of adoption, creating opportunities for targeted growth campaigns.

### Finding 5

Merchant fee monetization can generate meaningful revenue while maintaining a low-cost user experience.

---

## Product Recommendations

### Short-Term

* Launch in restaurant and dining categories
* Incentivize first-time split-payment usage
* Improve repayment reminders

### Medium-Term

* Introduce AI-based participant suggestions
* Build recurring shared expense functionality

### Long-Term

* Enable subscription splitting
* Launch Split Pay Later products
* Introduce credit-backed shared payments

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Faker
* Power BI
* Git
* GitHub

---

## Business Impact

This project demonstrates how product strategy, user analytics, and operational insights can be combined to evaluate and launch a scalable FinTech payment feature. The solution provides a framework for measuring adoption, improving settlement efficiency, and unlocking new revenue streams within the UPI ecosystem.
