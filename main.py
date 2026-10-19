import hashlib
import time

def sha256_hash(data: str) -> str:
   
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def mock_poseidon_hash(input_val: int, prime_modulus: int = 21888242871839275222246405745257275088548364400416034343698204186575808495617) -> int:
    
    state = (input_val ** 5) % prime_modulus
    state = (state + 123456789) % prime_modulus
    return state

def run_benchmark():
    test_data = "Ethereum Foundation Cryptography Research"
    numeric_input = 123456789101112131415
    
    print("=" * 60)
    print("CRYPTOGRAPHIC HASH COMPARISON: SHA-256 vs MOCK POSEIDON")
    print("=" * 60)
    
    start_time = time.perf_counter()
    sha256_result = sha256_hash(test_data)
    sha256_time = (time.perf_counter() - start_time) * 1000
    
    print(f"\n[1] SHA-256 (Bit-wise Operations / ARX Architecture)")
    print(f"    Input:  '{test_data}'")
    print(f"    Output: {sha256_result}")
    print(f"    Time:   {sha256_time:.5f} ms")
    
    start_time = time.perf_counter()
    poseidon_result = mock_poseidon_hash(numeric_input)
    poseidon_time = (time.perf_counter() - start_time) * 1000
    
    print(f"\n[2] Poseidon-like Hash (Finite Field GF(p) / Algebraic Structure)")
    print(f"    Input (Field Element): {numeric_input}")
    print(f"    Output (Field Element): {poseidon_result}")
    print(f"    Time:   {poseidon_time:.5f} ms")
    
    print("\n" + "=" * 60)
    print("SUMMARY FOR ZERO-KNOWLEDGE PROOF (ZK-SNARK) CONTEXT:")
    print("• SHA-256 uses bitwise AND/XOR/ROTATIONS -> Expensive in R1CS/PlonK circuits (~25,000 constraints).")
    print("• Poseidon uses Field Multiplications (x^5 mod p) -> Highly optimized for ZK circuits (~200-300 constraints).")
    print("=" * 60)

if __name__ == "__main__":
    run_benchmark()