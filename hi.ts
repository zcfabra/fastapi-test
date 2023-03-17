

type Test ={
    name: string,
    age: number
}


// confirming that supersets are fine in TS 
const hi={ name:"Dave", age: 9000000, enjoys: "Nothing"} as Test;
console.log(hi);