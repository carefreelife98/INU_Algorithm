# from collections import deque
#
# MAX = 100
#
# def match(t, next1, next2, scan, ch):
#     dq = deque(maxlen=100)
#     j = 0
#     N = len(t - 1)
#     state = next1[0]
#     dq.append(scan)
#     while state != 0:
#         if state == scan:
#             j += 1
#             if len(dq) == 0:
#                 dq.appendleft(next1[0])
#             dq.append(scan)
#         elif ch[state] == t[j]:
#             dq.append(next1[state])
#         elif ch[state] == ' ':
#             n1 = next1[state]
#             n2 = next2[state]
#             dq.appendleft(n1)
#             if n1 != n2:
#                 dq.appendleft(n2)
#     if len(dq) == 0:
#         return j
#     if j > N:
#         return 0
#     state = dq.popleft()
#     if dq
