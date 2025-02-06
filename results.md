# o3-mini vs deepseek-r1 Agent Test

## Model Comparison

| Model            | Context Window | Max Output Tokens | SWE-Bench Score | Input Price (1M) | Output Price (1M) | Throughput (t/s) |
|------------------|----------------|-------------------|-----------------|------------------|-------------------|------------------|
| o3-mini          | 200,000 tokens | 100,000 tokens    | 49.3            | $1.10            | $4.40             | 1637             |
| deepseek-v3      | 64,000 tokens  | 8,000 tokens      | 42.0            | $0.14            | $0.28             | 22               |
| deepseek-r1      | 64,000 tokens  | 8,000 tokens      | 49.2            | $0.55            | $2.19             | 61               |
| gpt-4o           | 128,000 tokens | 16,384 tokens     | 33.2            | $2.50            | $10.00            | 64               |
| Claude 3.5 Sonnet| 200,000 tokens | 8,192 tokens      | 49.0            | $3.00            | $15.00            | 51               |

**Note:** Throughput values found on OpenRouter and change daily based on availability and usage.

## Test 1 - Newsletter Crew - Specific Process

| Model             | Time  | Input Token | Output Token | Cost  | Completed Successfully |
|-------------------|-------|-------------|--------------|-------|------------------------|
| gpt-4o            | 112 s | 16,869      | 4,788        | $0.09 | Yes                    |
| o3-mini           | 50 s  | 15,484      | 8,943        | $0.06 | Yes                    |
| deepseek-r1       | 576 s | 12,756      | 6,417        | $0.02 | Yes                    |
| deepseek-v3       | 644 s | 17,740      | 5,994        | $0.01 | Yes                    |
| Claude 3.5 Sonnet | 381 s | 17,459      | 5,659        | $0.14 | Yes                    |

## Test 2 - Tools Test

| Model             | Time  | Input Token | Output Token | Cost  | Called Tools Properly | Notes                                                                                |
|-------------------|-------|-------------|--------------|-------|-----------------------|--------------------------------------------------------------------------------------|
| gpt-4o            | 22 s  | 7,747       | 549          | $0.02 | Pass                  |                                                                                      |
| o3-mini           | 43 s  | 7,937       | 3,864        | $0.03 | Pass                  |                                                                                      |
| deepseek-r1       | 224 s | 3,981       | 2,025        | $0.01 | Failed                | Got 80% of the way through, then failed by calling the wrong tool and erroring out   |
| deepseek-v3       |  -    |      -      |      -       |  -    | Failed                |                                                                                      |
| Claude 3.5 Sonnet | 89 s  | 7,161       | 604          | $0.03 | Pass                  |                                                                                      |

## Test 3 - Context Window Test
