const std::map<char, char> mapping =
{
  {'A', 'T'},
  {'T', 'A'},
  {'C', 'G'},
  {'G', 'C'},
};

std::string DNAStrand(std::string dna)
{
  for (char& c : dna)
  {
    c = mapping.at(c);
  }
  return dna;
}