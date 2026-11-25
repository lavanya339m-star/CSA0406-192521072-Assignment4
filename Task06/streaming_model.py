#!/usr/bin/env python3
"""Simple analytical comparison; outputs are model estimates, not hardware benchmarks."""
videos=1200
size_mib=700
chunk_mib=4
catalogue_mib=videos*size_mib
hot_mib=catalogue_mib*0.20
concurrent=20000
bitrate_mbps=5
print("ASSUMPTION-BASED MODEL (not a physical benchmark)")
print(f"Catalogue: {catalogue_mib:,} MiB = {catalogue_mib/1024:.1f} GiB")
print(f"Two local copies: {2*catalogue_mib/1024/1024:.2f} TiB")
print(f"20% hot set: {hot_mib/1024:.1f} GiB")
print(f"Chunks per 700 MiB video: {size_mib//chunk_mib}")
print(f"Concurrent payload throughput: {concurrent*bitrate_mbps/1000:.1f} Gbit/s")
for label,hit,rate in [("HDD-origin",0.10,150),("SSD-hot-tier",0.80,1500)]:
    # illustrative 4 MiB chunk service time when served by assumed device
    ms=chunk_mib/(rate/1000)
    print(f"{label}: assumed cache hit={hit:.0%}, device={rate} MB/s, 4MiB read≈{ms:.1f} ms")
print("Random seek: indexed design reads one 4 MiB chunk plus index metadata.")
