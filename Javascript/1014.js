//twoSum함수에 숫자배열과 '특정 수'를 인자로 넘기면,
//더해서 '특정 수'가 나오는 index를 배열에 담아 return해 주세요.

const twoSum = (nums, target) => {
    let a = 0;
    let c = 0;
    const b  = target;
    a = nums;
    for(let i=0; i<a.length; i++){
      for(let j=1; j<a.length; j++){
        if (b===(a[i]+a[j])){
          return c=[i,j]
        }
          
      }
    }
  }


twoSum([4,9,11,14],13);