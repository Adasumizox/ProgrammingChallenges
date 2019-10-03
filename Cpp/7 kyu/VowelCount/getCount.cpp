#include <string>
#include <algorithm>

using namespace std;

int getCount(const string& inputStr){
  return count_if(inputStr.begin(), inputStr.end(), [](const char ch) {
      switch(ch) {
          case 'a':
          case'e':
          case'i':
          case'o':
          case'u':
              return true;
          default:
              return false;} 
     });
}