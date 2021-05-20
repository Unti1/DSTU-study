#include <iostream>
#include <string>
using namespace std;

class Word
{
public :
    string word;
    Word(string w) :word(w) {}
    Word(){}

};
class TranslationPair
{
public:
    Word* Eng;
    Word* Rus;
    TranslationPair(Word* eng, Word* rus) :Eng(eng), Rus(rus) {}
};

void RussianTranslate(TranslationPair** array,string word, const int size = 10)
{
    for (int i = 0; i < size; i++)
    {
        if (array[i]->Rus->word == word)
        {
            cout << array[i]->Eng->word << endl;
            break;
        }
    }
}

void EnglishTranslate(TranslationPair** array, string word, const int size = 10)
{
    for (int i = 0; i < size; i++)
    {
        if (array[i]->Eng->word == word)
        {
            cout << array[i]->Rus->word << endl;
            break;
        }
    }
}

int main()
{
    setlocale(LC_ALL, "ru");
    int size = 10;
    Word* arreng = new Word[size];
    TranslationPair** arrpair = new TranslationPair*[size]; 
    for (int i = 0; i < size; i++)
    {
        string e, r;
        cout << "Английский перевод: ";
        cin >> e;
        cout << "Русский перевод: ";
        cin >> r;
        Word* peng = new Word(e);
        Word* prus = new Word(r);
        arreng[i] = *peng;
        arrpair[i] = new TranslationPair(peng, prus);
    }
    RussianTranslate(arrpair, "banan");
    EnglishTranslate(arrpair, "banana");
    
    delete[] arreng;
    delete[] arrpair;

    return 0;
}
