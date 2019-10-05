int find_short(const std::string &str)
{
    std::istringstream inp(str);
    std::string s;
    int len = -1;
    while (std::getline(inp, s, ' '))
        if (s.length() < len)
            if ((len = s.length()) == 1)
                break;
    return len;
}