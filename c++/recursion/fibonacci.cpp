#include <bits/stdc++.h>
using namespace std;

int fib(int n) {
    if(n==0 || n==1) return n;
    return fib(n-1)+fib(n-2);
}

int main() {
    #ifndef ONLINE_JUDGE
	freopen("build/input.txt", "r", stdin);
	freopen("build/output.txt", "w", stdout);
	#endif
    int n;
    cin>>n;
    int res=fib(n);
    cout<<res;
    return 0;
}