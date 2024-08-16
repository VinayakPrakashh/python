import numpy as np

def overlap_save(signal, impulse_response, block_size):
    num_blocks = len(signal) // block_size
    output_signal = np.zeros(len(signal) + len(impulse_response) - 1)

    for i in range(num_blocks):
        block = signal[i * block_size : (i + 1) * block_size]
        padded_block = np.pad(block, (0, len(impulse_response) - 1), 'constant')
        padded_impulse_response = np.pad(impulse_response, (0, len(padded_block) - len(impulse_response)), 'constant')
        block_fft = np.fft.fft(padded_block)
        impulse_response_fft = np.fft.fft(padded_impulse_response)
        convolution_fft = block_fft * impulse_response_fft
        convolution = np.fft.ifft(convolution_fft)
        output_signal[i * block_size : i * block_size + len(convolution)] += convolution.real

    return output_signal

# Example usage
signal = eval(input("Enter the input sequence: "))
impulse_response = eval(input("Enter the impulse sequence: "))    
block_size = 4
output_signal = overlap_save(signal, impulse_response, block_size)
print("Output signal:", output_signal)