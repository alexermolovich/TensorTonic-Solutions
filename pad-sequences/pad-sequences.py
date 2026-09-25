import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    largest_array_padding : int = 0  
    m : int = 0 
    r_seqs = None 
    if max_len is None: 
        for sub_array in seqs:
            m+=1 
            if largest_array_padding < len(sub_array):
                largest_array_padding = len(sub_array)
    else:
        largest_array_padding = max_len
        m = len(seqs)

    r_seqs = np.full((m, largest_array_padding), pad_value, dtype=int)
    update_counter : int  = 0
    
    for update_counter, sub_array in enumerate(seqs):
        truncated_seq = sub_array[:largest_array_padding]
        r_seqs[update_counter, :len(truncated_seq)] =  truncated_seq 
   
    return r_seqs 