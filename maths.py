import numpy as np
import matplotlib.pyplot as plt

# Parameters
Tb = 1              # Bit duration
fs = 1000           # Sampling frequency
t = np.linspace(0, Tb, fs, endpoint=False)

fc = 5              # Carrier frequency
A = 1               # Amplitude

# -----------------------------
# 1. BPSK Waveform Generation
# -----------------------------
# bit 1 -> +carrier
bit1 = A * np.cos(2 * np.pi * fc * t)

# bit 0 -> -carrier
bit0 = -A * np.cos(2 * np.pi * fc * t)

# -----------------------------
# 2. Energy per Bit Calculation
# -----------------------------
# Discrete-time energy approximation
E1 = np.sum(bit1**2) / fs
E0 = np.sum(bit0**2) / fs

print("Energy of bit 1:", E1)
print("Energy of bit 0:", E0)

# -----------------------------
# 3. Orthogonality Verification
# -----------------------------
f1 = 5
f2 = 10

s1 = np.cos(2 * np.pi * f1 * t)
s2 = np.cos(2 * np.pi * f2 * t)

inner_product = np.sum(s1 * s2) / fs
print("Inner product of signals:", inner_product)

# -----------------------------
# 4. Multi-bit BPSK Signal
# -----------------------------
bits = np.random.randint(0, 2, 10)
print("Random bits:", bits)

bpsk_signal = []

for bit in bits:
    if bit == 1:
        bpsk_signal.extend(bit1)
    else:
        bpsk_signal.extend(bit0)

bpsk_signal = np.array(bpsk_signal)

# Time axis for full signal
t_total = np.linspace(0, Tb * len(bits), len(bpsk_signal), endpoint=False)

# -----------------------------
# 5. Visualization
# -----------------------------

# Plot bit waveforms
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, bit1)
plt.title("BPSK Waveform for Bit 1")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(t, bit0)
plt.title("BPSK Waveform for Bit 0")
plt.xlabel("Time")
plt.ylabel("Amplitude")

# Plot multi-bit signal
plt.subplot(3, 1, 3)
plt.plot(t_total, bpsk_signal)
plt.title("10-bit BPSK Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

# -----------------------------
# Constellation Diagram
# -----------------------------
plt.figure()
symbols = 2*bits - 1   # Map 0->-1, 1->+1
plt.scatter(symbols, np.zeros_like(symbols))
plt.title("BPSK Constellation Diagram")
plt.xlabel("In-phase")
plt.ylabel("Quadrature")
plt.grid()
plt.show()
