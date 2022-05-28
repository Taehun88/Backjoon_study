# Backjoon_12851 숨바꼭질 2

* 문제분석
    > 수빈이는 현재 위치에서 3가지 행동 가능
    > 가장 빠른 시간과 경우의 수 출력

* Logic
    > 수빈이는 현재 위치에서 3가지 행동 가능 -> 해당 지점에서 각 행동을 전부 해본다
    > 가장 빠른 시간과 경우의 수 출력 -> 시간과 경우의 수를 지정한다

* Algorithm
    > BFS

* Algorithm 선택이유
    > 3가지 행동은 current node에서 edge가 3개인 Graph로 생각 가능
    > 가장 빠른 시간 -> 최단경로, 경우의 수 -> node 까지 가는 path 개수로 생각
    > 해당 내용을 Graph와 path로 생각하는 것이 어려웠음
    > Back Tracking으로 풀어보려 했으나 Timeout 발생