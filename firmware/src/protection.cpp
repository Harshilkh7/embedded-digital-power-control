#include "protection.h"

namespace {
constexpr float UV_LIMIT = 2.80f;
constexpr float OV_LIMIT = 3.63f;
constexpr float OC_LIMIT = 2.00f;
constexpr float WARNING_LOW = 3.00f;
constexpr float WARNING_HIGH = 3.50f;
constexpr float WARNING_CURRENT = 1.50f;
}

ProtectionState protection_evaluate(float voltage, float current) {
    if (voltage > OV_LIMIT) return ProtectionState::OVERVOLTAGE;
    if (voltage < UV_LIMIT) return ProtectionState::UNDERVOLTAGE;
    if (current > OC_LIMIT) return ProtectionState::OVERCURRENT;
    if (voltage < WARNING_LOW || voltage > WARNING_HIGH || current > WARNING_CURRENT) {
        return ProtectionState::WARNING;
    }
    return ProtectionState::REGULATING;
}

const char* protection_name(ProtectionState state) {
    switch (state) {
        case ProtectionState::REGULATING: return "REGULATING";
        case ProtectionState::WARNING: return "WARNING";
        case ProtectionState::OVERVOLTAGE: return "OVERVOLTAGE";
        case ProtectionState::UNDERVOLTAGE: return "UNDERVOLTAGE";
        case ProtectionState::OVERCURRENT: return "OVERCURRENT";
        default: return "UNKNOWN";
    }
}
