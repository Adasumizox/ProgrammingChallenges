#include <vector>
#include <numeric>

int positive_sum (const std::vector<int> arr){
  return std::accumulate(arr.begin(), arr.end(), 0, [](int a, int b) { return a + std::max(0, b); });
}