import grad
import graph
import perm
import mobius

print("Проверка порядка для S_n")
for i in range(1, 6):
    s_n = perm.check_order(perm.generate_permutations(i))
    diag = graph.HasseDiagram(s_n)
    print("S", i,'--', grad.check_paths(diag.hasse_diagram))

print("Проверка порядка для B_n")
for i in range(1, 5):
    a = perm.check_order(perm.normalize_perms_b(perm.get_perm_b(i)))
    diag = graph.HasseDiagram(a)
    print("B", i,'--', grad.check_paths(diag.hasse_diagram))

print("Проверка куба для S_n")
for i in range(1, 6):
    s_n = perm.check_degree(perm.generate_permutations(i), 3)
    diag = graph.HasseDiagram(s_n)
    print("S", i, '--', grad.check_paths(diag.hasse_diagram))

print("Проверка куба для B_n")
for i in range(1, 6):
    s_n = perm.check_degree(perm.normalize_perms_b(perm.get_perm_b(i)), 3)
    diag = graph.HasseDiagram(s_n)
    print("S", i, '--', grad.check_paths(diag.hasse_diagram))

print("Строим функцию Мебиуса")
for i in range(1, 6):
    s_n = perm.check_order(perm.generate_permutations(i))
    diag = graph.HasseDiagram(s_n)
    a = mobius.mobius_func(diag.hasse_diagram)
    print(s_n)
    print(f"-------n={i}-------")
    for i in a:
        print(i)
