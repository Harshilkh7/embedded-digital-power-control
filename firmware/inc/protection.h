#pragma once

#include <stdint.h>

enum class ProtectionState : uint8_t {
    REGULATING = 0,
    WARNING,
    OVERVOLTAGE,
    UNDERVOLTAGE,
    OVERCURRENT
};

ProtectionState protection_evaluate(float voltage, float current);
const char* protection_name(ProtectionState state);
