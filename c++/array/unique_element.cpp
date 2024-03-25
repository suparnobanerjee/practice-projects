#include<bits/stdc++.h>
using namespace std;

// Assuming array is already sorted
// Use of 2 pointers

int removeDuplicates(vector<int> &arr, int n) {
	int i=0;
	for(int j=1;j<n;j++){
		if(arr[i]!=arr[j]){
			i++;
			arr[i]=arr[j];
		}
	}
	return i+1;
}
int main(){
    int n;
    cout<<"Enter size of array : "<<endl;
    cin>>n;
    cout<<"Enter elements of array : "<<endl;
    vector<int> arr(n);
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
    int sol;
    sol=removeDuplicates(arr,n);
    cout<<"Number of unique elements : "<<sol<<endl;
}