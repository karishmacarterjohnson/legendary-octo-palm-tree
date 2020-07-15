/* Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

*/



function productGame(list){
var products = [];

  for (var i = 0; i < list.length; i++){
    // loop through each item in array
    var prod = 1;
    for(var j = 0; j <list.length; j++){
      if(j!== i){
        // for each item loop, multiply all terms that arent of index i
        prod*= list[j];
      }
      else{
        // when looking at indexed term, do nothing
      }
       }
  products.push(prod); 
  // push product into array
   }
  console.log(products)
  return products;
}


// test outcome
productGame([1,2,3,4,5])
