/*
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
*/


function sumGame(list, k){
  for(var i = 0; i<list.length; i++){
    for(var j = i+1; j<list.length;j++){
     if(list[i]+list[j]===k){
       console.log(`${list[i]}` + '+' + `${list[j]}`) // prints # + #
       return true; 
       break;
     } 
      else if(i == list.length-2 && j == list.length-1){
      // if on last pair of matches, print, no match
        console.log('no match') 
      }
      else{
      // not matches but not the last term
      // console.log('just passing by')
      }
    }
  }
}

//sumGame([10,6,0,4,15,3,7],17)
//sumGame([2,4,6,7],100)
//console.log(sumGame([1,2,3,4],100))
