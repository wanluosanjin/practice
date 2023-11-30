#include "stm32f10x.h"
#include "PID.h"

void PID_Init(PID_t *PID)
{
	PID->Target = 0;
	PID->Error = 0;
	PID->PrevError = 0;
	PID->I = 0;
	PID->D = 0;
	PID->Kp = 0;
	PID->Ki = 0;
	PID->Kd = 0;
	PID->Out = 0;
	PID->OutMax = 0;
	PID->OutMin = 0;
}

void PID_SetParam(PID_t *PID, float Kp, float Ki, float Kd)
{
	PID->Kp = Kp;
	PID->Ki = Ki;
	PID->Kd = Kd;
}

void PID_SetThreshold(PID_t *PID, float OutMax, float OutMin)
{
	PID->OutMax = OutMax;
	PID->OutMin = OutMin;
}

void PID_SetTarget(PID_t *PID, float Target)
{
	PID->Target = Target;
}

float PID_Update(PID_t *PID, float Real, float dt)
{
	PID->Real = Real;
	
	PID->PrevError = PID->Error;
	PID->Error = PID->Target - Real;
	
	PID->I += PID->Error * dt;
	
	PID->D = (PID->Error - PID->PrevError) / dt;
	
	PID->Out = PID->Kp * PID->Error
			 + PID->Ki * PID->I
			 + PID->Kd * PID->D;
	
	if (PID->Out > PID->OutMax)
	{
		PID->Out = PID->OutMax;
	}
	else if (PID->Out < PID->OutMin)
	{
		PID->Out = PID->OutMin;
	}
	
	return PID->Out;
}
