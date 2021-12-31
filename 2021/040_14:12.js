function main(input) {
    inputs = input.split(' ');
    n = parseInt(inputs[0]);
    a = parseInt(inputs[1]);
    b = parseInt(inputs[2]);
    if (a > b) {
        console.log(0);
    } elif (a == b) {
        console.log(1);
    } elif (a > b) {
        if (n == 1) 
            console.log(0);
         elif (n == 2) 
            console.log(1);
         elif (n > 3) 
            const mi = a * (n - 1) + b;
            const ma = a + b * (n - 1);
            console.log(ma - mi + 1);
    }
}

main(require('fs').readFileSync('/dev/stdin', 'utf8'));