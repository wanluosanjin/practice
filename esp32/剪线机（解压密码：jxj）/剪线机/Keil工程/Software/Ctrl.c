#include "stm32f10x.h"
#include "PID.h"
#include "Encoder.h"
#include "Motor.h"

PID_t MPID;
uint8_t WorkFlag = 0;

void Ctrl_Init(void)
{
	PID_Init(&MPID);
	PID_SetParam(&MPID, 0.5, 0, 2.5);
	PID_SetThreshold(&MPID, 100, -100);
	PID_SetTarget(&MPID, 0);
	Encoder_Init();
	Motor_Init();
}

void Ctrl_SetTarget(int16_t Target)
{
	WorkFlag = 1;
	PID_SetTarget(&MPID, Target);
}

void Ctrl_Reset(void)
{
	WorkFlag = 1;
	PID_SetTarget(&MPID, 0);
	Encoder_SetCounter(0);
}

void Ctrl_Loop(void)
{
	if (WorkFlag)
	{
		PID_Update(&MPID, Encoder_GetCounter(), 50);
		Motor_SetSpeed(MPID.Out);
	}
}
