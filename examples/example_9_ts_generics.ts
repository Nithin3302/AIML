// TS: generics example
function wrap<T>(v:T){return {v}}
console.log(wrap<number>(123))
