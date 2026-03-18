log=[]
def p(line):
    print(line)
    log.append(line)
n=int(input("Enter number of resources: "))
m=int(input("Enter number of users: "))
print("Enter resource details (name capacity cost):")
resources=[]
for i in range(n):
    parts=input().split()
    resources.append({"name":parts[0],"capacity":int(parts[1]),"cost":int(parts[2])})
print("Enter user task requirements (name requirement):")
tasks=[]
for i in range(m):
    parts=input().split()
    tasks.append({"name":parts[0],"req":int(parts[1])})
resources.sort(key=lambda x:x["cost"])
allocation=[]
total_cost=0
p("\nResources:")
for r in resources:
    p(f"  {r['name']} | Capacity: {r['capacity']} | Cost: {r['cost']}")
p("\nTasks:")
for t in tasks:
    p(f"  {t['name']} | Requirement: {t['req']}")
p("\nAllocation Steps:")
for task in tasks:
    allocated=False
    for r in resources:
        if r["capacity"]>=task["req"]:
            p(f"  {task['name']} -> {r['name']} (cost={r['cost']}) [SELECTED]")
            r["capacity"]-=task["req"]
            total_cost+=r["cost"]
            allocation.append((task["name"],r["name"]))
            allocated=True
            break
        else:
            p(f"  {task['name']} -> {r['name']} (insufficient capacity, skipped)")
    if not allocated:
        p(f"  {task['name']} -> Not Allocated")
p("\nFinal Allocation:")
for a in allocation:
    p(f"  {a[0]} -> {a[1]}")
p(f"\nTotal Cost: {total_cost}")
p("Time Complexity: O(n x m)")
with open("cloud_resource_allocation_output.txt","w") as f:
    f.write("\n".join(log))
print("\nOutput saved to cloud_resource_allocation_output.txt")