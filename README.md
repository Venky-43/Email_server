# 📧 Serverless Email API

This project is a simple **Serverless REST API** using **Node.js, AWS Lambda, and the Serverless Framework**, that allows you to send emails by making a POST request with the recipient's email, subject, and body content.

---

## 🚀 Features

- Send emails using Gmail SMTP
- Built with Node.js and Serverless Framework
- Runs locally with `serverless-offline`
- Deployed to AWS Lambda & API Gateway
- Secure credentials with `.env` (for local use) or environment variables (for AWS)

---

## 📦 Tech Stack

- Node.js
- Serverless Framework (v3)
- AWS Lambda
- AWS API Gateway
- Nodemailer
- dotenv (for local testing)

---

## 📁 Folder Structure

email/
├── handler.js
├── serverless.yml
├── .env # (local use only)
├── .gitignore
└── package.json

## Install Dependencies

npm install

 ## Create .env File (Local Only)

 SENDER_EMAIL=yourgmail@gmail.com
 SENDER_PASS=yourapppassword

 ## ▶️ Run Locally

 serverless offline

## Test with Postman

URL: http://localhost:Port_number/dev/send

Method: POST

Headers: Content-Type: application/json

Body (raw, JSON):
{
  "receiver_email": "your_Choice@example.com",
  "subject": "Hello from Serverless!",
  "body_text": "This email was sent from a local Serverless API."
}

## 📬 Example Response

{
  "message": "Email sent successfully"
}

## 📜 License

This project is open-source and available for educational and demo use.

## 🙋‍♂️ Author

Venkannababu Kothapalli

GitHub: https://github.com/Venky-43


