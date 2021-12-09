//ATELIER 3
//EXERCICE 9

#include<iostream>
using namespace std;

class Test {
    private:
       static  int cmp;
    public:
         void call(){
             cmp++;
             cout<<cmp<<endl;
         }

};

int Test :: cmp=0;
//FONCTION PRINCIPALES
int main(){
    Test A1,A2;
      A1.call();
      A2.call();
    
}