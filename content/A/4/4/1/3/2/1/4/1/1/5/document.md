---
id: 53ed66f4-d010-4370-b83b-e36a185f12ad
docNo: A.4.4.1.3.2.1.4.1.1.5
name: Reference Implementation
type: Core
depth: 11
childType: sections_and_primary_docs
---

###### A.4.4.1.3.2.1.4.1.1.5 - Reference Implementation [Core]

A reference implementation of the time-weighted utilization formula is included herein. The reference implementation uses sample data and a 30 day interval for illustrative purposes.

`# Your list of real events: (timestamp, total_borrowed, total_supply)
events = [
(datetime(2025, 7, 25, 10), 100_000, 200_000),
(datetime(2025, 7, 25, 16), 120_000, 210_000),
(datetime(2025, 7, 26, 8), 130_000, 220_000),
(datetime(2025, 7, 27, 12), 110_000, 215_000),
(datetime(2025, 7, 28, 9), 140_000, 225_000),
]

# Ensure events are sorted
events.sort()

# Get time window
now = datetime.utcnow()
start_time = now - timedelta(days=30)

# Add synthetic first event (30d ago) using earliest known borrow/supply
first_real_ts, first_borrow, first_supply = events[0]
if first_real_ts > start_time:
events.insert(0, (start_time, first_borrow, first_supply))

# Add synthetic final event (now) using most recent known borrow/supply
last_real_ts, last_borrow, last_supply = events[-1]
if last_real_ts < now:
events.append((now, last_borrow, last_supply))

# Step 1: Compute utilization per event
utilizations = []
for ts, borrow, supply in events:
utilization = borrow / supply if supply != 0 else 0
utilizations.append((ts, utilization))

# Step 2: Compute time-weighted utilization average
weighted_sum = 0
total_time = 0

for i in range(len(utilizations) - 1):
ts1, util1 = utilizations[i]
ts2, _ = utilizations[i + 1]

time_diff = (ts2 - ts1).total_seconds()
weighted_sum += util1 * time_diff
total_time += time_diff

avg_utilization = weighted_sum / total_time if total_time > 0 else 0

print(f"30-day time-weighted average utilization: {avg_utilization:.2%}")`
