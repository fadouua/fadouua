#include <iostream>
#include <list>
using namespace std;
int main()
{
    list<int> Liste;    //declaration une liste
    //declaration des variables
    int n; 
    int i;
    cout<<"inserez les nombres a trier "<<endl;
    cout<<"pour arreter taper 0 "<<endl;
    for (i = 0; ; i++)  
    {
    cin>>n;
    if(n==0)
    {
        break;  
    }
    Liste.push_back(n); 
    }
    list<int>::iterator it;  
    Liste.sort();    
    it=Liste.begin();
    cout<<"votre liste de nombre triee est : ";
    for (it ;it !=Liste.end();it++)  
    {
            cout<<*it<<"  ";
    }
}
