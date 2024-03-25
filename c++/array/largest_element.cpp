#include <bits/stdc++.h>
using namespace std;
void largestElement(vector<int>& arr,int n){
    int sol=arr[0];
    for(int i=1;i<n;i++){
        if(arr[i]>sol) sol=arr[i];
    }
    cout<<"Largest element : "<<sol;
}
int main(){
    int n;
    cout<<"Enter size of array : ";
    cin>>n;
    vector<int> arr(n);
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    largestElement(arr,n);
}