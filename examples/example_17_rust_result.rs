// Rust: Result example
use std::fs;
fn main(){
  match fs::read_to_string("Cargo.toml"){
    Ok(c)=>println!("Read {} bytes",c.len()),
    Err(e)=>println!("Err {e}")
  }
}
