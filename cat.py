import sys

CHUNK_SIZE = 8192  # Fixed buffer size ensures O(1) memory

def cat(file):
    while chunk := file.read(CHUNK_SIZE):
        sys.stdout.buffer.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
