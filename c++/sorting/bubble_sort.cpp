#include <bits/stdc++.h>
using namespace std;

//  TC -> worst - O(N^2) | best - O(N)
void bs(int arr[], int n){
  for(int i=n-1;i>=1;i--){
    int flag=0;
    for(int j=0;j<i;j++){
      if(arr[j]>arr[j+1]){
        flag=1;
        swap(arr[j],arr[j+1]);
      }
    }
    if(flag==0){
      break;
    }
  }  
}

int main() {
    #ifndef ONLINE_JUDGE
	freopen("build/input.txt", "r", stdin);
	freopen("build/output.txt", "w", stdout);
	#endif
    int t;
    cin>>t;
    while(t--) {
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++) {
            cin>>arr[i];
        }
        bs(arr,n);
        for(int i=0;i<n;i++) {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}