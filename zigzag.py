# zigzag algorithm

def solution(list_):
    rows=len(list_)
    columns=len(list_[0])
    solution=[[] for i in range(rows+columns-1)] 
    
    for i in range(rows): 
        for j in range(columns): 
            sum=i+j 
            if(sum%2 ==0): 
                solution[sum].insert(0,list_[i][j]) 
            else: 
                solution[sum].append(list_[i][j])
    for i in solution: 
        for j in i: 
            print(j,end=" ")         

if __name__ == "__main__":
    list_ = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
    solution(list_)


