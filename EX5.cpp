//ATELIER 5
//EXERCICE 5
#include<iostream>
using namespace std;
class Animal{
    private:
    int Age;
    string Nom;
    public:
    Animal(int Age , string Nom){
        this->Age=Age;
        this->Nom=Nom;
    }
    void set_value();

};

class Zebra{
    protected:
          int Age;
    private:
          string Nom;
    public:
    Zebra(int Age , string Nom){
        this->Age=Age;
        this->Nom=Nom;
    }
    void show1(){
        cout<<"Age = "<<Age<<" ,  Nom = "<<Nom<<endl;
    }
};

class Dolphin{
    protected:
          int Age;
    private:
          string Nom;
    public:
    Dolphin(int Age , string Nom){
        this->Age=Age;
        this->Nom=Nom; 
    }
    void show2(){
        cout<<"Age = "<<Age<<" ,  Nom = "<<Nom<<endl;
    }
};

//FONCTION PRINCIPALES
int main(){
     Zebra z(16,"ZEBRA");
     Dolphin d(20,"DOLPHIN");
     z.show1();
     d.show2();

    return 0;
};