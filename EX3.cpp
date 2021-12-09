//ATELIER 3
//EXERCICE 3

#include <iostream>
using namespace std;
class complexe{
	
	public:
		int RE1;
		int RE2;
		int IM1;
		int IM2;
		
		int op;
		//FAIRE ENTRER LES COMPLEXES
		 complexe(){
		 	cout<<"Pour le premier complexe "<<endl;
			cout<<"Faire entrer la partie reele"<<endl;		
			cin>>RE1; 
		    cout<<"Faire entrer la partie imaginaire"<<endl;		
			cin>>IM1; 	
			
			cout<<"Pour le deuxieme complexe "<<endl;
			cout<<"Faire entrer la partie reele "<<endl;		
			cin>>RE2;
			cout<<"Faire entrer la partie imaginaire"<<endl;		
			cin>>IM2;  
			
			cout<<"Choisissez une operation"<<endl;
            cout<<"1.Somme"<<endl;
            cout<<"2.Soustraction"<<endl;
            cout<<"3.Multiplication"<<endl;
            cout<<"4.Division"<<endl;
            cin>>op;
			
			};
			//FONCTION DE CALCULE
	void calculer(){
		if(op==1){
			cout<<"la somme de deux complexes est : " <<RE1+RE2<< " +"<<IM1+IM2<<"i"<<endl;//LA SOMME
        }
	
	    else if (op==2){
	  	    cout<<"la soustraction de deux complexes est : " <<RE1-RE2<< " +"<<IM1-IM2<<"i"<<endl;//LA SOUSTRACTION
	  	}
	  	
	  	else if(op==3){
	  		cout<<"la multiplication de deux complexes est : "<<RE1*RE2+IM1*IM2<< " +"<<RE1*IM2+IM1*RE2<<"i"<<endl;//LA MULTIPLICATION
	    }
	    
		else if(op==4){
		   if(IM2==0 && RE2==0){
		   	    cout<<"erreur division sur 0";
		   }
		    else{
		        cout<<"la division de deux complexes est : " <<float(IM1*IM2-RE1*RE2)/float(IM2*IM2+RE2*RE2)<< " +"<<float(IM1*RE2-RE1*IM2)/float(RE2*RE2+IM2*IM2)<<"i"<<endl;//LA DIVISION
		  		}
			 
		  }
		    else{
		  	    cout<<"Choisissez une des quatres operations!"<<endl;
		  }
	}
	
	
};
	
//FONCTION PRINCIPALES
int main(){
	complexe a;
	a.calculer();	

	return 0;
};
