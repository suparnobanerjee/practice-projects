#include <iostream>
using namespace std;

void selection_sort(int arr[], int n){
  for(int i=0;i<n-1;i++){
    int index=i;
    for(int j=i;j<n;j++){
      if(arr[j]<arr[index]) index=j;
    }
    int temp=arr[i];
    arr[i]=arr[index];
    arr[index]=temp;
  }
}

int main(){
  int n;
  cout<<"Enter size : "<<endl;
  cin>>n;
  int arr[n];
  cout<<"Enter elements : "<<endl;
  for(int i=0; i<n; i++){
    cin>>arr[i];
  }
  cout<<"Unordered array : "<<endl;
  for(int i=0; i<n; i++){
    cout<<arr[i]<<" ";
  }
  selection_sort(arr, n);
  cout<<"\nOrdered array : "<<endl;
  for(int i=0; i<n; i++){
    cout<<arr[i]<<" ";
  }
  return 0;
}
