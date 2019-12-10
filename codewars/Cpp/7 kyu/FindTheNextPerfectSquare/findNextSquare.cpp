#include <cmath>
long int findNextSquare(long int sq) {
  if(sqrt(sq) != (int)sqrt(sq)){return -1;}
  return  pow(sqrt(sq) + 1,2);
}