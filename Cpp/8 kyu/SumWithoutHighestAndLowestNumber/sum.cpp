#include<vector>
#include<numeric>
using namespace std;

int sum(vector<int> numbers)
{
  if (numbers.size() < 2) return 0;
  return std::accumulate(numbers.begin(), numbers.end(), 0) - *min_element(numbers.begin(), numbers.end()) - *max_element(numbers.begin(), numbers.end());
}