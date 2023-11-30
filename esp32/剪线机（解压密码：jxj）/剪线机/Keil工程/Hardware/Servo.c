#include "stm32f10x.h"                  // Device header
#include "PWM1.h"
#include "Servo.h"

void Servo_Init(void)
{
	PWM1_Init();
	Servo_Up();
}

void Servo_SetAngle(float Angle)
{
	PWM1_SetCompare2(Angle / 180 * 2000 + 500);
}

void Servo_Down(void)
{
	Servo_SetAngle(65);
}

void Servo_Middle(void)
{
	Servo_SetAngle(77);
}

void Servo_Up(void)
{
	Servo_SetAngle(90);
}
