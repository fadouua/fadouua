#include <iostream>

using namespace std;

// definition de class
class Complex
{
public:
    float reel;
    float imaginaire;
    void setValue(float re,float im);
    Complex operator+(Complex);
    Complex operator-(Complex);
    Complex operator*(Complex);
    Complex operator/(Complex);
};

// fonction pur changer les variable reel,imaginaire 
void Complex::setValue(float re,float im)
{
    reel = re;
    imaginaire = im;
}

// Definition de l'operateur
Complex Complex::operator+(Complex second){
    Complex result;
    result.imaginaire = this->imaginaire + second.imaginaire;
    result.reel = this->reel + second.reel;
    return result;
}

Complex Complex::operator-(Complex second){
    Complex result;
    result.imaginaire = this->imaginaire - second.imaginaire;
    result.reel = this->reel - second.reel;
    return result;
}

Complex Complex::operator*(Complex second){
    Complex result;
    result.reel = this->reel * second.reel - this->imaginaire * second.imaginaire;
    result.imaginaire = this->reel * second.imaginaire + this->imaginaire * second.reel;
    return result;
}


Complex Complex::operator/(Complex second){
    Complex result;
       result.reel = (this->reel * second.reel + this->imaginaire * second.imaginaire) /
                (second.reel * second.reel + second.imaginaire * second.imaginaire);
        result.imaginaire = (this->imaginaire * second.reel - this->reel * second.imaginaire) /
                (second.reel * second.reel + second.imaginaire * second.imaginaire);
    return result;
}
     


//fonction prend deux parametre de type (class) Complex
// et retourne un variable de meme type Complex
Complex arithmetics(Complex first,Complex second){
    Complex result; // pour stocker la resultat 
    float tempRe,tempIm;
    char operation ;
    //on montre les operations possible a l'utilisateur
    cout << "quelle est votre operation ? \n";
    cout << "1: la somme\n";
    cout << "2: la soustraction\n";
    cout << "3: la multiplication\n";
    cout << "4: la devision\n";
    cin >> operation;

    // on applique directement les regle des operation des nombres complex
    // selon l'operation choisi par l'utilisateur 
    switch (operation)
    {
    case '1':
        result = first + second;
        break;
     case '2':
        result = first - second;
        break;
     case '3':
        result = first * second;        
        break;
     case '4':
        result = first / second;
        break;
    }

    return result;
    
}

int main(int argc, char const *argv[])
{
    float tempRe,tempIm;

    // creation de deux nombre complex
    Complex z1,z2;
    
    // on demande des valeur 
    cout << "entre la partie reel du premier nombre : " << endl;
    cin >> tempRe;
    cout << "entre la partie imaginaire du premier nombre : " << endl;
    cin >> tempIm;
    z1.setValue(tempRe,tempIm);

    cout << "entre la partie reel du deuxieme nombre : " << endl;
    cin >> tempRe;
    cout << "entre la partie imaginaire du deuxieme nombre : " << endl;
    cin >> tempIm;
    z2.setValue(tempRe,tempIm);

    // appele de la fonction
    cout << "le premier nombre: " << z1.reel << " + " << z1.imaginaire << "i \n";
    cout << "le deuxieme nombre: " << z2.reel << " + " << z2.imaginaire << "i \n";
    Complex result = arithmetics(z1,z2);

    // affichage de la resultat de l'operation
    cout << "Votre solution est : "<< endl << result.reel << " + " << result.imaginaire << "i \n";

    return 0;
}