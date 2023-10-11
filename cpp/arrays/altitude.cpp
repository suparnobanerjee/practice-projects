//problem statement : https://leetcode.com/problems/find-the-highest-altitude/

#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int current_alt = 0;
        int max_alt = 0;
        for (const int& alt_gain : gain) {
            current_alt += alt_gain;
            max_alt = max(current_alt, max_alt);
        }
        return max_alt;
    }
};

int main() {
    int n;
    cout << "Enter the number of altitudes: ";
    cin >> n;

    vector<int> gain(n);
    cout << "Enter the altitude gains:" << endl;
    for (int i = 0; i < n; ++i) {
        cin >> gain[i];
    }

    Solution solution;
    int result = solution.largestAltitude(gain);
    cout << "The highest altitude is: " << result << endl;

    return 0;
}
