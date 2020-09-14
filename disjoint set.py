class disjoint_set:
    def __init__(self,num):

        self.array=[0]+[[i,0] for i in range(1,num+1)]  # our set
    
    def union(self,a,b):
        
        ''' a and b are the vertices that we want to connect them to each other '''
        
        a=self.find(a) # finds the ancestor of a
        b=self.find(b) # finds the ancestor of b
    
        if a==b:
            # if the ancestors of a and b are the same , do nothing
            return False
    

        # connecting two graph components to each other

        if self.array[a][1] > self.array[b][1] :
            self.array[b][0]=a
        
        elif self.array[a][1] < self.array[b][1] :
            self.array[a][0]=b

        else:
            self.array[a][0]=b
            self.array[b][1]+=1
        return True
            
    def find(self,a):
        p=[]
        while self.array[a][0]!=a :
            p.append(a)
            a=self.array[a][0]
        for i in p:
            self.array[i][0]=a
        return a
        
// c++ impelemenation
#include <bits/stdc++.h>
using namespace std;
#define long long ll

class disjoint_set
{
private:
    int num;
    vector<pair<int, int>> arr;

public:
    disjoint_set(int n)
    {
        num = n;
        for (int i = 1; i < n + 1; i++)
        {
            arr.push_back({i, 0});
        }
    }

    int find(int a)
    {
        vector<int> p;
        while (arr[a].first != a)
        {
            p.push_back(a);
            a = arr[a].first;
        }
        for (auto i : p)
        {
            arr[i].first = a;
        }
        return a;
    }

    bool _union_(int a, int b)
    {
        a = find(a);
        b = find(b);
        if (a == b)
        {
            return 0;
        }

        if (arr[a].second > arr[b].second)
        {
            arr[b].second = a;
        }
        else if (arr[a].second < arr[b].second)
        {
            arr[a].first = b;
        }
        else
        {
            arr[a].first = b;
            arr[b].second++;
        }
    }
};
