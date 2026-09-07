CC=arm-none-eabi-gcc
CFLAGS=-mcpu=cortex-m3 -mthumb -O2 -ffreestanding -Wall -Wextra -Iinc
LDFLAGS=-mcpu=cortex-m3 -mthumb -Tlinker.ld -nostdlib -Wl,--gc-sections
BUILD=build
all: $(BUILD)/firmware.elf $(BUILD)/firmware.bin $(BUILD)/firmware.hex
$(BUILD):; mkdir -p $(BUILD)
$(BUILD)/%.o: src/%.c | $(BUILD); $(CC) $(CFLAGS) -c $< -o $@
$(BUILD)/startup.o: src/startup.s | $(BUILD); $(CC) $(CFLAGS) -c $< -o $@
$(BUILD)/firmware.elf: $(BUILD)/drivers.o $(BUILD)/control.o $(BUILD)/main.o $(BUILD)/startup.o; $(CC) $(LDFLAGS) $^ -o $@
$(BUILD)/firmware.bin: $(BUILD)/firmware.elf; arm-none-eabi-objcopy -O binary $< $@
$(BUILD)/firmware.hex: $(BUILD)/firmware.elf; arm-none-eabi-objcopy -O ihex $< $@
clean:; rm -rf $(BUILD)
