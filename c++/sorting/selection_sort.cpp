#include <bits/stdc++.h>
using namespace std;

//  TC -> worst - O(N^2) | best - O(N^2)
void ss(int arr[], int n) {
    for(int i=0;i<n-1;i++){
        int min=i;
        for(int j=i+1;j<n;j++){
            if(arr[j]<arr[i]){
                min=j;
            }
        }
        if(min!=i){
            swap(arr[i],arr[min]);
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
        for(int i=0; i<n; i++) {
            cin>>arr[i];
        }
        ss(arr,n);
        for(int i=0; i<n; i++) {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}