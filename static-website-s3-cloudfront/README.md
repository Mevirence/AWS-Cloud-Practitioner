
## 🧰 How It Works

1. **HTML/CSS files** are uploaded to an S3 bucket
2. The bucket is configured for **static website hosting**
3. Public read access is allowed via **bucket policy**
4. A **CloudFront distribution** is created to use the S3 bucket as its origin
5. Website is accessible globally via the **d3pefn3eqjkrfg.cloudfront.net**

## 🔐 S3 Bucket Policy (for public access)

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::demo-cloudfront-mevi-v4/*"
        }
    ]
}

