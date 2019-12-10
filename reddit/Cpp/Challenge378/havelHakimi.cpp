#include <vector>
#include <algorithm>
bool havelHakimi(vector<uint16_t> vec) {
    //maybe queue better
    while(true) {
        vec.erase(std::remove(vec.begin(), vec.end(), 0), vec.end());
        if(vec.size() == 0) return true;
        sort(vec.begin(),vec.end(), greater<uint16_t>());
        uint16_t n = vec.front();
        vec.erase(vec.begin());
        if (n > vec.size()) return false;
        for(auto& element: vec) {
            element -= 1;
        }
    }
}