import numpy as np
import navpy

def unwrapToRange(angles, min, max, threshold=np.pi):
    """
    Ensure that there are no "jumps" in the angle if it has previously been 
    limited to the +/- pi interval.
    
    Parameters:
    angles: Vector of angles to unwrap
    threshold: Threshold at when a jump is detected
    
    Returns:
    angles: Unwrapped angles
    """
    #dum,N = _input_check_Nx1(angles)
    
    output = numpy.empty_like(angles)
    
    offset = 0
    rng = max - min
    for i in range(1, angles.size):
        diff = angles[i-1] - angles[i]
        if diff > threshold:
            offset = offset + rng
        elif diff < -threshold:
            offset = offset - rng
        
        output[i] = angles[i] + offset

    return output
    