#include "control.h"
static float integral;
void control_reset(void){integral=0;}
float control_update(float ref,float meas){
    const float kp=.08f, ki=80.0f, dt=1e-6f;
    float e=ref-meas, candidate=integral+ki*e*dt;
    float raw=kp*e+candidate, out=raw;
    if(out>.95f)out=.95f; if(out<0)out=0;
    if(!((raw>.95f&&e>0)||(raw<0&&e<0))) integral=candidate;
    return out;
}
