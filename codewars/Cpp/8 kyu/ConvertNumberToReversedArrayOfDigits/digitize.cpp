#include<vector>
std::vector<int> digitize(unsigned long n) 
{
    std::vector <int> num;
    while(n!=0){
        num.push_back(n%10);//fetch the LSB of the number
        n = n / 10;//right shift the number
    }
    return num;
}

