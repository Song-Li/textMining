#include <iostream>
#include <vector>
#include <stdlib.h>
#include <map>
#include <set>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

class PreProcess {
public:
  map<string, string> jsonToMap(string json);
  vector<map<string, string> > readJsonFile(string file_name);
  set<string> tokenize(map<string, string> json_file);
};
