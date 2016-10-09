#include "pre_process.h"

map<string, string> PreProcess::jsonToMap(string json) {
  map<string, string> ret;
  int len = json.length();
  bool flag = 0; //make the " is the start or end "
  bool name = 1;
  string key, value;
  for(int i = 1;i < len;++ i) {
    if(json[i] == ':') {
      name = 0;
      ++ i;
      continue;
    }
    else if(json[i] == ',' || json[i] == '}') {
      name = 1;
      ret[key] = value;
      ++ i;
      key = "";
      value = "";
      continue;
    }
    if((json[i] == '\"' || json[i] == '[') && json[i - 1] != '\\') {
      while( !((json[i] == '"' || json[i] == ']' ) &&  i && json[i - 1] != '\\') ) {
        if(name) key += json[i];
        else value += json[i];
        ++ i;
      }
    }else {
      if(name) key += json[i];
      else value += json[i];
    }
  }
  return ret;
}

vector<map<string, string> > PreProcess::readJsonFile(string file_name) {
  vector<map<string, string> > ret;
  ifstream input_stream;
  input_stream.open(file_name.c_str());
  if(!input_stream) {
    cout << "Open json file error" << endl;
    return ret;
  }
  string input_string;
  while(getline(input_stream, input_string)) {
    ret.push_back(jsonToMap(input_string));    
    input_string = "";
  }
  cout << ret.size() << " lines of data imported" <<endl;
  return ret;
}
