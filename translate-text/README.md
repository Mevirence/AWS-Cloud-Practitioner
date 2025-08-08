# Translate Text API with AWS Translate

## 📌 Overview
A simple serverless translation API that takes text input and returns the translated text in the target language.  
Built with:
- **AWS Lambda** (Python)
- **Amazon Translate**
- **Amazon API Gateway (HTTP API)**

---

## 🛠️ Architecture
1. **API Gateway** receives HTTP POST requests.
2. **Lambda Function** processes the request and calls **Amazon Translate**.
3. The translated text is returned as a JSON response.

---

## 🚀 Steps to Deploy

### 1 — Create the Lambda Function
- Runtime: Python 3.x
- Code: [`lambda_function.py`](lambda_function.py)
- IAM Role: Must have `translate:TranslateText` permission.

### 2 — Create an HTTP API in API Gateway
- Create API → HTTP API
- Integration → Lambda → select your Lambda function.
- Route: `POST /translate`
- Enable **CORS** if needed.

### 3 — Test with `curl`
```bash
curl -X POST "https://h5j8t2ipp4.execute-api.ap-southeast-1.amazonaws.com/translate" \
  -H "Content-Type: application/json" \
  -d '{"text":"Nice to meet you","target":"es"}'

