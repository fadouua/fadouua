//ATELIER 3
//EXERCICE 2
#include <iostream>

using namespace std;

class Shape
{

public: 
    float x, y;
	int R1,R2,T1,T2,n;


  Shape()
  {
    cout<<"Calculez l'aire du triangle ou du rectangle ? "<<endl;//l'utilisateur doit choisir le reactangle ou le triangle
    cout<<"Tapez 1 pour le rectangle ."<<endl;
    cout<<"Tapez 2 pour le triangle ."<<endl;
    cin>>n;
  }
  //fonction pour calculer l'aire:
  void calculer(){
    //l'utilisateur doit entrer les dimensions de rectangle
  	if (n==1){
  	cout<<"Donnez les dimensions du rectangle :"<<endl;
  	cout<<"Entrez l'hauteur :";
  	cin>>R1;
  	cout<<endl<<"Entrez le largeur :";
  	cin>>R2;
  	cout << "L'aire du rectangle est: " <<R1 * R2 << endl;
  }
  //l'utilisateur doit entrer les dimensions de rectangle
  else if(n==2){
  	cout<<"Donnez les dimensions du triangle :"<<endl;
  	cout<<"Entrez l'hauteur :";
  	cin>>T1;
  	cout<<endl<<"Entrez le largeur :";
  	cin>>T2;
  	cout << "L'aire du triangle est: " <<(T1 * T2)/2 << endl;
  }
  }
};

//Fonction principale
int main (){

  Shape a;
  a.calculer();

  return 0;
}
