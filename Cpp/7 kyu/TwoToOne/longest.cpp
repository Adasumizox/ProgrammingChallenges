#include <set>
#include <string>

namespace TwoToOne {

std::string longest(const std::string& s1, const std::string& s2) {
  std::set<char> chars(s1.begin(), s1.end());
  for (char c : s2)
    chars.insert(c);
  return std::string(chars.begin(), chars.end());
}

}