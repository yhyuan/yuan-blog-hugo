---
title: "Create Rust Aws Lambda"
date: 2023-11-06T13:30:29-05:00
draft: false
tags: ['rust', 'AWS', 'lambda']
---

Here is the notes for learning [this tutorial](https://blog.scanner.dev/getting-started-with-serverless-rust-in-aws-lambda/)
## Install brew on Ubuntu
```
curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
```

run two commands.
```
Output
==> Next steps:
- Run these two commands in your terminal to add Homebrew to your PATH:
    echo 'eval "$(/home/sammy/.linuxbrew/bin/brew shellenv)"' >> /home/sammy/.profile
    eval "$(/home/sammy/.linuxbrew/bin/brew shellenv)"
```
## Install cargo-lambda with brew
```
brew tap cargo-lambda/cargo-lambda
brew install cargo-lambda
```
## Create a project
```
cargo lambda new rust-lambda-s3-test
```
## Update the code
```
#[derive(Deserialize)]
struct Request {
    bucket: String,
    key: String,
}
```

Cargo.toml
```
[dependencies]

anyhow = "1"
async-compression = { version = "0.3", features = ["tokio", "zstd"] }
lambda_runtime = "0.7"
rusoto_core = { version = "0.48", default_features = false, features = ["rustls"] }
rusoto_s3 = { version = "0.48", default_features = false, features = ["rustls"] }
serde = "1.0.136"
serde_json = "1"
tokio = { version = "1", features = ["macros"] }
tracing = { version = "0.1", features = ["log"] }
tracing-subscriber = { version = "0.3", default-features = false, features = ["fmt"] }
```

```
use rusoto_core::Region;
use rusoto_s3::{S3Client, S3};
use tokio::io::AsyncBufReadExt;
```

```
async fn function_handler(event: LambdaEvent<Request>) -> Result<Response, Error> {
    let bucket = &event.payload.bucket;
    let key = &event.payload.key;

    let started_at = std::time::Instant::now();

    // Customize with the region of your actual S3 bucket.
    let client = S3Client::new(Region::UsWest2);

    // Initiate a GetObject request to S3.
    let output = client
        .get_object(rusoto_s3::GetObjectRequest {
            bucket: bucket.to_string(),
            key: key.to_string(),
            ..Default::default()
        })
        .await?;

    let Some(body) = output.body else {
        return Err(anyhow::anyhow!("No body found in S3 response").into());
    };

    // Begin streaming the contents down, decompressing on the fly, and
    // iterating over each chunk split by newlines.
    let body = body.into_async_read();
    let body = tokio::io::BufReader::new(body);
    let decoder = async_compression::tokio::bufread::ZstdDecoder::new(body);
    let reader = tokio::io::BufReader::new(decoder);
    let mut lines = reader.lines();

    // For each line we encounter while asynchronously streaming down the
    // S3 data, parse the JSON object.
    let mut num_log_events = 0;
    while let Some(line) = lines.next_line().await? {
        let _value: serde_json::Value = serde_json::from_str(&line)?;
        num_log_events += 1;
        if num_log_events % 1000 == 0 {
            println!("num_log_events={}", num_log_events);
        }
    }

    let msg = format!(
        "elapsed={:?} num_log_events={}",
        started_at.elapsed(),
        num_log_events
    );

    let resp = Response {
        req_id: event.context.request_id,
        msg,
    };

    Ok(resp)
}
```

## Deploy
```
cargo lambda build --release --arm64
```
```
cargo lambda deploy \
--profile dev \
--region us-west-2 \
--timeout 45 \
rust-lambda-s3-test
```