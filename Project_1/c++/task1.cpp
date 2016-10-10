#include "pre_process.h"

int main() {
  PreProcess* pre = new PreProcess() ;
  pre->readJsonFile("./input.json");
  return 0;
}
