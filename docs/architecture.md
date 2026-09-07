# Architecture

The project has five firmware layers:

1. Memory-mapped STM32 registers
2. Peripheral drivers
3. Digital control
4. Protection/validation
5. Application loop

The Python side supplies a control-oriented buck plant, automated tests,
performance metrics and a GenAI integration boundary.
