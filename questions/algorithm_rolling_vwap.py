# Question: Compute rolling volume-weighted average prices for a trade stream.
#

from collections import deque
def generateTick(stream,window):
    cumm_pv=0
    cumm_v=0
    q=deque()

    idx=0
    while idx<len(stream):
        q.append(stream[idx])
        cumm_pv+=stream[idx][0]*stream[idx][1]
        cumm_v+=stream[idx][1]
        if len(q)<window:
            continue
        p,v=q.popleft()
        cumm_pv-=p*v
        cumm_v-=v
        yield cumm_pv/cumm_v

    if len(q)<window:
        return
def rolling_vwap(stream: list[tuple], window: int):
    yield from generateTick(stream,window)

