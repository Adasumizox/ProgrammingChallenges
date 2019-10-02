#include <vector>
#include <numeric>

int square_sum(const std::vector<int>& v) {
  int x = std::inner_product(v.begin(), v.end(), v.begin(), 0 );
  return x;
}