---
title: "Use Python and Rust to Create Http Requests Without AWS SDK"
date: 2023-12-23T09:43:57-05:00
tags: ['Python', 'Rust', 'AWS']
draft: false
---

I used ChatGPT to create a Python client to access the AWS API without AWS SDK. 
```python
import requests
import datetime
import hashlib
import hmac
import base64

def aws_api_request(access_key, secret_key, region, service, endpoint, http_method='GET', payload='', headers=None, params=None):
    # Define the AWS service endpoint
    url = f'https://{endpoint}'

    # Set up the timestamp for the request
    amz_date = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    date_stamp = datetime.datetime.utcnow().strftime('%Y%m%d')  # Datestamp for Credential Scope
    
    payload_hash = hashlib.sha256(payload.encode()).hexdigest()
    headers['x-amz-content-sha256'] = payload_hash

    # Create the canonical request
    canonical_uri = '/'
    canonical_querystring = '&'.join([f'{key}={value}' for key, value in params.items()]) if params else ''
    canonical_headers = f'host:{endpoint}\nx-amz-date:{amz_date}\n'
    signed_headers = 'host;x-amz-date'
    canonical_request = f'{http_method}\n{canonical_uri}\n{canonical_querystring}\n{canonical_headers}\n{signed_headers}\n{hashlib.sha256(payload.encode()).hexdigest()}'

    # Create the string to sign
    credential_scope = f'{date_stamp}/{region}/{service}/aws4_request'
    string_to_sign = f'AWS4-HMAC-SHA256\n{amz_date}\n{credential_scope}\n{hashlib.sha256(canonical_request.encode()).hexdigest()}'

    # Calculate the signature
    signing_key = get_signature_key(secret_key, date_stamp, region, service)
    signature = hmac.new(signing_key, (string_to_sign).encode(), hashlib.sha256).hexdigest()

    # Add the signature to the headers
    headers['Authorization'] = f'AWS4-HMAC-SHA256 Credential={access_key}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}'
    headers['x-amz-date'] = amz_date

    # Make the HTTP request
    response = requests.request(http_method, url, headers=headers, params=params, data=payload)

    return response

def get_signature_key(key, date_stamp, region_name, service_name):
    k_date = hmac.new(('AWS4' + key).encode(), date_stamp.encode(), hashlib.sha256).digest()
    k_region = hmac.new(k_date, region_name.encode(), hashlib.sha256).digest()
    k_service = hmac.new(k_region, service_name.encode(), hashlib.sha256).digest()
    k_signing = hmac.new(k_service, b'aws4_request', hashlib.sha256).digest()
    return k_signing

# Example usage
access_key = ''
secret_key = ''
region = 'us-east-1'
service = 's3'
endpoint = 's3.amazonaws.com'
bucket_name = 'bucket_name'

headers = {'Host': endpoint}
params = {'bucket': bucket_name}

response = aws_api_request(access_key, secret_key, region, service, endpoint, http_method='GET', headers=headers, params=params)

print(response.status_code)
print(response.text)

```

Accessing AWS APIs directly without using the AWS SDK in Rust involves crafting HTTP requests and handling AWS authentication manually. Here's a basic example using the reqwest crate for HTTP requests and the aws_sigv4 crate for AWS Signature Version 4 signing:

First, add these dependencies to your Cargo.toml file:

```toml
[dependencies]
reqwest = { version = "0.11", features = ["blocking", "json"] }
aws-sigv4 = "0.17.1"
```
Now, you can use the following code as a starting point for a Rust client to access an AWS API. This example assumes you want to make a simple request to an AWS service like S3:

```rust
use reqwest;
use aws_sigv4::{sign, Credentials, Region, Service};

fn main() {
    // AWS credentials
    let access_key = "YOUR_ACCESS_KEY";
    let secret_key = "YOUR_SECRET_KEY";
    let region = Region::new("us-east-1");
    let service = Service::new("s3");

    // AWS service endpoint
    let endpoint = "https://s3.amazonaws.com";
    let uri = "/your-bucket/your-object";

    // HTTP method and payload (if any)
    let http_method = reqwest::Method::GET;
    let payload = "".to_owned();

    // Generate the AWS SigV4 signed request
    let signed_request = sign(
        &access_key,
        &secret_key,
        &region,
        &service,
        &http_method,
        &uri,
        &endpoint,
        &payload,
    );

    // Make the HTTP request using reqwest
    match reqwest::blocking::Client::new()
        .request(http_method, &format!("{}{}", endpoint, uri))
        .header("Authorization", signed_request.authorization_header())
        .header("x-amz-date", signed_request.datetime())
        .header("x-amz-content-sha256", signed_request.payload_hash())
        .body(payload)
        .send()
    {
        Ok(response) => {
            // Handle the response here
            println!("Status: {}", response.status());
            println!("Headers:\n{:#?}", response.headers());
            println!("Body:\n{}", response.text().unwrap());
        }
        Err(err) => {
            // Handle errors
            eprintln!("Error: {}", err);
        }
    }
}
```

Make sure to replace YOUR_ACCESS_KEY, YOUR_SECRET_KEY, /your-bucket/your-object, and adjust the AWS service endpoint and other details based on your use case.

This is a basic example, and in a production environment, you should handle errors, retries, and security considerations more robustly. Additionally, for more complex AWS APIs, you may need to include specific headers or follow certain conventions depending on the service you're interacting with. Always refer to the AWS service documentation for the API details you need to follow.
