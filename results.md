# o3-mini vs deepseek-r1 Agent Test

## Model Comparison

| Model                     | Context Window   | Max Output Tokens | SWE-Bench Score | Input Price (1M) | Output Price (1M) | Throughput (t/s) |
|---------------------------|------------------|-------------------|-----------------|------------------|-------------------|------------------|
| o3-mini                   | 200,000 tokens   | 100,000 tokens    | 49.3            | $1.10            | $4.40             | 1637             |
| deepseek-v3               | 64,000 tokens    | 8,000 tokens      | 42.0            | $0.14            | $0.28             | 22               |
| deepseek-r1               | 64,000 tokens    | 8,000 tokens      | 49.2            | $0.55            | $2.19             | 61               |
| gpt-4o                    | 128,000 tokens   | 16,384 tokens     | 33.2            | $2.50            | $10.00            | 64               |
| Claude 3.5 Sonnet         | 200,000 tokens   | 8,192 tokens      | 49.0            | $3.00            | $15.00            | 57               |
| Gemini 2.0 Flash          | 1,000,000 tokens | 8,192 tokens      | 51.8            | $0.10            | $0.40             | 248              |

**Note:** Throughput values found on OpenRouter and change daily based on availability and usage.

## Test 1 - Newsletter Crew - Specific Process

| Model            | Time  | Input Token | Output Token | Cost   | Completed Successfully |
|------------------|-------|-------------|--------------|--------|------------------------|
| gpt-4o           | 112 s | 16,869      | 4,788        | $0.09  | Yes                    |
| o3-mini          | 50 s  | 15,484      | 8,943        | $0.06  | Yes                    |
| deepseek-r1      | 576 s | 12,756      | 6,417        | $0.02  | Yes                    |
| deepseek-v3      | 644 s | 17,740      | 5,994        | $0.01  | Yes                    |
| Claude 3.5 Sonnet| 230 s | 45,256      | 11,082       | $0.30  | Yes                    |
| Gemini 2.0 Flash | 74 s  | 28,231      | 8,127        | $0.005 | Yes                    |

## Test 2 - Tools Test

| Model            | Time  | Input Token | Output Token | Cost   | Called Tools Properly |
|------------------|-------|-------------|--------------|--------|-----------------------|
| gpt-4o           | 22 s  | 7,747       | 549          | $0.02  | Pass                  |
| o3-mini          | 43 s  | 7,937       | 3,864        | $0.03  | Pass                  |
| deepseek-r1      | 224 s | 3,981       | 2,025        | $0.01  | Failed                |
| deepseek-v3      |  -    |      -      |      -       |  -     | Failed                |
| Claude 3.5 Sonnet| 27.5 s| 9,018       | 573          | $0.04  | Pass                  |
| Gemini 2.0 Flash | 15 s  | 17,774      | 452          | $0.003 | Pass                  |

## Test 3 - Context Window Test

| Model            | Time  | Input Token | Output Token | Cost   | Found Information | % of Context Used |
|------------------|-------|-------------|--------------|--------|-------------------|-------------------|
| gpt-4o           | 17 s  | 126,085     | 86           | $0.32  | Pass              | 95.31%            |
| o3-mini          | 19 s  | 190,288     | 1,015        | $0.21  | Pass              | 94.71%            |
| deepseek-r1      | 53.7 s| 60,491      | 735          | $0.03  | Pass              | 92.19%            |
| deepseek-v3      | 296 s | 93,350      | 2,173        | $0.01  | Pass              | 92.19%            |
| Claude 3.5 Sonnet| 67 s  | 56,138      | 1,456        | $0.19  | Pass              | 13%               |
| Gemini 2.0 Flash | 41 s  | 800,878     | 242          | $0.08  | Pass              | 80.09%            |
