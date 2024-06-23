#include<stdio.h>
int main(){
float p,t,r,SI,Amt;
printf("Enter the principal amount rathe of interest and time period");
scanf("%f %f %f"&p,&r,&t);
SI=(p*t*r)/100;
Amt=SI+p;
printf("The simple interest is : %f" SI);
printf("The amount is : %f" Amt);
}
