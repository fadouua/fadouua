//ATELIER 3
//EXERCICE 1
#include <iostream>
using namespace std;

class Myclass{
		public://accees specifique
	int num;//attribut
	Myclass();//constructeur par defaut
	~Myclass();//destructeur par utilisateur
	//fonction definie a l'interieure de note classe
	void print(){
		cout<<"Faire entrer le numero : "<<endl;
		cin>> num ;
		cout<<"votre numero est : "<<num<<endl;
	};
};

	Myclass::Myclass(){
};
 
    Myclass::~Myclass(){
	};
int main(){
	Myclass etu;	
	
	etu.print();
	return 0;
};


