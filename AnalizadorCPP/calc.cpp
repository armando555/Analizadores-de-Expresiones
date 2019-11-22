#include <iostream>
#include <sstream>
#include <string>
#include "calcex.h"
#include "calculator.h"
using namespace std;

Calculator* calc;

int main(int argc, char* argv[]) {
   string line;
 
   try {

      cout << "Please enter a calculator expression: ";

      getline(cin, line);
      // line + '\n';

      calc = new Calculator();

      int result = calc->eval(line);

      cout << "The result is " << result << endl;

      delete calc;

   }
   catch(Exception ex) {
      cout << "Program Aborted due to exception!" << endl;
   }
}
   
