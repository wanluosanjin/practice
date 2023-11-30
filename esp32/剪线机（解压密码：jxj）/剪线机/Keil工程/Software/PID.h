#ifndef __PID_H
#define __PID_H

typedef struct{
	float Target;
	float Error;
	float PrevError;
	float I;
	float D;
	float Kp;
	float Ki;
	float Kd;
	float Out;
	float OutMax;
	float OutMin;
	float Real;
} PID_t;

void PID_Init(PID_t *PID);

void PID_SetParam(PID_t *PID, float Kp, float Ki, float Kd);

void PID_SetThreshold(PID_t *PID, float OutMax, float OutMin);

void PID_SetTarget(PID_t *PID, float Target);

float PID_Update(PID_t *PID, float Real, float dt);

#endif
