//problem statement: https://practice.geeksforgeeks.org/problems/nth-fibonacci-number1335/1?page=1&sortBy=submissions

#include <iostream>
using namespace std;

class Solution{
    public:
        int nthFibonacci(int n){
            int arr[1000];
            arr[0]=0;
            arr[1]=1;
            for(int i=2;i<=n;i++){
                arr[i]=arr[i-1]+arr[i-2];
            }
            return arr[n];
        }
};

int main(){
    int n;
    cin>>n;
    Solution solution;
    int result=solution.nthFibonacci(n);
    cout<<result;
}

