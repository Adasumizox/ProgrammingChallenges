using namespace std;

class Accumul
{
public:
    static std::string accum(const std::string &s) {
      stringstream result;
      for (int i = 0; i < s.length(); i++) 
        result << "-" << string(1, toupper(s[i])) << string(i, tolower(s[i])); 
      return result.str().substr(1);
    }
};