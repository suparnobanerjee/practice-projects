#include <bits/stdc++.h>
using namespace std;

int secondLargest(vector<int> a, int n){
    int max=a[0];
    int smax=INT_MIN;
    for(int i=1;i<n;i++){
        if(a[i]>max){
            smax=max;
            max=a[i];
        } else if(a[i]<max && a[i]>smax){
            smax=a[i];
        }
    }
    return smax;
}
int secondSmallest(vector<int> a, int n){
    int min=a[0];
    int smin=INT_MAX;
    for(int i=1;i<n;i++){
        if(a[i]<min){
            smin=min;
            min=a[i];
        } else if(a[i]>min && a[i]<smin){
            smin=a[i];
        }
    }
    return smin;
}

vector<int> getSecondOrderElements(int n, vector<int> a) {
    int slargest=secondLargest(a,n);
    int ssmallest=secondSmallest(a,n);
    return {slargest,ssmallest};
}
int main(){
    int n;
    cout<<"Enter size of array : "<<endl;
    cin>>n;
    vector<int> arr(n);
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    vector<int> sol(2);
    sol = getSecondOrderElements(n,arr);
    cout<<"Second Largest : "<<sol[0]<<endl;
    cout<<"Second Smallest : "<<sol[1]<<endl;
}