electrons = int(input())
shells = []

for shell in range(1 , electrons + 1):
    maxi_electrons_in_shell = 2 * shell ** 2
    if electrons >= maxi_electrons_in_shell:
        shells.append(maxi_electrons_in_shell)
        electrons -= maxi_electrons_in_shell
        if electrons == 0:
            break
    else:
        shells.append(electrons)
        break
print(shells)

