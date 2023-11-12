---
title: "Actix Web Learning Notes"
date: 2023-11-12T12:06:09-05:00
tags:['rust', 'Actix']
draft: false
---

## Actix Web
### Minimal example
#### Create workspace
```shell
cargo new eztutors
cd eztutors
```
Add the following content to the Cargo.toml file under eztutors.
```toml
[workspace]
members = ["tutor-nodb"]
```
#### Create project
```shell
cargo new tutor-nodb
```

#### Add crates
```shell
cargo add actix-web
cargo add actix-rt
```
The Cargo.toml file contains the following contents:
```toml
[package]
name = "tutor-nodb"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
actix-rt = "2.9.0"
actix-web = "4.4.0"

```
#### Add to main.rs
```rust
use actix_web::{web, App, HttpResponse, HttpServer, Responder};
use std::io;

pub fn general_routes(cfg: &mut web::ServiceConfig) {
    cfg.route("/health", web::get().to(health_check_handler));
}

pub async fn health_check_handler() -> impl Responder {
    HttpResponse::Ok().json("Hello. EzyTutors is alive and kicking")
}

#[actix_rt::main]
async fn main() -> io::Result<()> {
    let app = move || App::new().configure(general_routes);
    HttpServer::new(app).bind("127.0.0.1:3000")?.run().await
}
```

#### Run
```shell
cargo run
```

#### Verify the result
Open the browser with http://127.0.0.1:3000/health and you will be able to see "Hello. EzyTutors is alive and kicking".

#### Add multiple `main.rs` to the project
* Add the following content to `Cargo.toml` under eztutor-nodb. 
```toml
[[bin]]
name = "basic-server"
```
* Rename the main.rs to basic-server.rs and move it to `src/bin`.
* If you are the root folder of tutor-nodb, run it with the following command:  
```shell
cargo run --bin basic-server
```
If you are under the workspace root folder, run it with the following command:
```shell
cargo run -p tutor-nodb --bin basic-server
```

### Example with Service
#### Update tutor-nodb project
* Add the following content to `Cargo.toml` in **tutor-nodb**
```toml
default-run="tutor-service"

[[bin]]
name = "tutor-service"
```
* add the following files to **tutor-nodb**
    * bin/tutor-service.rs
    * models,rs 
    * state.rs 
    * routes.rs 
    * handlers.rs

And add the following content to the files. 
state.rs
```rust
use std::sync::Mutex;

pub struct AppState {
    pub health_check_response: String, // Shared immutable state
    pub visit_count: Mutex<u32>, // Shared mutable state
}
```

routes.rs
```rust
use super::handlers::*;
use actix_web::web;

pub fn general_routes(cfg: &mut web::ServiceConfig) {
    cfg.route("/health", web::get().to(health_check_handler));
}
```

handlers.rs
```rust
use super::state::AppState;
use actix_web::{web, HttpResponse};

pub async fn health_check_handler(app_state: web::Data<AppState>) -> HttpResponse {
    let health_check_response = &app_state.health_check_response;
    let mut visit_count = app_state.visit_count.lock().unwrap();
    let response = format!("{} {} times", health_check_response, visit_count);
    *visit_count += 1;
    HttpResponse::Ok().json(&response)
}
```

bin/tutor-service.rs
```rust
use actix_web::{web, App, HttpServer};
use std::io;
use std::sync::Mutex;

#[path = "../handlers.rs"]
mod handlers;
#[path = "../routes.rs"]
mod routes;
#[path = "../state.rs"]
mod state;

use routes::*;
use state::AppState;

#[actix_rt::main]
async fn main() -> io::Result<()> {
    let shared_data = web::Data::new(AppState {
        health_check_response: "I'm good. You've already asked me ".to_string(),
        visit_count: Mutex::new(0),
    });
    
    let app = move || {
        App::new()
            .app_data(shared_data.clone())
            .configure(general_routes) // no ; should be added. 
    };

    HttpServer::new(app).bind("127.0.0.1:3000")?.run().await
}
```

Run it with `cargo run`. You will able to see the **"I'm good. You've already asked me  14 times"**

#### Add data models
* Add the `serde` and `chrono` crates. 
```toml
chrono = { version = "0.4.31", features = ["serde"] }
serde = { version = "1.0.192", features = ["derive"] }
```
* Add the following content to `models.rs`.
```rust
use actix_web::web;
use chrono::NaiveDateTime;
use serde::{Serialize, Deserialize};

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Course {
    pub tutor_id: i32,
    pub course_id: Option<i32>,
    pub course_name: String,
    pub posted_time: Option<NaiveDateTime>,
}
impl From<web::Json<Course>> for Course {
    fn from(course: web::Json<Course>) -> Self {
        Course {
            tutor_id: course.tutor_id,
            course_id: course.course_id,
            course_name: course.course_name.clone(),
            posted_time: course.posted_time,
        }
    }
}
```
* Add `pub courses: Mutex<Vec<Course>>,` as a part of `AppState`. 
* Add the following content to tutor-service.rs
```rust
#[path = "../models.rs"]
mod models;
```
and 
```rust
        courses: Mutex::new(vec![]),
```
to `shared_data`.

#### Post courses
* Add the following content to `routes.rs`
```rust
pub fn course_routes(cfg: &mut web::ServiceConfig) {
    cfg.service(web::scope("/courses"))
        .route("/", web::post().to(new_course))
        .route("/{tutor_id}", web::get().to(get_courses_for_tutor))
        .route("/{tutor_id}/{course_id}", web::get().to(get_courses_detail));
}
```

* Add an extra path th main() function
```rust
            .configure(course_routes) // no ; should be added. 
```

* Update the handlers.rs
```rust
use super::models::Course;
use actix_web::{web, HttpResponse};

pub async fn new_course(
    new_course: web::Json<Course>,
    app_state: web::Data<AppState>
) -> HttpResponse {
    println!("Received new course");
    let course_count_for_user = app_state
        .courses
        .lock()
        .unwrap()
        .clone()
        .into_iter()
        .filter(|course| course.tutor_id == new_course.tutor_id)
        .count();
    let new_course = Course {
        tutor_id: new_course.tutor_id,
        course_id: Some(course_count_for_user as i32 + 1),
        course_name: new_course.course_name.clone(),
        posted_time: Some(Utc::now().naive_utc()),
    };
    app_state.courses.lock().unwrap().push(new_course);
    HttpResponse::Ok().json("Added course")
}

pub async fn get_courses_for_tutor(
    app_state: web::Data<AppState>,
    params: web::Path<i32>,
) -> HttpResponse {
    let tutor_id: i32 = params.into_inner();

    let filtered_courses = app_state
        .courses
        .lock()
        .unwrap()
        .clone()
        .into_iter()
        .filter(|course| course.tutor_id == tutor_id)
        .collect::<Vec<Course>>();

    if filtered_courses.len() > 0 {
        HttpResponse::Ok().json(filtered_courses)
    } else {
        HttpResponse::Ok().json("No courses found for tutor".to_string())
    }
}

pub async fn get_courses_detail(
    app_state: web::Data<AppState>,
    params: web::Path<(i32, i32)>,
) -> HttpResponse {
    let (tutor_id, course_id) = params.into_inner();

    let selected_course = app_state
        .courses
        .lock()
        .unwrap()
        .clone()
        .into_iter()
        .find(|course| course.tutor_id == tutor_id && course.course_id == Some(course_id))
        .ok_or("Course not found");

    if let Ok(course) = selected_course {
        HttpResponse::Ok().json(course)
    } else {
        HttpResponse::Ok().json("Course not found".to_string())
    }
}

mod tests {
    use super::*;
    use actix_web::http::StatusCode;
    use std::sync::Mutex;

    #[actix_rt::test]
    async fn post_course_test() {
        let course = web::Json(Course {
            tutor_id: 1,
            course_name: "Hello, this is a test course".into(),
            course_id: None,
            posted_time: None,
        });
        let app_state: web::Data<AppState> = web::Data::new(AppState { 
            health_check_response: "".to_string(), 
            visit_count: Mutex::new(0), 
            courses: Mutex::new(vec![]) 
        });
        let resp = new_course(course, app_state).await;
        assert_eq!(resp.status(), StatusCode::OK);
    }

    #[actix_rt::test]
    async fn get_all_courses_success() {
        let app_state: web::Data<AppState> = web::Data::new(AppState { 
            health_check_response: "".to_string(), 
            visit_count: Mutex::new(0), 
            courses: Mutex::new(vec![]) 
        });
        let tutor_id: web::Path<i32> = web::Path::from(1);
        let resp = get_courses_for_tutor(app_state, tutor_id).await;
        assert_eq!(resp.status(), StatusCode::OK);
    }

    #[actix_rt::test]
    async fn get_one_course_success() {
        let app_state: web::Data<AppState> = web::Data::new(AppState { 
            health_check_response: "".to_string(), 
            visit_count: Mutex::new(0), 
            courses: Mutex::new(vec![]) 
        });
        let params: web::Path<(i32, i32)> = web::Path::from((1, 1));
        let resp = get_courses_detail(app_state, params).await;
        assert_eq!(resp.status(), StatusCode::OK);
    }
}
```