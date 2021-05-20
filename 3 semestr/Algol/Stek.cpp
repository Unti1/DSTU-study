#include<iostream>
#include<stdio.h>

using namespace std;

const int SIZE = 5;

struct Elem {
	int data;
	Elem* next;
};

void SPush(Elem** head, int count) {
	int x;
	Elem* p;
	for (int i = 0; i < count; i++) {
		cout << "Введите " << i << " элемент: ";
		cin >> x;
		p = new Elem();
		p->data = x;
		if (*head != NULL) {
			p->next = *head;
			*head = p;
		}
		else
		{
			*head = p;
		}
	}
}
void SPrint(Elem* head) {
	Elem* p = head;
	cout << "Стек: " << endl;
	while (p != NULL) {
		cout << p->data << endl;
		p = p->next;
	}
}
void SDelete(Elem** head) {
	Elem* p = *head;
	Elem* prev = NULL;
	int key;
	cout << "Введите ключ для удаления: " << endl;
	cin >> key;
	while (p != NULL) {
		if (p->data == key) {
			if (p == *head) {
				*head = p->next;
				free(p);
				p->data = NULL;
				p->next = NULL;
			}
			else
			{
				prev->next = p->next;
				free(p);
				p->data = NULL;
				p->next = NULL;
			}
		}
		prev = p;
		p = p->next;
	}
}
void delete_num(Elem** head, int count) {
	Elem* p = *head;
	Elem* prev = NULL;
	int num = 0;
	cout << "Введите номер: ";
	cin >> num;
	int i = 0;
	while (p != NULL) {
		if (num == i) {
			if (p == *head) {
				*head = p->next;
				free(p);
				p->next = NULL;
				p->data = NULL;
			}
			else {
				prev->next = p->next;
				free(p);
				p->next = NULL;
				p->data = NULL;
			}
		}
		prev = p;
		p = p->next;
		i++;
	}
}

struct stack {
	int data[SIZE];
	int head;
};
void SPush(stack& s) {
	int x;
	for (int i = 0; i < SIZE; i++) {
		if (s.head == SIZE) {
			cout << "Стэк оверфлоу" << endl;
			return;
		}
		cout << "Введите " << i << " элемент : ";
		cin >> x;
		s.data[s.head++] = x;
	}
}

void SPrint(stack& s, int size) {
	cout << "Стек :" << endl;
	for (int i = 0; i < size; i++) {
		cout << s.data[--s.head] << endl;
	}
}
void SPop(stack& s, int& size) {
	size--;
	for (int i = 0; i < size; i++) {
		s.data[s.head++];
	}
	for (int i = 0; i < size; i++) {
		cout << s.data[--s.head] << endl;
	}
}

void SChangeHeadTail(stack& s, int& size){
	int temp[SIZE];
	for (int i = 0; i < size; i++) {
		temp[i] = s.data[s.head++];
	}
	auto tail = temp[0];
	temp[0] = temp[SIZE-1];
	temp[SIZE-1] = tail;
	s.head = 0;
	for (int i = 0; i < size; i++) {
		s.data[s.head++] = temp[i];
	}
	
}

int main() {
	stack s;
	s.head = 0;
	int size = 5;
	Elem* head = NULL;
	setlocale(LC_ALL, "ru");
	int count = 0;
	//cout << "Введите количество элементов стека: " << endl;
	//cin >> count;
	/*SPush(&head, count);
	SPrint(head);
	SDelete(&head);*/

	SPush(s);
	SPrint(s, size);
	//SPop(s, size);
	SChangeHeadTail(s, size);
	SPrint(s, size);

}