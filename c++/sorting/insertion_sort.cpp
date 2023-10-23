#include <bits/stdc++.h>
using namespace std;

// TC -> worst - O(N^2) | best - O(N)
void is(int arr[], int n) {
    for(int i=1;i<n;i++) {
        int current=arr[i];
        int j=i-1;
        while(j>=0 && arr[j]>current){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=current;
    }
}


int main() {
    #ifndef ONLINE_JUDGE
	freopen("../build/input.txt", "r", stdin);
	freopen("../build/output.txt", "w", stdout);
	#endif
    int t;
    cin>>t;
    while(t--) {
        int n;
        cin>>n;
        int arr[n];
        for(int i=0; i<n; i++) {
            cin>>arr[i];
        }
        is(arr,n);
        for(int i=0; i<n; i++) {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}