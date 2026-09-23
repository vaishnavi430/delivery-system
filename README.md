
# Delivery System

A Python-based delivery system that assigns packages to the nearest available agent and calculates the total delivery distance.

## Features

- Reads delivery data from JSON files
- Finds the nearest agent for each package
- Calculates distance using Euclidean distance
- Simulates Agent → Warehouse → Destination
- Calculates total delivery distance
- Calculates agent statistics
- Calculates delivery efficiency
- Identifies the best agent based on the lowest efficiency
- Generates a `report.json` file

## Technologies Used

- Python 3
- JSON
- Math
- Lists and Dictionaries
- Functions
- File Handling

No external Python libraries are required.

## Project Structure

```text
delivery-system/
│
├── delivery_system.py
├── base_case.json
├── report.json
├── README.md
│
└── test_cases/
    ├── test_case_1.json
    ├── test_case_2.json
    ├── test_case_3.json
    ├── test_case_4.json
    ├── test_case_5.json
    ├── test_case_6.json
    ├── test_case_7.json
    ├── test_case_8.json
    ├── test_case_9.json
    └── test_case_10.json
````

## How It Works

For each package:

1. The warehouse location is found.
2. The distance between each agent and the warehouse is calculated.
3. The nearest agent is selected.
4. The distance from the warehouse to the package destination is calculated.
5. Both distances are added to get the total delivery distance.
6. Agent statistics are calculated from the assigned packages.
7. The agent with the lowest efficiency value is selected as the best agent.
8. The final report is saved in `report.json`.

## Distance Calculation

The system uses Euclidean distance:

```text
distance = √((x2 - x1)² + (y2 - y1)²)
```

## Running the Project

Make sure Python 3 is installed.

Open the terminal in the project directory and run:

```bash
python delivery_system.py
```

The program currently reads the test case specified in `delivery_system.py`.

For example:

```python
data = load_data("test_cases/test_case_10.json")
```

To test another test case, change the file name:

```python
data = load_data("test_cases/test_case_1.json")
```

Then run:

```bash
python delivery_system.py
```

## Output

After execution, the program displays the final report in the terminal and creates:

```text
report.json
```

Example:

```json
{
    "A1": {
        "packages_delivered": 6,
        "total_distance": 200.92,
        "efficiency": 33.49
    },
    "A3": {
        "packages_delivered": 2,
        "total_distance": 30.98,
        "efficiency": 15.49
    },
    "best_agent": "A3"
}
```

## Testing

The program was tested using all 10 provided test cases:

* Test Case 1
* Test Case 2
* Test Case 3
* Test Case 4
* Test Case 5
* Test Case 6
* Test Case 7
* Test Case 8
* Test Case 9
* Test Case 10

All 10 test cases executed successfully.

## Author

Vaishnavi

