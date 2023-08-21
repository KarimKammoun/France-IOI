k, n = map(int, input().split())
cumul = [0]
ajout = cumul.append # <= très bon réflexe ; performance
force_cumulée = 0
for force in map(int, input().split()):
    force_cumulée += force
    ajout(force_cumulée)
tranche_forte = max(cumul[i + k] - cumul[i]
                        for i in range(n - k + 1))
print(tranche_forte)