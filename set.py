# I/p x = [5,6,7,2,5,7,3,5,7]
# o/p = [5,6,7,2,3]
#1. make a list
#2.traverse one pointer from 0-index
#3.traverse another pointer from 1-index(run nested loop)
#4.if [i]=[j] push([])
#5.else 
def repeatedElements(arr,X):
    for ele in arr:
        if ele not in X:
            X.append(ele)
    return X


if __name__ == "__main__":
    arr= [5,6,7,2,5,7,3,5,7]
    X = []
    res = repeatedElements(arr,X)
    print(res)

