#include <iostream>
#include <vector>
#include <queue>

struct line{
    int left;
    int right;
    bool operator < (const line & other) const {
        return this->right > other.right;
    }
};


bool cmp(const line & arg1, const line & arg2){
    return arg1.left < arg2.left;
}

int
main(void){
    int n, m;
    std::cin >> n >> m;
    std::vector<int>ans(n);
    std::vector<line> lines;
    for (int i = 0; i < m; i++){
        int l, r;
        std::cin >> l >> r;
        line line = {l, r};
        lines.push_back(line);
    }

    std::sort(lines.begin(), lines.end(), cmp);
    std::priority_queue<line> priority;
    int cur = 0;
    for (int i = 1; i < n + 1; i ++){
        while (cur < m && lines[cur].left == i){
            priority.push(lines[cur]);
            cur ++;
        }
        while ((priority.size() > 0) && priority.top().right < i){
            priority.pop();
        }
        ans[i - 1] = priority.size();
    }

    for (int i = 0; i < ans.size(); i++){
        std::cout << ans[i] << " ";
    }
    std::cout << std::endl;

}


