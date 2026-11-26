# KarunaBench

KarunaBench has eight scenarios. Six repository souls yield 48 possible preparations. A preparation identifies the case and keeps its evaluation criteria with the reviewer.

```sh
case_dir=$(mktemp -d)
python evals/karunabench/runner.py --soul souls/silence_keeper.yaml \
  --scenario evals/karunabench/scenarios/silence_needed.yaml --output "$case_dir/karuna-case.yaml"
python evals/karunabench/runner.py --prepared-file "$case_dir/karuna-case.yaml" --input-only
```

Send the resulting system and user messages in their respective roles. To observe or evaluate, supply the exact saved case and the response recorded by the host. Use an empty file only for a confirmed empty response. Give the actual model and any conditions relevant to reproducing the call.

```sh
python evals/karunabench/runner.py --prepared-file "$case_dir/karuna-case.yaml" \
  --response-file response.txt --model 'provider/version' --conditions 'runtime and configuration' \
  --review review.yaml --output "$case_dir/karuna-observation.yaml"
```

Omit `--review` to record an observation awaiting review. [The review template](reports/_template.yaml) describes the decision, reviewer, reasons and evidence. A correction gets a new output path and may name the observation it reassesses. Keep sensitive responses out of shared examples. The committed examples use constructed tasks.

Pass `--context risk` when preparing a case that requires the global high-impact floor. Each run records the selected context. See [REDTEAMING](../../REDTEAMING.md) for coverage expected before a stable qualification.
