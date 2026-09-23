import json
import math


# 1. LOAD JSON DATA
def load_data(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    return data


# 2. CALCULATE DISTANCE
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2
    )

    return distance


# 3. FIND WAREHOUSE
def find_warehouse(warehouses, warehouse_id):
    if warehouse_id in warehouses:
        return warehouses[warehouse_id]

    return None


# 4. FIND NEAREST AGENT
def find_nearest_agent(agents, warehouse_location):
    nearest_agent = None
    shortest_distance = float("inf")

    for agent_id, agent_location in agents.items():

        distance = calculate_distance(
            agent_location,
            warehouse_location
        )

        if distance < shortest_distance:
            shortest_distance = distance
            nearest_agent = agent_id

    return nearest_agent, shortest_distance


# 5. SIMULATE PACKAGE DELIVERIES
def simulate_deliveries(data):

    delivery_results = []

    for package in data["packages"]:

        warehouse_location = find_warehouse(
            data["warehouses"],
            package["warehouse"]
        )

        agent_id, agent_to_warehouse = find_nearest_agent(
            data["agents"],
            warehouse_location
        )

        warehouse_to_destination = calculate_distance(
            warehouse_location,
            package["destination"]
        )

        total_distance = (
            agent_to_warehouse +
            warehouse_to_destination
        )

        result = {
            "package_id": package["id"],
            "agent_id": agent_id,
            "total_distance": total_distance
        }

        delivery_results.append(result)

    return delivery_results


# 6. CALCULATE AGENT STATISTICS
def calculate_agent_statistics(delivery_results):

    agent_stats = {}

    for result in delivery_results:

        agent_id = result["agent_id"]
        distance = result["total_distance"]

        if agent_id not in agent_stats:
            agent_stats[agent_id] = {
                "packages_delivered": 0,
                "total_distance": 0
            }

        agent_stats[agent_id]["packages_delivered"] += 1

        agent_stats[agent_id]["total_distance"] += distance

    return agent_stats


# 7. CREATE FINAL REPORT
def create_report(agent_stats):

    report = {}

    for agent_id, stats in agent_stats.items():

        packages_delivered = stats["packages_delivered"]
        total_distance = stats["total_distance"]

        efficiency = (
            total_distance /
            packages_delivered
        )

        report[agent_id] = {
            "packages_delivered": packages_delivered,
            "total_distance": round(total_distance, 2),
            "efficiency": round(efficiency, 2)
        }

    return report


# 8. FIND BEST AGENT
def find_best_agent(report):

    best_agent = None
    best_efficiency = float("inf")

    for agent_id, stats in report.items():

        if stats["efficiency"] < best_efficiency:
            best_efficiency = stats["efficiency"]
            best_agent = agent_id

    return best_agent


# 9. SAVE REPORT
def save_report(report, filename):

    with open(filename, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )


# 10. MAIN PROGRAM
def main():

    # Change the test case number here when testing
    data = load_data("test_cases/test_case_10.json")

    # Simulate deliveries
    delivery_results = simulate_deliveries(data)

    # Calculate statistics
    agent_stats = calculate_agent_statistics(
        delivery_results
    )

    # Create report
    report = create_report(agent_stats)

    # Find best agent
    best_agent = find_best_agent(report)

    # Add best agent to report
    report["best_agent"] = best_agent

    # Display final report
    print("\nFinal Report:")

    for key, value in report.items():
        print(key, ":", value)

    # Save report
    save_report(
        report,
        "report.json"
    )

    print("\nReport saved successfully to report.json")


# 11. START PROGRAM
if __name__ == "__main__":
    main()