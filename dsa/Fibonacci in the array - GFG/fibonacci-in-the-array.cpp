//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	public:
	int checkFib(long long arr[], int N)
	{
	    int max=0;
	    for(int i=0;i<N;i++){
	        if(max>arr[i]) max=arr[i];
	    }
	    const int mod=1000000007;
	    int a=0,b=1;
	    int temp=0;
	    unordered_set<int> set;
	    for(int j=2;j<=1000;j++){
	        temp=(a+b)%mod;
	        set.insert(temp);
	        a=b;
	        b=temp;
	    }
	    set.insert(0);
	    int count=0;
	    for(const int& element : set){
	        for(int k=0;k<N;k++){
	            if(element==arr[k]) count++;
	        }
	    }
	    return count;
	}
};
	

//{ Driver Code Starts.



int main() 
{
   	
   	int t;
    cin >> t;
    while (t--)
    {
    	int n;
       	
		cin>>n;
		long long a[n];
		for(int i=0;i<n;++i)
			cin>>a[i];
        

        Solution ob;
        cout << ob.checkFib(a, n);
	    cout << "\n";
	     
    }
    return 0;
}

	
// } Driver Code Ends