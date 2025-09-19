# Serverless REST API with AWS Lambda, API Gateway, and DynamoDB

## 📌 Overview
This project demonstrates how to build a **serverless REST API** on AWS that goes beyond the usual stateless ‘Hello World’ examples. It integrates with **DynamoDB** to provide **persistence**, showing how serverless can handle real-world use cases.

The API provides two endpoints:
- `POST /message` → Save a message to DynamoDB.
- `GET /message` → Retrieve the latest saved message.

Unlike many serverless demos, this project solves a **gap**: proving that serverless isn’t limited to stateless responses. By adding DynamoDB, it demonstrates **state management and persistence** — a critical requirement for real-world applications.

---

## 🎯 Objectives
- Build a **serverless REST API** using AWS services.
- Implement **message persistence** with DynamoDB.
- Expose endpoints through API Gateway for external access.
- Demonstrate how serverless apps can move from **toy demos** to **real-world solutions**.

---

## ⚙️ Tech Stack
- **AWS Lambda** – backend compute layer.
- **Amazon API Gateway** – API endpoint management.
- **Amazon DynamoDB** – NoSQL database for persistence.
- **Python 3.9** – Lambda runtime.
- **AWS Management Console** – setup and configuration.
