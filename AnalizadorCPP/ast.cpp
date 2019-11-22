#include "ast.h"
#include <iostream>
#include "calculator.h"
#include <math.h>
// for debug information uncomment
//#define debug

AST::AST() {}

AST::~AST() {}

BinaryNode::BinaryNode(AST* left, AST* right):
   AST(),
   leftTree(left),
   rightTree(right)
{}

BinaryNode::~BinaryNode() {
#ifdef debug
   cout << "In BinaryNode destructor" << endl;
#endif

   try {
      delete leftTree;
   } catch (...) {}

   try {
      delete rightTree;
   } catch(...) {}
}

int PotenciaNode::potencia(){
   int num=getLeftSubTree()->evaluate();
   int num2=getRightSubTree()->evaluate();
   int acu=1;
   for(int i=1;i<=num2;i++){
      acu=acu*(num);
   }
   return acu;
}

AST* BinaryNode::getLeftSubTree() const {
   return leftTree;
}

AST* BinaryNode::getRightSubTree() const {
   return rightTree;
}

UnaryNode::UnaryNode(AST* sub):
   AST(),
   subTree(sub)
{}

UnaryNode::~UnaryNode() {
#ifdef debug
   cout << "In UnaryNode destructor" << endl;
#endif

   try {
      delete subTree;
   } catch (...) {}
}
   
AST* UnaryNode::getSubTree() const {
   return subTree;
}

AddNode::AddNode(AST* left, AST* right):
   BinaryNode(left,right)
{}

int AddNode::evaluate() {
   cout<<"subtree"<<endl;
   return getLeftSubTree()->evaluate() + getRightSubTree()->evaluate();
}

SubNode::SubNode(AST* left, AST* right):
   BinaryNode(left,right)
{}
TimesNode::TimesNode(AST* left, AST*right):
   BinaryNode(left,right)
{}
DivideNode::DivideNode(AST* left, AST* right):
   BinaryNode(left,right)
{}
ModuleNode::ModuleNode(AST* left, AST* right):
   BinaryNode(left,right)
{}
PotenciaNode::PotenciaNode(AST* left, AST* right):
   BinaryNode(left,right)
{}
int SubNode::evaluate() {
   cout<<"subtree"<<endl;
   return getLeftSubTree()->evaluate() - getRightSubTree()->evaluate();
}
int TimesNode::evaluate(){
   cout<<"subtree"<<endl;
   return getLeftSubTree()->evaluate()*getRightSubTree()->evaluate();
}
int DivideNode::evaluate(){
   cout<<"subtree"<<endl;
   return getLeftSubTree()->evaluate()/getRightSubTree()->evaluate();
}
int ModuleNode::evaluate(){
   cout<<"subtree"<<endl;
   return getLeftSubTree()->evaluate()%getRightSubTree()->evaluate();
}
int PotenciaNode::evaluate(){
   cout<<"subtree"<<endl;
   return pow(getLeftSubTree()->evaluate(),getRightSubTree()->evaluate());
}

NumNode::NumNode(int n) :
   AST(),
   val(n)
{}

int NumNode::evaluate() {
   return val;
}
