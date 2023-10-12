//problem statement: https://practice.geeksforgeeks.org/problems/nth-fibonacci-number1335/1?page=1&sortBy=submissions

#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
        int nthFibonacci(int n){
            const int mod=1000000007; //ensures that the result lies in range (till 1000000006) 
            int a=0, b=1;
            int temp;
            for(int i=2;i<=n;i++){
                temp=(a+b)%mod;
                a=b;
                b=temp;
            }
            return temp;
        }
};

int main(){
    int n;
    cin>>n;
    Solution solution;
    int result=solution.nthFibonacci(n);
    cout<<result;
}

