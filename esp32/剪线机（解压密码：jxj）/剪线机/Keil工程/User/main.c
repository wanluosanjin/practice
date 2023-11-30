#include "stm32f10x.h"                  // Device header
#include "Delay.h"
#include "LED.h"
#include "Key.h"
#include "OLED.h"
#include "Motor.h"
#include "Servo.h"
#include "Encoder.h"
#include "Ctrl.h"
#include "PID.h"
#include "Timer.h"

uint8_t KeyNum;
uint16_t num;

extern PID_t MPID;

#define		RST		0
#define		C1		11
#define		C2		12
#define		C3		13
#define		SU		21
#define		SM		22
#define		SD		23

uint8_t StartFlag;
uint8_t State;
uint16_t Time[]  = {100,100,500,500,100,1200,500,100,500,500};
uint8_t Action[] = {RST,C1, SM, SU, C2, SM,  SU, C3, SD, SU};

uint8_t UpParam = 90, MiddleParam = 65, DownParam = 60;


int main(void)
{
	LED_Init();
	Key_Init();
	OLED_Init();
	Servo_Init();
	Ctrl_Init();
	Timer_Init();
	
	OLED_ShowString(1, 1, "Target:");
	OLED_ShowString(2, 1, "Real  :");
	OLED_ShowString(3, 1, "Out   :");
	OLED_ShowString(4, 1, "U:00 M:00 D:00");
	
	while (1)
	{
		KeyNum = Key_GetNum();
		if (KeyNum == 1)
		{
			StartFlag = !StartFlag;
			if (StartFlag == 1)
			{
				LED_ON();
			}
			else
			{
				LED_OFF();
			}
		}
		if (KeyNum == 2)
		{
			MiddleParam += 1;
		}
		if (KeyNum == 3)
		{
			MiddleParam -= 1;
		}
		OLED_ShowSignedNum(1, 8, MPID.Target, 5);
		OLED_ShowSignedNum(2, 8, MPID.Real, 5);
		OLED_ShowSignedNum(3, 8, MPID.Out, 5);
		OLED_ShowNum(4, 3, UpParam, 2);
		OLED_ShowNum(4, 8, MiddleParam, 2);
		OLED_ShowNum(4, 13, DownParam, 2);
	}
}

void DoAction(uint8_t Action)
{
	if (Action == RST)
	{
		Ctrl_Reset();
	}
	else if(Action == C1)
	{
		Ctrl_SetTarget(60);
	}
	else if(Action == C2)
	{
		Ctrl_SetTarget(3200);
	}
	else if(Action == C3)
	{
		Ctrl_SetTarget(3330);
	}
	else if(Action == SU)
	{
		Servo_SetAngle(UpParam);
	}
	else if(Action == SM)
	{
		Servo_SetAngle(MiddleParam);
	}
	else if(Action == SD)
	{
		Servo_SetAngle(DownParam);
	}
}

void TIM4_IRQHandler(void)
{
	static uint16_t TCount[2];
	if (TIM_GetITStatus(TIM4, TIM_IT_Update) == SET)
	{
		TCount[0] ++;
		if (TCount[0] >= 50)
		{
			TCount[0] = 0;
			Ctrl_Loop();
		}
		
		if (StartFlag)
		{
			TCount[1] ++;
			if (TCount[1] >= Time[State])
			{
				TCount[1] = 0;
				DoAction(Action[State]);
				State ++;
				State %= 10;
			}
		}
		
		TIM_ClearITPendingBit(TIM4, TIM_IT_Update);
	}
}
