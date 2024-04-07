#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;
void insert(vector<int> &arr,int value)
{
    int low = 0;
    int high = (int)(arr.size() - 1);
    int mid = low+(high - low)/2;
    int indexToInsert = -1;
    while(low<=high)
    {
        if(mid < 0 || mid > arr.size()-1)
            break;
        if(value < arr[mid])
        {
            //check if previous index is valid and lesser than value
            if(mid-1 >= 0)
            {
                if(arr[mid-1]<value)
                {
                    indexToInsert = mid;
                    break;
                }
            }
            high = mid - 1;
        }
        else if(value > arr[mid])
        {
            //check if next index is valid and greater than value
            if(mid+1 < arr.size())
            {
                if(arr[mid+1]>value)
                {
                    indexToInsert = mid+1;
                    break;
                }
            }
            low = mid + 1;
        }
        mid = low+(high - low)/2;
    }
    if(indexToInsert == -1)
    {
        if(mid<=0)
            indexToInsert = 0;
        else if (mid>=arr.size())
            indexToInsert = (int)(arr.size());
    }

    arr.insert(arr.begin() + indexToInsert, value);
}



int search(std::vector<int> arr, int size, int value)
{
    if (arr[size - 1] == (value + size - 1))
        return arr[-1] + 1;
 
    int a = 0, b = size - 1;
    int mid;
    while ((b - a) > 1) {
        mid = (a + b) / 2;
        if ((arr[a] - a) != (arr[mid] - mid))
            b = mid;
        else if ((arr[b] - b) != (arr[mid] - mid))
            a = mid;
    }
    return (arr[a] + 1);
}


int main(){
    std::vector<int> ans;
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++){
        int guest;
        cin >> guest;
        if (guest > 0){
            std::vector<int> tmp;
            tmp.push_back(guest);
            const auto it = std::search(ans.begin(), ans.end(), tmp.begin(), tmp.end());
            if (it == ans.end()){
                std::cout << guest << std::endl;
                ans.push_back(guest);
            }
            else{
                std::vector<int> tmp_(it, ans.end());
                int res = search(tmp_, tmp_.size(), guest);
                std::cout << res << std::endl;
                insert(ans, res);
            }
        }
        else{
            std::vector<int> tmp;
            tmp.push_back(abs(guest));
            auto it = std::search(ans.begin(), ans.end(), tmp.begin(), tmp.end());
            ans.erase(it - 1);
        }
    }
}