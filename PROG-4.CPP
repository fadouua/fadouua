#include <iostream>
#include <list>
using namespace std;
int main()
{
    list<string> Liste;   //d�claration une liste
    string n;
    int i;
    cout<<"Entrer N, Prenom et Age de chaque personne sous form de Nom,Prenom,age. inserez ( pause ) quand vous terminez :"<<endl;
    for (i = 0;; i++) 
    {
    cin>>n;
    if(n=="pause")
    {
        break;   
    }
    Liste.push_back(n); 
    }
    list<string>::iterator it;  
    Liste.sort();     
    it=Liste.begin();
    cout<<"votre Triage  est : " <<endl ;
    for (it;it!=Liste.end();it++)  
    {
            cout<<*it<<"  ";
    }
}