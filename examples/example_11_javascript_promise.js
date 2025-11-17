// JavaScript: promises/async example
function delay(ms){return new Promise(r=>setTimeout(r,ms));}
async function run(){
  await delay(300);
  console.log("Async example done");
}
run();
