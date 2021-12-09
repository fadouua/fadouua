//ATELIER 3
//EXERCICE4

#include <iostream>
using namespace std;
//la class mere
class mere{
	
	public:
		string mere;
		void display(){
			cout<<" Test1 "<<endl;
			
		};
};
//la class fille
class fille:public mere{
	public:
		string fille;
	void display(){
			cout<<" Test2  "<<endl;
		}
  };
//fonction principale
  int main(){
    mere M;
    M.display();
    fille F;
    F.display();
};
