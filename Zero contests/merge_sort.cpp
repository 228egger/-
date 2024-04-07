#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<long int> merge(vector<long int> Left, vector<long int> Right){
    vector<long int> result;
    int i = 0;
    int j = 0;
    while ((i < Left.size()) && (j < Right.size())){
        if (Left[i] > Right[j]){
            result.push_back(Right[j]);
            j++;
        }
        else{
            result.push_back(Left[i]);
            i++;
        }
    }
    while (i < Left.size()){
        result.push_back(Left[i]);
        i++;
    }
    while (j < Right.size()){
        result.push_back(Right[j]);
        j++;
    }
    return result;
}

vector<long int> merge_sort(vector<long int> & arr){
    if (arr.size() < 2){
        return arr;
    }
    int m = int(arr.size() / 2);
    auto start = arr.begin();
    auto end = arr.end();
    vector<long int> L_arg = vector<long int>(start, start + m);
    vector<long int> R_arg = vector<long int>(start + m, end);
    vector<long int> left = merge_sort(L_arg);
    vector<long int> right = merge_sort(R_arg);
    return merge(left, right);
}



int
main(void){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int n;
        cin >> n;
        vector<long int> arg;
        string myString;
        cin.ignore();
        getline(cin, myString);
        stringstream iss(myString);
        long int tmp;
        while ( iss >> tmp ){
            arg.push_back(tmp);
        }
        vector<long int> answer = merge_sort(arg);
        for (int i = 0; i < arg.size(); i++){
            cout << answer[i] << " ";
        }
        cout << endl;
    }
}