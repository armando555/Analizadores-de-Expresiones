#include "parser.h"
#include "calcex.h"
#include <string>
#include <sstream>

Parser::Parser(istream* in) {
   scan = new Scanner(in);
}

Parser::~Parser() {
   try {
      delete scan;
   } catch (...) {}
}

AST* Parser::parse() {
   cout<<"PROG"<<endl;
   return Prog();
}

AST* Parser::Prog() {
   cout<<"EXPR IN PARSER DE PROG"<<endl;
   AST* result = Expr();
   cout<<"GET TOKEN DE PROG"<<endl;
   Token* t = scan->getToken();
   cout<<"SALÍ DEL GET TOKEN DE PROG"<<endl;
   if (t->getType() != eof) {
      cout << "Syntax Error: Expected EOF, found token at column " << t->getCol() << endl;
      throw ParseError;
   }

   return result;
}

AST* Parser::Expr() {
   cout<<"FUNCTION EXPR"<<endl;
   return RestExpr(Term());
}

AST* Parser::RestExpr(AST* e) {
   cout<<"RESTEXPR GET TOKEN"<<endl;
   Token* t = scan->getToken();

   if (t->getType() == add) {
      cout<<"ADD NODE"<<endl;
      return RestExpr(new AddNode(e,Term()));
   }

   if (t->getType() == sub)
      return RestExpr(new SubNode(e,Term()));

   if (t->getType()== times){
      return RestExpr(new TimesNode(e,Term()));
   }
   if(t->getType()==divide){
      return RestExpr(new DivideNode(e,Term()));
   }
   if(t->getType()==module){
      return RestExpr(new ModuleNode(e,Term()));
   }
   if(t->getType()==potencia){
      return RestExpr(new PotenciaNode(e,Term()));
   }
   scan->putBackToken();
   return e;
}

AST* Parser::Term() {
   //write your Term() code here. This code is just temporary
   //so you can try the calculator out before finishing it.
   cout<<"TERM PARSER"<<endl;
   Token* t = scan->getToken();

   if (t->getType() == number) {
      istringstream in(t->getLex());
      int val;
      in >> val;
      return new NumNode(val);
   }

   cout << "Term not implemented" << endl;

   throw ParseError; 
}

AST* Parser::RestTerm(AST* e) {
   cout << "RestTerm not implemented" << endl;

   throw ParseError; 
}

AST* Parser::Storable() {
   cout << "Storable not implemented" << endl;

   throw ParseError; 
}

AST* Parser::Factor() {
   cout << "Factor not implemented" << endl;

   throw ParseError; 
}
   
