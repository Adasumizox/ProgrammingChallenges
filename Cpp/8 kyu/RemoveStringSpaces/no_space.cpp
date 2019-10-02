std::string no_space(std::string x)
{
    x.erase(std::remove(x.begin(), x.end(), ' '), x.end());
    return x;
}