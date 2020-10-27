# eNFA2DFA

fa들이 저장된 txt 파일들에서는

예를 들어 dfa1.txt에서

A B C  # states
0 1    # inputs
A      # start state
A B    # final states
A 0 A  # 이 밑으로는 transition function
A 1 B  # ex, <- 이 것은 delta(A, 1) = B를 의미
B 0 A
B 1 C
C 0 C
C 1 C

만약 transition function이
0 a 0 1
이렇게 되어있을 경우, 이것은 delta(0, a) = 0 or 1을 의미