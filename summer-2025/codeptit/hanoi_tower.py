
# n dia -> 2^n - 1 buoc
def hanoi(n, source, mid, target, moves):
    if n == 1:
        moves.append(f"{source} -> {target}")
        return
    # B1: Chuyen n - 1 dia tu source sang mid
    hanoi(n - 1, source, target, mid, moves)
    # B2: Chuyen dia lon nhat sang target
    moves.append(f"{source} -> {target}")
    # B3: Chuyen n - 1 dia tu mid sang target
    hanoi(n - 1, mid, source, target, moves)

n = int(input())
moves = []
hanoi(n, "A", "B", "C", moves)
for m in moves:
    print(m)