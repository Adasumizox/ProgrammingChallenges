#include <vector>

std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
    if(input.empty())
      return {};
    int countPositives {0}, sumNegatives {0};
    for(int x: input)
      x>0 ? countPositives++ : (x!=0 ? sumNegatives+=x : 0);
    return {countPositives, sumNegatives};
}