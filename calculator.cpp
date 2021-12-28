#include<iostream>
#include<string>
using namespace std;
string input, num1,num2="", oper1, oper2, actual_num_1, actual_num_2;
int number1, actual_number_1, actual_number_2;


void user_input(){
    cin>>input;
}
void format_input(){
    for(int i=0; i<input.length(); i++){
        if(isdigit(input.at(i))){
            // cout<<"yes";
            num1+=input.at(i);
            
        }
        else{
            if(oper1.length()==0){
                oper1=input.at(i);
                actual_num_1=num1;
            }
            else if(oper2.length()==0){
            	oper2=input.at(i);
            	actual_num_2=num1;
            }
            
            num1="";
            
        }
    }
    //cout<<num1<<endl;
    //cout<<oper1<<endl;
    //cout<<oper2<<endl;
    //cout<<actual_num_1<<endl;
    //cout<<actual_num_2<<endl;
    
}

void output_printer_2_numbers(){
	number1= stoi(num1);
	actual_number_1 = stoi(actual_num_1);
	if(oper1=="+" && oper2==""){
        cout<<number1+actual_number_1<<endl;
    }
    else if(oper1=="-" && oper2==""){
        cout<<actual_number_1-number1<<endl;
    }
    else if(oper1=="*" && oper2==""){
        cout<<number1*actual_number_1<<endl;
    }
    else if(oper1=="/" && oper2==""){
        cout<<actual_number_1/number1<<endl;
    }
	}

void output_printer(){
    number1 = stoi(num1);
    actual_number_1 = stoi(actual_num_1);
    actual_number_2 = stoi(actual_num_2);
    
    if(oper1=="+" && oper2=="+"){
        cout<<actual_number_1+number1+ actual_number_2<<endl;
    }
    else if(oper1=="+" && oper2=="-"){
        cout<<actual_number_1-number1+ actual_number_2<<endl;
    }
    else if(oper1=="-" && oper2=="+"){
        cout<<actual_number_1+number1- actual_number_2<<endl;
    }
    else if(oper1=="-" && oper2=="-"){
        cout<<actual_number_1-number1- actual_number_2<<endl;
    }
    else if(oper1=="+" && oper2=="*"){
        cout<<actual_number_1+(number1* actual_number_2)<<endl;
    }
    else if(oper1=="*" && oper2=="+"){
        cout<<(actual_number_1*actual_number_2)+number1<<endl;
    }
    else if(oper1=="" && oper2==""){
        cout<<actual_number_1*number1* actual_number_2<<endl;
    }
    else if(oper1=="+" && oper2=="/"){
        cout<<actual_number_1+ (actual_number_2/number1)<<endl;
    }
    else if(oper1=="/" && oper2=="+"){
        cout<<(actual_number_1/actual_number_2)+number1<<endl;
    }
    else if(oper1=="-" && oper2=="/"){
        cout<<actual_number_1- (actual_number_2/number1)<<endl;
    }
    else if(oper1=="/" && oper2=="-"){
        cout<<(actual_number_1/actual_number_2)-number1<<endl;
    }
    else if(oper1=="-" && oper2=="*"){
        cout<<actual_number_1+(number1* actual_number_2)<<endl;
    }
    else if(oper1=="*" && oper2=="-"){
        cout<<(actual_number_1*actual_number_2)+number1<<endl;
    }
    else if(oper1=="/" && oper2=="*"){
        cout<<(actual_number_1/ actual_number_2)*number1<<endl;
    }
    else if(oper1=="*" && oper2=="/"){
        cout<<(actual_number_1*actual_number_2)/number1<<endl;
    }
    else if(oper1=="/" && oper2=="/"){
        cout<<(actual_number_1/ actual_number_2)/number1<<endl;
    }
}

void decider(){
  if(oper2.length()==0){
  	output_printer_2_numbers();
  	}
  else{
  	output_printer();
  	}
  }
  
int main()
{
    cout<<"Please give input: ";
    user_input();
    format_input();
    decider();
    return 0;
}