function moreThanHalf(nums) {
    // 받는배열
    let Nums = nums;
    // 유니크한 배열
    let uniq = Nums.reduce(function(a,b){
        if (a.indexOf(b) < 0 ) a.push(b);
        return a;
    },[]);
    // 유니크 배열 오름차순 정리
    uniq.sort()
    // 키와 벨류 초기값 선언
    let result = 0;
    let max = -1
    // 키값만 가지고 벨류는 빈값으로 가지는 오브젝트
    let uniqObj =  uniq.reduce((a,b)=> (a[b]=0,a),{});
  
  
    // 각 키값별로 값이 여러개인 경우 1을 값에 더해준다
    for(let i = 0;i<Nums.length;i++ ){
      for(let j = 0; j<uniq.length;j++){
        if(Nums[i] === uniq[j]){
          uniqObj[Nums[i]] += 1
        }
      }
    }
    
    //키별로 벨류를 초기max 값과 비교해서 result에 키값을 저장
    for(let k in uniqObj){
      if (uniqObj[k] > max){
        max = uniqObj[k]
        result = k
      }
    }
    // 키는 문자열이므로 숫자로 변환
    return Number(result)
  }