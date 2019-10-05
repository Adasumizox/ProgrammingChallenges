#include <iomanip>

using namespace std;

string seriesSum(int n)
{
    double ret = 0.0;
    double base = 1.0;
    while (n--) {
      ret += 1 / base;
      base += 3;
    }
    stringstream retss;
    retss << setprecision(2) << fixed << ret;
    return retss.str();
}