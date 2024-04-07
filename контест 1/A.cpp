#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int
main(void){
    int n;
    cin >> n;
    double left_1 = numeric_limits<double>::infinity();
    double right_1 = -numeric_limits<double>::infinity();
    double left_2 = numeric_limits<double>::infinity();
    double right_2 = -numeric_limits<double>::infinity();
    double highest_right = -numeric_limits<double>::infinity();
    double highest_left = -numeric_limits<double>::infinity();
    for (int i = 0; i < n; i++){
        string myString;
        cin.ignore();
        getline(cin, myString);
        stringstream iss(myString);
        double tmp;
        vector<double> arg;
        while ( iss >> tmp ){
            arg.push_back(tmp);
        }
        if (abs(arg[1]) > 0 && (arg[0] > 0)){
            highest_right = max(highest_right, abs(arg[1]));
            cout << arg[1] << arg[0] << endl;
        }
        else if (abs(arg[1]) > 0 && (arg[0] < 0)){
            highest_left = max(highest_left, abs(arg[1]));
            cout << 1;
        }
        if ((arg[1] == 0) && (arg[0] > 0)){
            if (arg[0] < left_1){
                if (left_1 != numeric_limits<double>::infinity()){
                    right_1 = max(left_1, right_1);
                }
                left_1 = arg[0];
            }
            else if (arg[0] > right_1){
                if (right_1 != -numeric_limits<double>::infinity()){
                    left_1 = min(left_1, right_1);
                }
                right_1 = arg[0];
            }
        }
        if ((arg[1] == 0) && (arg[0] < 0)){
            if (arg[0] > left_2){
                if (left_2 != -numeric_limits<double>::infinity()){
                    right_2 = max(left_2, right_2);
                }
                left_2 = arg[0];
            }
            else if (arg[0] < right_2){
                if (right_2 != numeric_limits<double>::infinity()){
                    left_2 = min(left_2, right_2);
                }
                right_2 = arg[0];
            }
        }
    }
    double s_1 = abs((right_1 - left_1) * highest_right / 2);
    double s_2 =  abs((right_2 - left_2) * highest_left / 2);
    if (max(s_1, s_2) != numeric_limits<double>::infinity()){
        cout << max(s_1, s_2) << endl;;
    }
    else if (min(s_1, s_2) != numeric_limits<double>::infinity()){
        cout << min(s_1, s_2) << endl;;
    }
    else{
        cout << 0 << endl;;
    }
    cout << right_2 << left_2 << highest_left << endl;
}