#include<bits/stdc++.h>
using namespace std;

int main(){

    vector<int> nums = {1,3,4,2,2};
    vector<int> v;

    // vector<int>::iterator it;

    // for(it = nums.begin(); it < nums.end(); it++){
    //     v.push_back(it);
    // }

    copy(nums.begin(), nums.end(), v.begin());

    sort(v.begin(), v.end());

    for(auto i:v){
        cout << i << " ";
    }

}