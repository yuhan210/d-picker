# d-picker

Datacenter scheduling simulator

- Supporting utility functions:
    1. Zero-one
    2. Hinge
    3. Square
    4. Logistic
    5. Exponential

- Assumptions
    1. Client only sends the next job when 
        - it's served by the server - scheduler won't see two jobs from the same client at each point in time
        - previous job has timed-out (utility function goes to 0, or really small in logistic utility function)

- Distribution assumptions:
    1. Client job generation based on poisson
    2. Client nwk delay (uplink/downlink?) follows normal


- Goal:
    How do different schedulers affect the overall utility? 
