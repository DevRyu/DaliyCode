//최빈값을 정해진 순서대로 답하기
//nums는 숫자로 이루어진 배열입니다.
//가장 자주 등장한 숫자를 k 개수만큼 return해주세요. 
//예)
//nums = [1,1,1,2,2,3]
//k = 2
//return [1,2]
function topK(nums, k) {
    let K = k  
    // 받는배열
    let Nums = nums;
    // 유니크한 배열
    let uniq = Nums.reduce(function(a,b){
        if (a.indexOf(b) < 0 ) a.push(b);
        return a;
    },[]);
    // 유니크 배열 오름차순 정리
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
    let sortedUniqObj = [];
    // 어레이화
    for(let i in uniqObj){
      sortedUniqObj.push([i, uniqObj[i]]);
    }
    // 어레이후 큰 키값별로정렬
    sortedUniqObj.sort(function(a,b){
      return b[1] - a[1];
    });
    let answer= []
    for(let j =0; j<k;j++){
      answer[j] = Number(sortedUniqObj[j][0])
    }
    return(answer)
  }
  // const nums = [3,3,3,2,2,1]
  // const k = 2
  // topK(nums, k);